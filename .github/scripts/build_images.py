#!/usr/bin/env python3
"""
build_images.py — responsive derivatives for Gallery photos

For every raster photo inside a per-post image folder
(assets/img/posts/<post-slug>/*.jpg|jpeg|png — the folder shape from ADR-0009):

  1. Sanitizes the committed source *in place* when it still carries metadata:
     bakes the EXIF orientation into the pixels and strips EXIF/XMP (GPS
     coordinates, device model, timestamps…) while keeping the ICC profile.
     A JPEG is re-encoded with its own quantization tables and chroma
     subsampling, so the generation loss is negligible. Idempotent — a clean
     file is never rewritten. The sanitized file is what galleries link to
     (the GLightbox full-resolution target) and what <img src> falls back to.

  2. Generates AVIF and WebP derivatives at a few widths, never upscaling,
     under assets/img/derived/<post-slug>/ as
     <stem>-<sha1[:8] of the source>-<width>.<ext>. The hash means a changed
     source can't collide with a stale derivative, and browsers cache-bust.

  3. Writes _data/images.json — the intrinsic (post-orientation) width/height
     of each source plus its derivative sets — which _includes/photo.html reads
     to emit <picture> with srcset/sizes/width/height.

Derivatives and the manifest are build output, not source (both gitignored):
deploy.yml runs this script before `jekyll build`, caching assets/img/derived/
between runs keyed on the sources. Run it locally before `jekyll serve` to see
the same markup in development. Decision record: docs/adr/0011.

Usage:
  python3 .github/scripts/build_images.py [--no-sanitize] [--force] [--quiet]
"""

import argparse
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    from PIL import Image, ImageOps, JpegImagePlugin
except ImportError:  # pragma: no cover
    print("::error::Pillow is required — python3 -m pip install 'Pillow>=11.2'")
    sys.exit(2)

# ── Config ────────────────────────────────────────────────────────────────────

ROOT         = Path(__file__).resolve().parents[2]
SOURCE_ROOT  = ROOT / "assets" / "img" / "posts"
DERIVED_ROOT = ROOT / "assets" / "img" / "derived"
MANIFEST     = ROOT / "_data" / "images.json"

SOURCE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

# Rungs of the srcset. Gallery thumbnails render at ~130–250 CSS px (so 480w
# covers 1x/2x and 960w covers 3x screens); 1600w exists for a photo placed
# standalone at full article width. A source narrower than the largest rung
# also gets a rung at its own width so nothing is ever upscaled.
WIDTHS = (480, 960, 1600)

# Encoder settings. AVIF q55 ≈ JPEG q80 visually at roughly a third of the
# bytes; WebP q75 is the fallback for browsers without AVIF. Both strip
# EXIF/XMP explicitly and carry the source's ICC profile.
FORMATS = {
    "avif": {"quality": 55, "speed": 6},
    "webp": {"quality": 75, "method": 5},
}

HASH_LENGTH     = 8
ORIENTATION_TAG = 0x0112
GPS_IFD_TAG     = 0x8825
RESAMPLE        = Image.Resampling.LANCZOS

# ── Helpers ───────────────────────────────────────────────────────────────────

def site_url(path: Path) -> str:
    """Repo-relative path as a site-relative URL (baseurl is applied by Liquid)."""
    return "/" + path.relative_to(ROOT).as_posix()


def source_photos() -> list[Path]:
    """Raster photos inside per-post folders, sorted for deterministic output."""
    if not SOURCE_ROOT.exists():
        return []
    photos: list[Path] = []
    for folder in sorted(p for p in SOURCE_ROOT.iterdir() if p.is_dir()):
        for path in sorted(folder.rglob("*")):
            if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS:
                photos.append(path)
    return photos


def file_digest(path: Path) -> str:
    sha1 = hashlib.sha1()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            sha1.update(chunk)
    return sha1.hexdigest()[:HASH_LENGTH]


def display_size(im: Image.Image) -> tuple[int, int]:
    """Width/height as the photo is meant to be seen, honouring EXIF orientation."""
    width, height = im.size
    if im.getexif().get(ORIENTATION_TAG, 1) in (5, 6, 7, 8):
        width, height = height, width
    return width, height


def rungs_for(source_width: int) -> list[int]:
    widths = [w for w in WIDTHS if w < source_width]
    if source_width <= WIDTHS[-1]:
        widths.append(source_width)
    return widths


def to_web_mode(im: Image.Image) -> Image.Image:
    """Normalise palette/CMYK/etc. to something AVIF and WebP encode losslessly in spirit."""
    if im.mode in ("RGB", "RGBA", "L"):
        return im
    if im.mode == "P" and "transparency" in im.info or im.mode in ("LA", "PA"):
        return im.convert("RGBA")
    return im.convert("RGB")


# ── Step 1: sanitize sources ──────────────────────────────────────────────────

def needs_sanitizing(im: Image.Image) -> bool:
    return len(im.getexif()) > 0 or bool(im.info.get("xmp"))


def sanitize(path: Path) -> bool:
    """Bake orientation and strip metadata in place. Returns True when rewritten."""
    with Image.open(path) as im:
        if not needs_sanitizing(im):
            return False
        # Phone JPEGs with an embedded preview/motion clip open as "MPO"
        # (multi-picture); they are JPEGs and are written back as one frame.
        fmt = "JPEG" if im.format in ("JPEG", "MPO") else im.format
        save_kwargs: dict = {"exif": b""}
        if im.info.get("icc_profile"):
            save_kwargs["icc_profile"] = im.info["icc_profile"]
        if fmt == "JPEG":
            # Reuse the source's own quantization tables and subsampling so the
            # re-encode is as close to lossless as a JPEG round-trip can be.
            save_kwargs["qtables"] = im.quantization
            sampling = JpegImagePlugin.get_sampling(im)
            if sampling >= 0:
                save_kwargs["subsampling"] = sampling
        fixed = ImageOps.exif_transpose(im)
        fixed.info.pop("exif", None)
        fixed.info.pop("xmp", None)
        tmp = path.with_name(path.name + ".tmp")
        fixed.save(tmp, format=fmt, **save_kwargs)
    os.replace(tmp, path)
    return True


# ── Step 2: derivatives ───────────────────────────────────────────────────────

def plan(source: Path) -> tuple[str, dict, list[tuple[Path, int, str]]]:
    """Manifest entry for one source plus the (output, width, format) jobs it implies."""
    with Image.open(source) as im:
        width, height = display_size(im)
    digest = file_digest(source)
    derived_dir = DERIVED_ROOT / source.parent.relative_to(SOURCE_ROOT)
    key = source.relative_to(SOURCE_ROOT).as_posix()

    entry: dict = {"width": width, "height": height}
    jobs: list[tuple[Path, int, str]] = []
    for fmt in FORMATS:
        entry[fmt] = []
        for rung in rungs_for(width):
            output = derived_dir / f"{source.stem}-{digest}-{rung}.{fmt}"
            entry[fmt].append({"w": rung, "path": site_url(output)})
            jobs.append((output, rung, fmt))
    return key, entry, jobs


def render(source: Path, jobs: list[tuple[Path, int, str]]) -> int:
    """Decode the source once, then resize per rung and encode every format."""
    with Image.open(source) as im:
        base = to_web_mode(ImageOps.exif_transpose(im))
    icc = base.info.get("icc_profile")

    by_width: dict[int, list[tuple[Path, str]]] = {}
    for output, rung, fmt in jobs:
        by_width.setdefault(rung, []).append((output, fmt))

    for rung, outputs in sorted(by_width.items(), reverse=True):
        if rung < base.width:
            new_height = max(1, round(base.height * rung / base.width))
            resized = base.resize((rung, new_height), RESAMPLE, reducing_gap=3.0)
        else:
            resized = base
        for output, fmt in outputs:
            kwargs = dict(FORMATS[fmt], exif=b"", xmp=b"")
            if icc:
                kwargs["icc_profile"] = icc
            output.parent.mkdir(parents=True, exist_ok=True)
            tmp = output.with_name(output.name + ".tmp")
            resized.save(tmp, format=fmt.upper(), **kwargs)
            os.replace(tmp, output)
    return len(jobs)


def prune(expected: set[Path]) -> int:
    """Delete derivatives that no current source accounts for (stale hashes, removed photos)."""
    if not DERIVED_ROOT.exists():
        return 0
    removed = 0
    for path in sorted(DERIVED_ROOT.rglob("*"), reverse=True):
        if path.is_file() and path not in expected:
            path.unlink()
            removed += 1
        elif path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    return removed


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Sanitize Gallery photos and build their responsive derivatives.")
    parser.add_argument("--no-sanitize", action="store_true", help="leave committed sources untouched")
    parser.add_argument("--force", action="store_true", help="regenerate derivatives that already exist")
    parser.add_argument("-q", "--quiet", action="store_true", help="only print the summary")
    args = parser.parse_args()

    log = (lambda *_: None) if args.quiet else print
    started = time.time()

    sources = source_photos()
    if not sources:
        print(f"No Gallery photos under {SOURCE_ROOT.relative_to(ROOT)}/<post-slug>/ — nothing to do.")

    sanitized: list[Path] = []
    if not args.no_sanitize:
        for source in sources:
            if sanitize(source):
                sanitized.append(source)
                log(f"  🧹 sanitized  {source.relative_to(ROOT).as_posix()}")

    manifest: dict[str, dict] = {}
    expected: set[Path] = set()
    work: list[tuple[Path, list[tuple[Path, int, str]]]] = []
    for source in sources:
        key, entry, jobs = plan(source)
        manifest[key] = entry
        expected.update(output for output, _, _ in jobs)
        pending = [job for job in jobs if args.force or not job[0].exists()]
        if pending:
            work.append((source, pending))

    generated = 0
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 2) as pool:
        for source, count in zip((s for s, _ in work), pool.map(lambda w: render(*w), work)):
            generated += count
            log(f"  🖼️  {count:2d} derivative(s)  {source.relative_to(ROOT).as_posix()}")

    removed = prune(expected)

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        f"\n{len(sources)} source photo(s), {len(sanitized)} sanitized, "
        f"{generated} derivative(s) generated, {len(expected) - generated} reused, "
        f"{removed} stale removed — {time.time() - started:.1f}s\n"
        f"manifest: {MANIFEST.relative_to(ROOT).as_posix()}  derivatives: {DERIVED_ROOT.relative_to(ROOT).as_posix()}/"
    )
    if sanitized:
        print(
            "\nSanitized sources were rewritten in place — commit them, they are the "
            "photos the site publishes and links to (orientation baked, EXIF/GPS/XMP removed)."
        )


if __name__ == "__main__":
    main()
