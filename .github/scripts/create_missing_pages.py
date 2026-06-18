#!/usr/bin/env python3
"""
create_missing_pages.py — auto-creates missing category pages, tag pages,
subcategory pages, and RSS feed files.

Called by the GitHub Actions workflow with a list of post file paths:
    python3 create_missing_pages.py _posts/2026-05-11-my-post.md ...

Outputs to $GITHUB_OUTPUT:
    created_count   — total number of files created
    pr_comment      — formatted markdown comment for the PR
"""

import os
import re
import sys
from pathlib import Path
try:
    import yaml as _yaml
    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False

# ── Config ────────────────────────────────────────────────────────────────────

ROOT       = Path(__file__).resolve().parents[2]
CATS_DIR   = ROOT / "categorias"
TAGS_DIR   = ROOT / "topicos"
FEEDS_DIR  = ROOT / "feed"

CATEGORY_LAYOUT       = "category"
TAG_LAYOUT            = "tag"
CATEGORY_PERMALINK    = "/categorias/{slug}/"
SUBCATEGORY_PERMALINK = "/categorias/{cat_slug}/{sub_slug}/"
TAG_PERMALINK         = "/topicos/{slug}/"
FEED_PERMALINK        = "/feed/{slug}.xml"
SUBFEED_PERMALINK     = "/feed/{cat_slug}-{sub_slug}.xml"

# Manual slug overrides for names that produce bad automatic slugs.
# Key: lowercased original name; Value: desired slug.
SLUG_OVERRIDES: dict[str, str] = {
    "c#":               "csharp",
    "c++":              "cpp",
    "js/ts & node.js":  "js-ts-node-js",
    "js/ts":            "js-ts",
    "tips & tricks":    "tips-tricks",
    "travel & places":  "travel-places",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Latin slugify matching Jekyll's `slugify: 'latin'` filter.

    Checks SLUG_OVERRIDES first so special names (C#, JS/TS…) always produce
    the same slug as the manually created page files.
    """
    key = text.strip().lower()
    if key in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[key]

    replacements = {
        'ã': 'a', 'â': 'a', 'á': 'a', 'à': 'a',
        'ê': 'e', 'é': 'e', 'è': 'e',
        'í': 'i', 'ì': 'i',
        'ô': 'o', 'õ': 'o', 'ó': 'o',
        'ú': 'u', 'ü': 'u',
        'ç': 'c',
    }
    s = key
    for src, dst in replacements.items():
        s = s.replace(src, dst)
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s.strip())
    return re.sub(r'-+', '-', s).strip('-')


def parse_front_matter(path: Path) -> dict:
    """Return a dict of front matter values.

    Uses PyYAML when available (handles multi-line arrays, nested structures).
    Falls back to a simple regex parser for single-line scalar values only.
    """
    text = path.read_text(encoding='utf-8')
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}
    raw = parts[1]

    if _HAS_YAML:
        try:
            return _yaml.safe_load(raw) or {}
        except _yaml.YAMLError:
            pass  # fall through to regex parser

    # Fallback: regex parser (scalar values only)
    fm: dict = {}
    for line in raw.splitlines():
        m = re.match(r'^(\w+):\s*(.*)', line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def extract_list(raw) -> list[str]:
    """Parse a value into a list of strings.
    Accepts: Python list (from yaml), inline '[a, b]' string, or bare string.
    """
    if isinstance(raw, list):
        return [str(i).strip() for i in raw if i is not None]
    if not raw:
        return []
    raw = str(raw).strip()
    if raw.startswith('[') and raw.endswith(']'):
        return [i.strip().strip('"').strip("'") for i in raw[1:-1].split(',') if i.strip()]
    return [raw.strip('"').strip("'")] if raw else []


def extract_subcat_pairs(fm: dict) -> list[tuple[str, str]]:
    """Return (parent_category, subcategory) pairs from a post's front matter.

    Supports two formats:
      • subcategory: "DevOps"            — paired with every parent in categories[]
      • subcategories:                   — explicit pairs; each item must be "Parent/Child"
          - "Coding/DevOps"
          - "Testing/Automation"

    Both fields may coexist; duplicates are removed.
    """
    categories = extract_list(fm.get('categories', []))
    pairs: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def _add(parent: str, child: str) -> None:
        parent, child = parent.strip(), child.strip()
        if parent and child and (parent, child) not in seen:
            pairs.append((parent, child))
            seen.add((parent, child))

    # New format: subcategories: ["Parent/Child", ...]
    for item in extract_list(fm.get('subcategories', [])):
        if '/' in item:
            parent, child = item.split('/', 1)
            _add(parent, child)
        # bare name without parent — skip; ambiguous

    # Old format: subcategory: "Name" — pair with every parent category
    sub = fm.get('subcategory', '')
    if isinstance(sub, str):
        sub = sub.strip().strip('"').strip("'")
    else:
        sub = str(sub).strip() if sub else ''
    if sub:
        for cat in categories:
            _add(cat, sub)

    return pairs


def _xml_escape(text: str) -> str:
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def feed_template(original: str, slug: str) -> str:
    """Generate a Jekyll Liquid RSS feed file for a top-level category."""
    safe = _xml_escape(original)
    return (
        "---\n"
        "layout: null\n"
        f"permalink: {FEED_PERMALINK.format(slug=slug)}\n"
        "---\n"
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        f'    <title>{{{{ site.title | xml_escape }}}} — {safe}</title>\n'
        f'    <description>Artigos sobre {safe} em {{{{ site.title | xml_escape }}}}</description>\n'
        f'    <link>{{{{ site.url }}}}{{{{ site.baseurl }}}}/categorias/{slug}/</link>\n'
        f'    <atom:link href="{{{{ site.url }}}}{{{{ site.baseurl }}}}/feed/{slug}.xml"'
        ' rel="self" type="application/rss+xml"/>\n'
        "    <language>pt-BR</language>\n"
        f'    {{% assign _cat_posts = site.posts | where_exp: "p",'
        f' "p.categories contains \'{original}\'" | limit: 20 %}}\n'
        "    {% for post in _cat_posts %}\n"
        "    <item>\n"
        "      <title>{{ post.title | xml_escape }}</title>\n"
        "      <link>{{ post.url | absolute_url }}</link>\n"
        '      <guid isPermaLink="true">{{ post.url | absolute_url }}</guid>\n'
        "      <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>\n"
        "      <description>{{ post.description | xml_escape }}</description>\n"
        "    </item>\n"
        "    {% endfor %}\n"
        "  </channel>\n"
        "</rss>\n"
    )


def subcategory_feed_template(
    cat_original: str, cat_slug: str,
    sub_original: str, sub_slug: str,
) -> str:
    """Generate a Jekyll Liquid RSS feed for a subcategory."""
    safe_cat = _xml_escape(cat_original)
    safe_sub = _xml_escape(sub_original)
    feed_slug = f"{cat_slug}-{sub_slug}"
    filter_cond = f"p.subcategories contains '{cat_original}/{sub_original}'"
    return (
        "---\n"
        "layout: null\n"
        f"permalink: {SUBFEED_PERMALINK.format(cat_slug=cat_slug, sub_slug=sub_slug)}\n"
        "---\n"
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        f'    <title>{{{{ site.title | xml_escape }}}} — {safe_cat} › {safe_sub}</title>\n'
        f'    <description>Artigos sobre {safe_sub} em {{{{ site.title | xml_escape }}}}</description>\n'
        f'    <link>{{{{ site.url }}}}{{{{ site.baseurl }}}}/categorias/{cat_slug}/{sub_slug}/</link>\n'
        f'    <atom:link href="{{{{ site.url }}}}{{{{ site.baseurl }}}}/feed/{feed_slug}.xml"'
        ' rel="self" type="application/rss+xml"/>\n'
        "    <language>pt-BR</language>\n"
        f'    {{% assign _sub_posts = site.posts | where_exp: "p", "{filter_cond}" | limit: 20 %}}\n'
        "    {% for post in _sub_posts %}\n"
        "    <item>\n"
        "      <title>{{ post.title | xml_escape }}</title>\n"
        "      <link>{{ post.url | absolute_url }}</link>\n"
        '      <guid isPermaLink="true">{{ post.url | absolute_url }}</guid>\n'
        "      <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>\n"
        "      <description>{{ post.description | xml_escape }}</description>\n"
        "    </item>\n"
        "    {% endfor %}\n"
        "  </channel>\n"
        "</rss>\n"
    )


def write_output(key: str, value: str) -> None:
    github_output = os.environ.get('GITHUB_OUTPUT')
    if github_output:
        if '\n' in value:
            delimiter = 'EOF_' + key.upper()
            with open(github_output, 'a') as f:
                f.write(f"{key}<<{delimiter}\n{value}\n{delimiter}\n")
        else:
            with open(github_output, 'a') as f:
                f.write(f"{key}={value}\n")
    else:
        print(f"[OUTPUT] {key}={value[:120]}{'...' if len(value) > 120 else ''}")


# ── Core logic ────────────────────────────────────────────────────────────────

def collect_missing(post_files: list[str]) -> tuple[dict, dict, dict]:
    """
    Return three dicts of items that need pages created:
        missing_cats:    {slug: original_name}
        missing_tags:    {slug: original_name}
        missing_subcats: {(cat_slug, sub_slug): (cat_original, sub_original)}
    """
    for d in (CATS_DIR, TAGS_DIR, FEEDS_DIR):
        d.mkdir(parents=True, exist_ok=True)

    existing_cats = {f.stem for f in CATS_DIR.glob("*.md")}
    existing_tags = {f.stem for f in TAGS_DIR.glob("*.md")}

    # Subcategory pages live in categorias/{cat_slug}/{sub_slug}.md
    existing_subcats: set[tuple[str, str]] = set()
    for cat_dir in CATS_DIR.iterdir():
        if cat_dir.is_dir():
            for f in cat_dir.glob("*.md"):
                existing_subcats.add((cat_dir.name, f.stem))

    missing_cats:    dict[str, str]                         = {}
    missing_tags:    dict[str, str]                         = {}
    missing_subcats: dict[tuple[str, str], tuple[str, str]] = {}

    for post_file in post_files:
        path = Path(post_file)
        if not path.is_absolute():
            path = ROOT / path
        if not path.exists():
            print(f"⚠ File not found, skipping: {path}")
            continue

        fm    = parse_front_matter(path)
        cats  = extract_list(fm.get('categories', []))
        tags  = extract_list(fm.get('tags', []))
        pairs = extract_subcat_pairs(fm)

        print(f"\n📄 {path.name}")
        print(f"   categories:    {cats}")
        print(f"   subcategories: {pairs or '(none)'}")
        print(f"   tags:          {tags}")

        for cat in cats:
            if not cat:
                continue
            slug = slugify(cat)
            if slug not in existing_cats and slug not in missing_cats:
                missing_cats[slug] = cat

        for cat_original, sub_original in pairs:
            cat_slug = slugify(cat_original)
            sub_slug = slugify(sub_original)
            key = (cat_slug, sub_slug)
            if key not in existing_subcats and key not in missing_subcats:
                missing_subcats[key] = (cat_original, sub_original)

        for tag in tags:
            if not tag:
                continue
            slug = slugify(tag)
            if slug not in existing_tags and slug not in missing_tags:
                missing_tags[slug] = tag

    return missing_cats, missing_tags, missing_subcats


def create_pages(
    missing_cats:    dict[str, str],
    missing_tags:    dict[str, str],
    missing_subcats: dict[tuple[str, str], tuple[str, str]],
) -> tuple[list, list, list, list]:
    """
    Create missing category pages, subcategory pages, tag pages, and RSS feeds.
    Returns (created_cats, created_subcats, created_tags, created_feeds).
    """
    existing_feeds = {f.stem for f in FEEDS_DIR.glob("*.xml")}

    created_cats:    list[tuple[str, str]]           = []
    created_subcats: list[tuple[str, str, str, str]] = []
    created_tags:    list[tuple[str, str]]           = []
    created_feeds:   list[tuple[str, str, str]]      = []  # (label, slug, path)

    for slug, original in sorted(missing_cats.items()):
        # Category page
        cat_path = CATS_DIR / f"{slug}.md"
        cat_path.write_text(
            f"---\n"
            f"layout: {CATEGORY_LAYOUT}\n"
            f"category: {original}\n"
            f"permalink: {CATEGORY_PERMALINK.format(slug=slug)}\n"
            f"pagination:\n"
            f"  enabled: true\n"
            f"  per_page: 10\n"
            f"  sort_field: date\n"
            f"  sort_reverse: true\n"
            f"  category: {original}\n"
            f"---\n",
            encoding='utf-8',
        )
        created_cats.append((original, slug))
        print(f"✅ Created: categorias/{slug}.md  (category: {original})")

        # RSS feed for this category
        if slug not in existing_feeds:
            feed_path = FEEDS_DIR / f"{slug}.xml"
            feed_path.write_text(feed_template(original, slug), encoding='utf-8')
            existing_feeds.add(slug)
            created_feeds.append((original, slug, f"feed/{slug}.xml"))
            print(f"✅ Created: feed/{slug}.xml  (category: {original})")

    for (cat_slug, sub_slug), (cat_original, sub_original) in sorted(missing_subcats.items()):
        # Ensure parent directory exists
        subcat_dir = CATS_DIR / cat_slug
        subcat_dir.mkdir(exist_ok=True)

        sub_path = subcat_dir / f"{sub_slug}.md"
        permalink = SUBCATEGORY_PERMALINK.format(cat_slug=cat_slug, sub_slug=sub_slug)
        pair_str  = f"{cat_original}/{sub_original}"
        wc = f":subcategories contains '{pair_str}'"
        sub_path.write_text(
            f"---\n"
            f"layout: {CATEGORY_LAYOUT}\n"
            f"category: {cat_original}\n"
            f"subcategory: {sub_original}\n"
            f"permalink: {permalink}\n"
            f"pagination:\n"
            f"  enabled: true\n"
            f"  per_page: 10\n"
            f"  sort_field: date\n"
            f"  sort_reverse: true\n"
            f"  where_condition: \"{wc}\"\n"
            f"---\n",
            encoding='utf-8',
        )
        created_subcats.append((cat_original, cat_slug, sub_original, sub_slug))
        print(f"✅ Created: categorias/{cat_slug}/{sub_slug}.md  ({cat_original} › {sub_original})")

        # RSS feed for this subcategory
        feed_stem = f"{cat_slug}-{sub_slug}"
        if feed_stem not in existing_feeds:
            feed_path = FEEDS_DIR / f"{feed_stem}.xml"
            feed_path.write_text(
                subcategory_feed_template(cat_original, cat_slug, sub_original, sub_slug),
                encoding='utf-8',
            )
            existing_feeds.add(feed_stem)
            created_feeds.append((f"{cat_original} › {sub_original}", feed_stem, f"feed/{feed_stem}.xml"))
            print(f"✅ Created: feed/{feed_stem}.xml  ({cat_original} › {sub_original})")

    for slug, original in sorted(missing_tags.items()):
        tag_path = TAGS_DIR / f"{slug}.md"
        tag_path.write_text(
            f"---\n"
            f"layout: {TAG_LAYOUT}\n"
            f"tag: {original}\n"
            f"permalink: {TAG_PERMALINK.format(slug=slug)}\n"
            f"---\n",
            encoding='utf-8',
        )
        created_tags.append((original, slug))
        print(f"✅ Created: topicos/{slug}.md  (tag: {original})")

    return created_cats, created_subcats, created_tags, created_feeds


def build_pr_comment(
    created_cats:    list[tuple[str, str]],
    created_subcats: list[tuple[str, str, str, str]],
    created_tags:    list[tuple[str, str]],
    created_feeds:   list[tuple[str, str, str]],
    post_files:      list[str],
) -> str:
    total = len(created_cats) + len(created_subcats) + len(created_tags) + len(created_feeds)
    posts_list = '\n'.join(f"- `{f}`" for f in post_files)

    lines = [
        "## 🤖 Auto-created pages\n",
        f"The following **{total} file(s)** were automatically created and committed "
        f"to this branch based on the modified post(s):\n",
        f"<details><summary>Modified posts ({len(post_files)})</summary>\n\n"
        f"{posts_list}\n\n</details>\n",
    ]

    if created_cats:
        lines.append(f"### 📁 Categories ({len(created_cats)})\n")
        for original, slug in created_cats:
            lines.append(
                f"- `categorias/{slug}.md` → **{original}** "
                f"(`/categorias/{slug}/`)"
            )
        lines.append("")

    if created_subcats:
        lines.append(f"### 📂 Subcategories ({len(created_subcats)})\n")
        for cat_original, cat_slug, sub_original, sub_slug in created_subcats:
            lines.append(
                f"- `categorias/{cat_slug}/{sub_slug}.md` → **{cat_original} › {sub_original}** "
                f"(`/categorias/{cat_slug}/{sub_slug}/`)"
            )
        lines.append("")

    if created_feeds:
        lines.append(f"### 📡 RSS feeds ({len(created_feeds)})\n")
        for label, slug, path in created_feeds:
            lines.append(f"- `{path}` → **{label}** (`/{path}`)")
        lines.append("")

    if created_tags:
        lines.append(f"### 🏷️ Tópicos ({len(created_tags)})\n")
        for original, slug in created_tags:
            lines.append(
                f"- `topicos/{slug}.md` → `#{original}` "
                f"(`/topicos/{slug}/`)"
            )
        lines.append("")

    lines += [
        "---",
        "> _Committed by `github-actions[bot]` · "
        "workflow: `auto-create-pages.yml`_",
    ]

    return '\n'.join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    post_files = [f for f in sys.argv[1:] if f.strip()]

    if not post_files:
        print("No post files provided — nothing to do.")
        write_output('created_count', '0')
        write_output('pr_comment', '')
        return

    print(f"\n🔍 Scanning {len(post_files)} post file(s) for missing pages...\n")

    missing_cats, missing_tags, missing_subcats = collect_missing(post_files)

    total_missing = len(missing_cats) + len(missing_tags) + len(missing_subcats)
    if total_missing == 0:
        print("\n✅ All category, subcategory and tag pages already exist — nothing to create.")
        write_output('created_count', '0')
        write_output('pr_comment', '')
        return

    print(f"\n📝 Creating missing pages...")
    created_cats, created_subcats, created_tags, created_feeds = create_pages(
        missing_cats, missing_tags, missing_subcats
    )

    total_created = len(created_cats) + len(created_subcats) + len(created_tags) + len(created_feeds)
    comment = build_pr_comment(created_cats, created_subcats, created_tags, created_feeds, post_files)

    write_output('created_count', str(total_created))
    write_output('pr_comment', comment)

    print(f"\n🎉 Done — {total_created} file(s) created.")


if __name__ == '__main__':
    main()
