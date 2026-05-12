#!/usr/bin/env python3
"""
create_missing_pages.py — auto-creates missing category pages, tag pages,
and category RSS feed files.

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

# ── Config ────────────────────────────────────────────────────────────────────

ROOT       = Path(__file__).resolve().parents[2]
CATS_DIR   = ROOT / "categorias"
TAGS_DIR   = ROOT / "topicos"
FEEDS_DIR  = ROOT / "feed"

CATEGORY_LAYOUT    = "category"
TAG_LAYOUT         = "tag"
CATEGORY_PERMALINK = "/categorias/{slug}/"
TAG_PERMALINK      = "/topicos/{slug}/"
FEED_PERMALINK     = "/feed/{slug}.xml"

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Latin slugify matching Jekyll's `slugify: 'latin'` filter."""
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
    """Return a dict of front matter key/value pairs."""
    fm = {}
    in_fm = False
    for i, line in enumerate(path.read_text(encoding='utf-8').splitlines()):
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


def extract_list(raw: str) -> list[str]:
    """Parse `[foo, bar]` or a bare value into a list."""
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        return [i.strip().strip('"').strip("'") for i in raw[1:-1].split(',') if i.strip()]
    return [raw.strip('"').strip("'")] if raw else []


def feed_template(original: str, slug: str) -> str:
    """Generate a Jekyll Liquid RSS feed file for a category."""
    return (
        "---\n"
        "layout: null\n"
        f"permalink: {FEED_PERMALINK.format(slug=slug)}\n"
        "---\n"
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        f'    <title>{{{{ site.title }}}} — {original}</title>\n'
        f'    <description>Artigos sobre {original} em {{{{ site.title }}}}</description>\n'
        f'    <link>{{{{ site.url }}}}{{{{ site.baseurl }}}}/categorias/{slug}/</link>\n'
        f'    <atom:link href="{{{{ site.url }}}}{{{{ site.baseurl }}}}/feed/{slug}.xml"'
        ' rel="self" type="application/rss+xml"/>\n'
        "    <language>pt-BR</language>\n"
        "    {{% assign cat_posts = site.posts"
        f' | where_exp: "p", "p.categories contains \'{original}\'"'
        " | limit: 20 %}\n"
        "    {{% for post in cat_posts %}}\n"
        "    <item>\n"
        "      <title>{{{{ post.title | xml_escape }}}}</title>\n"
        "      <link>{{{{ post.url | absolute_url }}}}</link>\n"
        '      <guid isPermaLink="true">{{{{ post.url | absolute_url }}}}</guid>\n'
        "      <pubDate>{{{{ post.date | date_to_rfc822 }}}}</pubDate>\n"
        "      <description>{{{{ post.description | xml_escape }}}}</description>\n"
        "    </item>\n"
        "    {{% endfor %}}\n"
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

def collect_missing(post_files: list[str]) -> tuple[dict, dict]:
    """
    Return two dicts of items that need pages created:
        missing_cats: {slug: original_name}
        missing_tags: {slug: original_name}
    Feed files are checked per category in create_pages() since they always
    accompany a new category page.
    """
    for d in (CATS_DIR, TAGS_DIR, FEEDS_DIR):
        d.mkdir(parents=True, exist_ok=True)

    existing_cats = {f.stem for f in CATS_DIR.glob("*.md")}
    existing_tags = {f.stem for f in TAGS_DIR.glob("*.md")}

    missing_cats: dict[str, str] = {}
    missing_tags: dict[str, str] = {}

    for post_file in post_files:
        path = Path(post_file)
        if not path.is_absolute():
            path = ROOT / path
        if not path.exists():
            print(f"⚠ File not found, skipping: {path}")
            continue

        fm = parse_front_matter(path)
        cats = extract_list(fm.get('categories', ''))
        tags = extract_list(fm.get('tags', ''))

        print(f"\n📄 {path.name}")
        print(f"   categories: {cats}")
        print(f"   tags:       {tags}")

        for cat in cats:
            if not cat:
                continue
            slug = slugify(cat)
            if slug not in existing_cats and slug not in missing_cats:
                missing_cats[slug] = cat

        for tag in tags:
            if not tag:
                continue
            slug = slugify(tag)
            if slug not in existing_tags and slug not in missing_tags:
                missing_tags[slug] = tag

    return missing_cats, missing_tags


def create_pages(
    missing_cats: dict[str, str],
    missing_tags: dict[str, str],
) -> tuple[list, list, list]:
    """
    Create missing category pages, tag pages, and category feed files.
    Returns (created_cats, created_tags, created_feeds).
    Each item is a (original_name, slug) tuple.
    """
    existing_feeds = {f.stem for f in FEEDS_DIR.glob("*.xml")}

    created_cats:  list[tuple[str, str]] = []
    created_tags:  list[tuple[str, str]] = []
    created_feeds: list[tuple[str, str]] = []

    for slug, original in sorted(missing_cats.items()):
        # Category page
        cat_path = CATS_DIR / f"{slug}.md"
        cat_path.write_text(
            f"---\n"
            f"layout: {CATEGORY_LAYOUT}\n"
            f"category: {original}\n"
            f"permalink: {CATEGORY_PERMALINK.format(slug=slug)}\n"
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
            created_feeds.append((original, slug))
            print(f"✅ Created: feed/{slug}.xml  (category: {original})")

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

    return created_cats, created_tags, created_feeds


def build_pr_comment(
    created_cats:  list[tuple[str, str]],
    created_tags:  list[tuple[str, str]],
    created_feeds: list[tuple[str, str]],
    post_files:    list[str],
) -> str:
    total = len(created_cats) + len(created_tags) + len(created_feeds)
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

    if created_feeds:
        lines.append(f"### 📡 RSS feeds ({len(created_feeds)})\n")
        for original, slug in created_feeds:
            lines.append(
                f"- `feed/{slug}.xml` → **{original}** "
                f"(`/feed/{slug}.xml`)"
            )
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

    missing_cats, missing_tags = collect_missing(post_files)

    total_missing = len(missing_cats) + len(missing_tags)
    if total_missing == 0:
        print("\n✅ All category and tag pages already exist — nothing to create.")
        write_output('created_count', '0')
        write_output('pr_comment', '')
        return

    print(f"\n📝 Creating missing pages...")
    created_cats, created_tags, created_feeds = create_pages(missing_cats, missing_tags)

    total_created = len(created_cats) + len(created_tags) + len(created_feeds)
    comment = build_pr_comment(created_cats, created_tags, created_feeds, post_files)

    write_output('created_count', str(total_created))
    write_output('pr_comment', comment)

    print(f"\n🎉 Done — {total_created} file(s) created.")


if __name__ == '__main__':
    main()
