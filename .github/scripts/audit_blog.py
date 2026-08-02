#!/usr/bin/env python3
"""
audit_blog.py — Jekyll blog structure auditor
Checks for missing category pages, tag pages, feed files,
incomplete post front matter, and broken external images.
Reports via GitHub annotations and $GITHUB_STEP_SUMMARY.
"""

import os
import re
import sys
import time
import urllib.request
import urllib.error
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

ROOT         = Path(__file__).resolve().parents[2]
POSTS_DIR    = ROOT / "_posts"
TAGS_DIR     = ROOT / "topicos"
CATS_DIR     = ROOT / "categorias"
FEEDS_DIR    = ROOT / "feed"
ASSETS_DIR   = ROOT / "assets"
CATEGORIES_DATA_FILE = ROOT / "_data" / "categories.yml"
SUMMARY_FILE = ROOT / "audit-report.md"

REQUIRED_FRONT_MATTER = [
    "layout", "title", "description", "date",
    "categories", "tags", "reading_time", "image",
]

# External image check settings
IMG_TIMEOUT        = 10        # seconds per request
IMG_MAX_WORKERS    = 8         # parallel HEAD requests
IMG_MAX_RETRIES    = 2         # retries on transient errors
IMG_RETRY_DELAY    = 2         # seconds between retries
IMG_USER_AGENT     = (
    "Mozilla/5.0 (compatible; Jekyll-blog-auditor/1.0; "
    "+https://github.com/guibranco/blog)"
)

# Patterns to extract external image URLs from markdown/HTML content
EXTERNAL_IMG_PATTERNS = [
    # Markdown: ![alt](https://...)
    re.compile(r'!\[[^\]]*\]\((https?://[^\s\)]+)\)'),
    # HTML: src="https://..."  or  src='https://...'
    re.compile(r'src=["\x27](https?://[^\s"\']+)["\x27]'),
    # HTML: href="https://...jpg/png/gif/webp/svg"
    re.compile(r'href=["\x27](https?://[^\s"\']+\.(?:jpe?g|png|gif|webp|svg))["\x27]', re.I),
    # CSS background-image: url('https://...')
    re.compile(r'url\(["\x27]?(https?://[^\s"\')\]]+)["\x27]?\)'),
]

# Domains that reliably reject HEAD / return false 4xx — skip them
SKIP_DOMAINS = {
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "cdnjs.cloudflare.com",
    "cdn.jsdelivr.net",
}

# `image:` feeds jekyll-seo-tag's og:image/twitter:image — social crawlers need
# a raster format, SVG is not reliably rendered by Facebook/Twitter/LinkedIn.
VALID_OG_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
# `cover:` is the on-page hero graphic — any standard web image format is fine.
VALID_COVER_EXTENSIONS = {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"}

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Basic Latin slugify matching Jekyll's `slugify: 'latin'` filter."""
    replacements = {
        'ã': 'a', 'â': 'a', 'á': 'a', 'à': 'a',
        'ê': 'e', 'é': 'e', 'è': 'e',
        'í': 'i', 'ì': 'i',
        'ô': 'o', 'õ': 'o', 'ó': 'o',
        'ú': 'u', 'ü': 'u',
        'ç': 'c',
    }
    s = text.lower()
    for src, dst in replacements.items():
        s = s.replace(src, dst)
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s.strip())
    return re.sub(r'-+', '-', s).strip('-')


def parse_front_matter(path: Path) -> tuple[dict, str]:
    """Return (front_matter_dict, body_text) for a markdown file.

    Scalar and inline-list (`key: [a, b]`) values are stored as strings.
    Block-style lists (`key:` followed by indented `- item` lines, as used
    for `subcategories:`) are stored as a Python list of raw item strings.
    """
    text = path.read_text(encoding='utf-8')
    fm, body, in_fm, fm_done = {}, [], False, False
    pending_list_key = None
    for i, line in enumerate(text.splitlines(keepends=True)):
        if i == 0 and line.strip() == '---':
            in_fm = True
            continue
        if in_fm and line.strip() == '---':
            in_fm, fm_done = False, True
            continue
        if in_fm:
            list_item = re.match(r'^\s+-\s*(.+)$', line)
            if pending_list_key and list_item:
                fm[pending_list_key].append(list_item.group(1).strip())
                continue
            pending_list_key = None
            m = re.match(r'^(\w+):\s*(.*)', line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if val == '':
                    pending_list_key = key
                    fm[key] = []
                else:
                    fm[key] = val
        elif fm_done:
            body.append(line)
    return fm, ''.join(body)


def extract_list_field(raw) -> list[str]:
    """Parse `[foo, bar]`, a block-parsed list, or a single YAML value into a list."""
    if isinstance(raw, list):
        return [str(i).strip().strip('"').strip("'") for i in raw if str(i).strip()]
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        items = raw[1:-1].split(',')
        return [i.strip().strip('"').strip("'") for i in items if i.strip()]
    return [raw.strip('"').strip("'")] if raw else []


def load_categories_data() -> dict[str, dict]:
    """Parse `_data/categories.yml` into {category_name: {"slug", "subcategories"}}.

    `subcategories` maps subcategory name -> slug. A minimal hand-rolled
    parser is used instead of PyYAML to avoid an extra CI dependency, since
    the file has a fixed, simple structure.
    """
    if not CATEGORIES_DATA_FILE.exists():
        return {}

    def unquote(s: str) -> str:
        s = s.strip()
        if len(s) >= 2 and s[0] == s[-1] and s[0] in ('"', "'"):
            return s[1:-1]
        return s

    categories: dict[str, dict] = {}
    current = None
    in_subs = False
    pending_sub = None

    for raw_line in CATEGORIES_DATA_FILE.read_text(encoding='utf-8').splitlines():
        if not raw_line.strip():
            continue
        indent = len(raw_line) - len(raw_line.lstrip(' '))
        line = raw_line.strip()

        m = re.match(r'^-\s*name:\s*(.+)$', line)
        if m and indent == 0:
            name = unquote(m.group(1))
            current = {"slug": "", "subcategories": {}}
            categories[name] = current
            in_subs = False
            pending_sub = None
            continue

        if current is None:
            continue

        if indent == 2 and line.startswith('slug:'):
            current["slug"] = unquote(line.split(':', 1)[1])
            in_subs = False
            continue
        if indent == 2 and line.startswith('subcategories:'):
            in_subs = True
            continue

        if in_subs:
            m2 = re.match(r'^-\s*name:\s*(.+)$', line)
            if m2 and indent == 4:
                pending_sub = unquote(m2.group(1))
                current["subcategories"][pending_sub] = ""
                continue
            if indent == 6 and line.startswith('slug:') and pending_sub is not None:
                current["subcategories"][pending_sub] = unquote(line.split(':', 1)[1])
                continue

    return categories


def local_asset_path(value: str) -> Path | None:
    """Resolve a front matter image/cover value to a repo-relative path.

    Returns None for external (http/https) URLs or empty values.
    """
    value = value.strip()
    if not value or value.startswith("http://") or value.startswith("https://"):
        return None
    return ROOT / value.lstrip("/")


def get_extension(value: str) -> str:
    """Return the lowercase file extension of an image path/URL, ignoring any query/fragment."""
    value = value.strip().split("?", 1)[0].split("#", 1)[0]
    return Path(value).suffix.lower()


def extract_external_images(body: str) -> list[str]:
    """Return all unique external image URLs found in post body."""
    urls = set()
    for pattern in EXTERNAL_IMG_PATTERNS:
        for match in pattern.finditer(body):
            url = match.group(1).rstrip(')')
            # Skip known CDN/font domains
            domain = re.sub(r'^https?://', '', url).split('/')[0]
            if domain not in SKIP_DOMAINS:
                urls.add(url)
    return sorted(urls)


def check_external_image(url: str) -> tuple[str, int | str]:
    """
    HEAD-request a URL, return (url, status_code_or_error_string).
    Falls back to GET if HEAD returns 405. Retries on transient errors.
    """
    last_error: int | str = "unknown"
    for attempt in range(IMG_MAX_RETRIES + 1):
        if attempt > 0:
            time.sleep(IMG_RETRY_DELAY)
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(
                url, method=method,
                headers={
                    "User-Agent": IMG_USER_AGENT,
                    "Accept": "image/*,*/*;q=0.8",
                },
            )
            try:
                with urllib.request.urlopen(req, timeout=IMG_TIMEOUT) as resp:
                    return url, resp.status
            except urllib.error.HTTPError as e:
                last_error = e.code
                if e.code == 405 and method == "HEAD":
                    continue   # try GET
                if e.code in (429, 503, 502, 504):
                    break      # retry after delay
                return url, e.code
            except urllib.error.URLError as e:
                last_error = str(e.reason)
                break          # network error — retry
            except Exception as e:
                last_error = str(e)
                break
    return url, last_error


def gh_warning(file: str, message: str):
    print(f"::warning file={file}::{message}")


def gh_error(file: str, message: str):
    print(f"::error file={file}::{message}")


# ── Audit ─────────────────────────────────────────────────────────────────────

def audit() -> tuple[dict, set, set]:
    issues: dict = {
        "missing_tag_pages":          [],
        "missing_category_pages":     [],
        "missing_feed_files":         [],
        "incomplete_front_matter":    [],
        "posts_without_image":        [],
        "posts_without_description":  [],
        "posts_without_reading_time": [],
        "broken_external_images":     [],   # {file, url, status}
        "skipped_external_images":    [],   # {file, url, reason}
        "unregistered_categories":    [],   # {file, category}
        "invalid_subcategories":      [],   # {file, subcategory, reason}
        "missing_local_images":       [],   # {file, field, path}
        "invalid_image_extensions":   [],   # {file, field, path, extension, expected}
    }

    all_tags: set[str] = set()
    all_cats: set[str] = set()
    categories_data = load_categories_data()

    # url -> [(relative_file, front_matter_image)]
    url_to_posts: dict[str, list[tuple[str, bool]]] = defaultdict(list)

    # ── Parse all posts ───────────────────────────────────────────────────────
    posts = sorted(POSTS_DIR.glob("*.md")) if POSTS_DIR.exists() else []
    if not posts:
        print("::warning::No posts found in _posts/")
        return issues, all_tags, all_cats

    print(f"\n📄 Scanning {len(posts)} post(s)...\n")

    for post in posts:
        rel = str(post.relative_to(ROOT))
        fm, body = parse_front_matter(post)

        # Collect categories / tags
        cats = extract_list_field(fm.get("categories", ""))
        tags = extract_list_field(fm.get("tags", ""))
        all_cats.update(cats)
        all_tags.update(tags)

        # Missing required front matter
        missing_fields = [f for f in REQUIRED_FRONT_MATTER if f not in fm]
        if missing_fields:
            issues["incomplete_front_matter"].append(
                {"file": rel, "missing": missing_fields}
            )
            for field in missing_fields:
                gh_warning(rel, f"Missing front matter field: `{field}`")

        if "image" not in fm:
            issues["posts_without_image"].append(rel)
        if "description" not in fm:
            issues["posts_without_description"].append(rel)
        if "reading_time" not in fm:
            issues["posts_without_reading_time"].append(rel)

        # Categories must be registered in _data/categories.yml (drives nav,
        # breadcrumbs and schema.org markup — an unregistered category silently
        # breaks those includes for the post).
        for cat in cats:
            if cat and cat not in categories_data:
                issues["unregistered_categories"].append({"file": rel, "category": cat})
                gh_error(rel, f"Category '{cat}' is not registered in _data/categories.yml")

        # Subcategories are written as "Parent/Child" and must resolve to a
        # parent category + subcategory pair that exists in categories.yml.
        for subcat in extract_list_field(fm.get("subcategories", "")):
            if "/" not in subcat:
                issues["invalid_subcategories"].append({
                    "file": rel, "subcategory": subcat,
                    "reason": "expected format 'Category/Subcategory'",
                })
                gh_error(rel, f"Malformed subcategory '{subcat}' — expected 'Category/Subcategory'")
                continue
            parent, child = subcat.split("/", 1)
            parent, child = parent.strip(), child.strip()
            if parent not in categories_data:
                issues["invalid_subcategories"].append({
                    "file": rel, "subcategory": subcat,
                    "reason": f"category '{parent}' is not registered in _data/categories.yml",
                })
                gh_error(rel, f"Subcategory '{subcat}' — category '{parent}' is not registered in _data/categories.yml")
            elif child not in categories_data[parent]["subcategories"]:
                issues["invalid_subcategories"].append({
                    "file": rel, "subcategory": subcat,
                    "reason": f"subcategory '{child}' is not registered under '{parent}' in _data/categories.yml",
                })
                gh_error(rel, f"Subcategory '{subcat}' is not registered under '{parent}' in _data/categories.yml")

        # Local image/cover files referenced in front matter must exist in the branch.
        for field in ("image", "cover"):
            value = fm.get(field, "")
            if not value:
                continue
            asset_path = local_asset_path(value)
            if asset_path is not None and not asset_path.exists():
                issues["missing_local_images"].append({"file": rel, "field": field, "path": value})
                gh_error(rel, f"Missing local `{field}` file: {value}")

        # `image:` (og:image/twitter:image) must be a raster format social
        # crawlers render; `cover:` (on-page hero) is expected to be an SVG.
        image_value = fm.get("image", "")
        if image_value:
            ext = get_extension(image_value)
            if ext not in VALID_OG_IMAGE_EXTENSIONS:
                issues["invalid_image_extensions"].append({
                    "file": rel, "field": "image", "path": image_value,
                    "extension": ext or "(none)",
                    "expected": "/".join(sorted(VALID_OG_IMAGE_EXTENSIONS)),
                })
                gh_error(
                    rel,
                    f"`image:` uses extension '{ext or '(none)'}' — Open Graph needs a raster "
                    f"image ({'/'.join(sorted(VALID_OG_IMAGE_EXTENSIONS))}); use the SVG for `cover:` instead"
                )

        cover_value = fm.get("cover", "")
        if cover_value:
            ext = get_extension(cover_value)
            if ext not in VALID_COVER_EXTENSIONS:
                issues["invalid_image_extensions"].append({
                    "file": rel, "field": "cover", "path": cover_value,
                    "extension": ext or "(none)",
                    "expected": "/".join(sorted(VALID_COVER_EXTENSIONS)),
                })
                gh_warning(
                    rel,
                    f"`cover:` uses extension '{ext or '(none)'}' — expected one of "
                    f"{'/'.join(sorted(VALID_COVER_EXTENSIONS))}"
                )

        # Collect external image URLs from body
        for url in extract_external_images(body):
            url_to_posts[url].append((rel, False))

        # Front matter image — flag external ones too
        fm_image = fm.get("image", "")
        if fm_image.startswith("http"):
            url_to_posts[fm_image].append((rel, True))

    # ── Check tag / category / feed pages ─────────────────────────────────────
    existing_tags  = {f.stem for f in TAGS_DIR.glob("*.md")} if TAGS_DIR.exists() else set()
    existing_cats  = {f.stem for f in CATS_DIR.glob("*.md")} if CATS_DIR.exists() else set()
    existing_feeds = {f.stem for f in FEEDS_DIR.glob("*.xml")} if FEEDS_DIR.exists() else set()

    for tag in sorted(all_tags):
        slug = slugify(tag)
        if slug not in existing_tags:
            issues["missing_tag_pages"].append({"tag": tag, "slug": slug})
            gh_error("topicos/", f"Missing tag page: topicos/{slug}.md  (tag: '{tag}')")

    for cat in sorted(all_cats):
        slug = slugify(cat)
        if slug not in existing_cats:
            issues["missing_category_pages"].append({"category": cat, "slug": slug})
            gh_error("categorias/", f"Missing category page: categorias/{slug}.md  (category: '{cat}')")
        if slug not in existing_feeds:
            issues["missing_feed_files"].append({"category": cat, "slug": slug})
            gh_warning("feed/", f"Missing feed file: feed/{slug}.xml  (category: '{cat}')")

    # ── Check external images (parallel HEAD requests) ─────────────────────────
    unique_urls = list(url_to_posts.keys())
    if unique_urls:
        print(f"\n🌐 Checking {len(unique_urls)} unique external image URL(s)...\n")
        results: dict[str, int | str] = {}

        with ThreadPoolExecutor(max_workers=IMG_MAX_WORKERS) as pool:
            future_to_url = {pool.submit(check_external_image, url): url for url in unique_urls}
            for future in as_completed(future_to_url):
                url, status = future.result()
                results[url] = status
                icon = "✅" if isinstance(status, int) and status < 400 else "❌"
                print(f"  {icon}  {status}  {url}")

        for url, status in results.items():
            posts_using = url_to_posts[url]
            is_ok = isinstance(status, int) and status < 400

            if not is_ok:
                for rel, is_fm in posts_using:
                    location = "front matter image" if is_fm else "body image"
                    issues["broken_external_images"].append({
                        "file":     rel,
                        "url":      url,
                        "status":   status,
                        "location": location,
                    })
                    severity = "error" if is_fm else "warning"
                    msg = f"Broken {location}: {url}  (HTTP {status})"
                    if severity == "error":
                        gh_error(rel, msg)
                    else:
                        gh_warning(rel, msg)

    return issues, all_tags, all_cats


# ── Report ────────────────────────────────────────────────────────────────────

def build_report(issues: dict, all_tags: set, all_cats: set) -> str:
    total_errors = (
        len(issues["missing_tag_pages"]) +
        len(issues["missing_category_pages"]) +
        len(issues["unregistered_categories"]) +
        len(issues["invalid_subcategories"]) +
        len(issues["missing_local_images"]) +
        len([i for i in issues["broken_external_images"] if i["location"] == "front matter image"]) +
        len([i for i in issues["invalid_image_extensions"] if i["field"] == "image"])
    )
    total_warnings = (
        len(issues["missing_feed_files"]) +
        len(issues["posts_without_image"]) +
        len(issues["posts_without_description"]) +
        len(issues["posts_without_reading_time"]) +
        len([i for i in issues["broken_external_images"] if i["location"] == "body image"]) +
        len([i for i in issues["invalid_image_extensions"] if i["field"] == "cover"])
    )

    post_count = len(list(POSTS_DIR.glob("*.md"))) if POSTS_DIR.exists() else 0

    lines = [
        "# Blog Structure Audit Report\n",
        "## Summary\n",
        "| | Count |",
        "|---|---|",
        f"| Posts scanned | {post_count} |",
        f"| Unique categories | {len(all_cats)} |",
        f"| Unique tags | {len(all_tags)} |",
        f"| ❌ Errors | {total_errors} |",
        f"| ⚠️ Warnings | {total_warnings} |",
        "",
    ]

    # ── Tag pages ─────────────────────────────────────────────────────────────
    lines.append("## Tag pages\n")
    if issues["missing_tag_pages"]:
        lines.append(f"**{len(issues['missing_tag_pages'])} missing:**\n")
        for item in issues["missing_tag_pages"]:
            lines.append(f"- `topicos/{item['slug']}.md` — tag: `{item['tag']}`")
        lines.append("\n<details><summary>Fix template</summary>\n\n```yaml\n---\nlayout: tag\ntag: <tag-name>\npermalink: /topicos/<slug>/\n---\n```\n</details>")
    else:
        lines.append("✅ All tag pages present.")
    lines.append("")

    # ── Category pages ────────────────────────────────────────────────────────
    lines.append("## Category pages\n")
    if issues["missing_category_pages"]:
        lines.append(f"**{len(issues['missing_category_pages'])} missing:**\n")
        for item in issues["missing_category_pages"]:
            lines.append(f"- `categorias/{item['slug']}.md` — category: `{item['category']}`")
        lines.append("\n<details><summary>Fix template</summary>\n\n```yaml\n---\nlayout: category\ncategory: <Category Name>\npermalink: /categorias/<slug>/\n---\n```\n</details>")
    else:
        lines.append("✅ All category pages present.")
    lines.append("")

    # ── Categories/subcategories registered in _data/categories.yml ──────────
    lines.append("## Categories & subcategories in _data/categories.yml\n")
    if issues["unregistered_categories"] or issues["invalid_subcategories"]:
        if issues["unregistered_categories"]:
            lines.append(f"**{len(issues['unregistered_categories'])} category use(s) not registered:**\n")
            for item in issues["unregistered_categories"]:
                lines.append(f"- `{item['file']}` — category: `{item['category']}`")
            lines.append("")
        if issues["invalid_subcategories"]:
            lines.append(f"**{len(issues['invalid_subcategories'])} invalid subcategory use(s):**\n")
            for item in issues["invalid_subcategories"]:
                lines.append(f"- `{item['file']}` — `{item['subcategory']}` — {item['reason']}")
            lines.append("")
    else:
        lines.append("✅ All categories/subcategories are registered in _data/categories.yml.")
    lines.append("")

    # ── Local image/cover files ────────────────────────────────────────────────
    lines.append("## Local image/cover files\n")
    if issues["missing_local_images"]:
        lines.append(f"**{len(issues['missing_local_images'])} missing file(s):**\n")
        for item in issues["missing_local_images"]:
            lines.append(f"- `{item['file']}` — `{item['field']}: {item['path']}` not found in branch")
    else:
        lines.append("✅ All local image/cover files exist in the branch.")
    lines.append("")

    # ── Image/cover extensions ────────────────────────────────────────────────
    lines.append("## Image/cover formats\n")
    if issues["invalid_image_extensions"]:
        lines.append(f"**{len(issues['invalid_image_extensions'])} field(s) with an unexpected format:**\n")
        for item in issues["invalid_image_extensions"]:
            icon = "❌" if item["field"] == "image" else "⚠️"
            lines.append(
                f"- {icon} `{item['file']}` — `{item['field']}: {item['path']}` "
                f"(found `{item['extension']}`, expected `{item['expected']}`)"
            )
    else:
        lines.append("✅ All `image:`/`cover:` fields use the expected format.")
    lines.append("")

    # ── Feed files ────────────────────────────────────────────────────────────
    lines.append("## Category RSS feeds\n")
    if issues["missing_feed_files"]:
        lines.append(f"**{len(issues['missing_feed_files'])} missing:**\n")
        for item in issues["missing_feed_files"]:
            lines.append(f"- `feed/{item['slug']}.xml` — category: `{item['category']}`")
    else:
        lines.append("✅ All category feeds present.")
    lines.append("")

    # ── External images ───────────────────────────────────────────────────────
    lines.append("## External images\n")
    if issues["broken_external_images"]:
        # Group by file for readability
        by_file: dict[str, list] = defaultdict(list)
        for item in issues["broken_external_images"]:
            by_file[item["file"]].append(item)

        lines.append(f"**{len(issues['broken_external_images'])} broken image(s) across {len(by_file)} post(s):**\n")
        for file, items in sorted(by_file.items()):
            lines.append(f"### `{file}`\n")
            for item in items:
                icon = "❌" if item["location"] == "front matter image" else "⚠️"
                lines.append(f"- {icon} **{item['location']}** — HTTP `{item['status']}`")
                lines.append(f"  ```")
                lines.append(f"  {item['url']}")
                lines.append(f"  ```")
    else:
        lines.append("✅ All external images reachable.")
    lines.append("")

    # ── Front matter ──────────────────────────────────────────────────────────
    lines.append("## Post front matter\n")

    for field, key in [
        ("`image:`",        "posts_without_image"),
        ("`description:`",  "posts_without_description"),
        ("`reading_time:`", "posts_without_reading_time"),
    ]:
        if issues[key]:
            lines.append(f"### Missing {field} ({len(issues[key])} posts)\n")
            for f in issues[key]:
                lines.append(f"- `{f}`")
            lines.append("")

    other = [
        i for i in issues["incomplete_front_matter"]
        if any(f not in {"image", "description", "reading_time"} for f in i["missing"])
    ]
    if other:
        lines.append(f"### Other missing fields ({len(other)} posts)\n")
        for item in other:
            fields = [f for f in item["missing"] if f not in {"image", "description", "reading_time"}]
            if fields:
                lines.append(f"- `{item['file']}` — {', '.join(f'`{f}`' for f in fields)}")
        lines.append("")

    if not any([issues["posts_without_image"], issues["posts_without_description"],
                issues["posts_without_reading_time"], other]):
        lines.append("✅ All posts have complete front matter.")

    lines += ["", "---", "_Generated by `.github/scripts/audit_blog.py`_"]
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    issues, all_tags, all_cats = audit()
    report = build_report(issues, all_tags, all_cats)

    SUMMARY_FILE.write_text(report, encoding='utf-8')

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(report)

    print("\n" + report)

    blocking = (
        len(issues["missing_tag_pages"]) +
        len(issues["missing_category_pages"]) +
        len(issues["unregistered_categories"]) +
        len(issues["invalid_subcategories"]) +
        len(issues["missing_local_images"]) +
        len([i for i in issues["broken_external_images"]
             if i["location"] == "front matter image"]) +
        len([i for i in issues["invalid_image_extensions"] if i["field"] == "image"])
    )
    sys.exit(1 if blocking > 0 else 0)


if __name__ == "__main__":
    main()
