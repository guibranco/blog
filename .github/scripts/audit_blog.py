#!/usr/bin/env python3
"""
audit_blog.py — Jekyll blog structure auditor
Checks for missing category pages, tag pages, feed files and
incomplete post front matter, then reports via GitHub annotations
and $GITHUB_STEP_SUMMARY.
"""

import os
import re
import sys
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

ROOT        = Path(__file__).resolve().parents[2]
POSTS_DIR   = ROOT / "_posts"
TAGS_DIR    = ROOT / "tags"
CATS_DIR    = ROOT / "categorias"
FEEDS_DIR   = ROOT / "feed"
SUMMARY_FILE = ROOT / "audit-report.md"

REQUIRED_FRONT_MATTER = ["layout", "title", "description", "date",
                          "categories", "tags", "reading_time", "image"]

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


def parse_front_matter(path: Path) -> dict:
    """Extract YAML front matter fields (simple key: value only)."""
    text = path.read_text(encoding='utf-8')
    fm = {}
    in_fm = False
    for i, line in enumerate(text.splitlines()):
        if i == 0 and line.strip() == '---':
            in_fm = True
            continue
        if in_fm and line.strip() == '---':
            break
        if in_fm:
            m = re.match(r'^(\w+):\s*(.*)', line)
            if m:
                fm[m.group(1)] = m.group(2).strip()
    return fm


def extract_list_field(raw: str) -> list[str]:
    """Parse a YAML inline list like `[foo, bar, baz]` or a single value."""
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        items = raw[1:-1].split(',')
        return [i.strip().strip('"').strip("'") for i in items if i.strip()]
    return [raw.strip('"').strip("'")] if raw else []


def gh_warning(file: str, message: str):
    print(f"::warning file={file}::{message}")


def gh_error(file: str, message: str):
    print(f"::error file={file}::{message}")


# ── Audit ─────────────────────────────────────────────────────────────────────

def audit() -> dict:
    issues = {
        "missing_tag_pages":      [],
        "missing_category_pages": [],
        "missing_feed_files":     [],
        "incomplete_front_matter":[],
        "posts_without_image":    [],
        "posts_without_description": [],
        "posts_without_reading_time": [],
    }

    all_tags: set[str] = set()
    all_cats: set[str] = set()

    # ── Parse all posts ───────────────────────────────────────────────────────
    posts = sorted(POSTS_DIR.glob("*.md")) if POSTS_DIR.exists() else []

    if not posts:
        print("::warning::No posts found in _posts/")
        return issues

    for post in posts:
        rel = str(post.relative_to(ROOT))
        fm  = parse_front_matter(post)

        # Collect categories and tags
        cats = extract_list_field(fm.get("categories", ""))
        tags = extract_list_field(fm.get("tags", ""))
        all_cats.update(cats)
        all_tags.update(tags)

        # Missing required front matter fields
        missing_fields = [f for f in REQUIRED_FRONT_MATTER if f not in fm]
        if missing_fields:
            issues["incomplete_front_matter"].append({
                "file": rel,
                "missing": missing_fields,
            })
            for field in missing_fields:
                gh_warning(rel, f"Missing front matter field: `{field}`")

        # Specific checks with friendlier messages
        if "image" not in fm:
            issues["posts_without_image"].append(rel)

        if "description" not in fm:
            issues["posts_without_description"].append(rel)

        if "reading_time" not in fm:
            issues["posts_without_reading_time"].append(rel)

    # ── Check tag pages ───────────────────────────────────────────────────────
    existing_tags = {f.stem for f in TAGS_DIR.glob("*.md")} if TAGS_DIR.exists() else set()

    for tag in sorted(all_tags):
        slug = slugify(tag)
        if slug not in existing_tags:
            issues["missing_tag_pages"].append({"tag": tag, "slug": slug})
            gh_error("tags/", f"Missing tag page: tags/{slug}.md  (tag: '{tag}')")

    # ── Check category pages ──────────────────────────────────────────────────
    existing_cats = {f.stem for f in CATS_DIR.glob("*.md")} if CATS_DIR.exists() else set()

    for cat in sorted(all_cats):
        slug = slugify(cat)
        if slug not in existing_cats:
            issues["missing_category_pages"].append({"category": cat, "slug": slug})
            gh_error("categorias/", f"Missing category page: categorias/{slug}.md  (category: '{cat}')")

    # ── Check feed files ──────────────────────────────────────────────────────
    existing_feeds = {f.stem for f in FEEDS_DIR.glob("*.xml")} if FEEDS_DIR.exists() else set()

    for cat in sorted(all_cats):
        slug = slugify(cat)
        if slug not in existing_feeds:
            issues["missing_feed_files"].append({"category": cat, "slug": slug})
            gh_warning("feed/", f"Missing feed file: feed/{slug}.xml  (category: '{cat}')")

    return issues, all_tags, all_cats


# ── Report ────────────────────────────────────────────────────────────────────

def build_report(issues: dict, all_tags: set, all_cats: set) -> str:
    def check(items, label):
        if items:
            return f"❌ {len(items)} {label}"
        return f"✅ {label} — all present"

    total_errors = (
        len(issues["missing_tag_pages"]) +
        len(issues["missing_category_pages"]) +
        len(issues["incomplete_front_matter"])
    )
    total_warnings = (
        len(issues["missing_feed_files"]) +
        len(issues["posts_without_image"]) +
        len(issues["posts_without_description"]) +
        len(issues["posts_without_reading_time"])
    )

    lines = [
        "# Blog Structure Audit Report\n",
        "## Summary\n",
        f"| | Count |",
        f"|---|---|",
        f"| Posts scanned | — |",
        f"| Unique categories | {len(all_cats)} |",
        f"| Unique tags | {len(all_tags)} |",
        f"| ❌ Errors | {total_errors} |",
        f"| ⚠️ Warnings | {total_warnings} |",
        "",
    ]

    # ── Missing tag pages ─────────────────────────────────────────────────────
    lines.append("## Tag pages\n")
    if issues["missing_tag_pages"]:
        lines.append(f"**{len(issues['missing_tag_pages'])} missing tag page(s):**\n")
        for item in issues["missing_tag_pages"]:
            lines.append(f"- `tags/{item['slug']}.md`  — tag: `{item['tag']}`")
        lines.append("\n**Fix:** create each missing file with:\n")
        lines.append("```yaml")
        lines.append("---")
        lines.append("layout: tag")
        lines.append("tag: <tag-name>")
        lines.append("permalink: /tags/<slug>/")
        lines.append("---")
        lines.append("```")
    else:
        lines.append("✅ All tag pages are present.")
    lines.append("")

    # ── Missing category pages ────────────────────────────────────────────────
    lines.append("## Category pages\n")
    if issues["missing_category_pages"]:
        lines.append(f"**{len(issues['missing_category_pages'])} missing category page(s):**\n")
        for item in issues["missing_category_pages"]:
            lines.append(f"- `categorias/{item['slug']}.md`  — category: `{item['category']}`")
        lines.append("\n**Fix:** create each missing file with:\n")
        lines.append("```yaml")
        lines.append("---")
        lines.append("layout: category")
        lines.append("category: <Category Name>")
        lines.append("permalink: /categorias/<slug>/")
        lines.append("---")
        lines.append("```")
    else:
        lines.append("✅ All category pages are present.")
    lines.append("")

    # ── Missing feed files ────────────────────────────────────────────────────
    lines.append("## Category RSS feeds\n")
    if issues["missing_feed_files"]:
        lines.append(f"**{len(issues['missing_feed_files'])} missing feed file(s):**\n")
        for item in issues["missing_feed_files"]:
            lines.append(f"- `feed/{item['slug']}.xml`  — category: `{item['category']}`")
    else:
        lines.append("✅ All category feeds are present.")
    lines.append("")

    # ── Incomplete front matter ───────────────────────────────────────────────
    lines.append("## Post front matter\n")

    if issues["posts_without_image"]:
        lines.append(f"### Missing `image:` ({len(issues['posts_without_image'])} posts)\n")
        for f in issues["posts_without_image"]:
            lines.append(f"- `{f}`")
        lines.append("")

    if issues["posts_without_description"]:
        lines.append(f"### Missing `description:` ({len(issues['posts_without_description'])} posts)\n")
        for f in issues["posts_without_description"]:
            lines.append(f"- `{f}`")
        lines.append("")

    if issues["posts_without_reading_time"]:
        lines.append(f"### Missing `reading_time:` ({len(issues['posts_without_reading_time'])} posts)\n")
        for f in issues["posts_without_reading_time"]:
            lines.append(f"- `{f}`")
        lines.append("")

    other_incomplete = [
        i for i in issues["incomplete_front_matter"]
        if any(f not in ["image", "description", "reading_time"] for f in i["missing"])
    ]
    if other_incomplete:
        lines.append(f"### Other missing fields ({len(other_incomplete)} posts)\n")
        for item in other_incomplete:
            other = [f for f in item["missing"] if f not in ["image", "description", "reading_time"]]
            if other:
                lines.append(f"- `{item['file']}` — missing: {', '.join(f'`{f}`' for f in other)}")
        lines.append("")

    if not any([issues["posts_without_image"], issues["posts_without_description"],
                issues["posts_without_reading_time"], other_incomplete]):
        lines.append("✅ All posts have complete front matter.")

    lines.append("")
    lines.append("---")
    lines.append("_Generated by `.github/scripts/audit_blog.py`_")

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    issues, all_tags, all_cats = audit()

    report = build_report(issues, all_tags, all_cats)

    # Write artifact
    SUMMARY_FILE.write_text(report, encoding='utf-8')

    # Write to GitHub Step Summary
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(report)

    print(report)

    # Exit with error if blocking issues exist
    blocking = (
        len(issues["missing_tag_pages"]) +
        len(issues["missing_category_pages"])
    )
    sys.exit(1 if blocking > 0 else 0)


if __name__ == "__main__":
    main()
