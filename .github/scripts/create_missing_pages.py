#!/usr/bin/env python3
"""
create_missing_pages.py — keeps _data/categories.yml and _data/tags.yml in
sync with what posts actually use.

Category, Subcategory, Tag, and RSS feed *pages* are no longer physical
files. _plugins/category_pages_generator.rb, _plugins/tag_pages_generator.rb,
and _plugins/feed_generator.rb generate all of them at build time straight
from these two data files (see docs/adr/0001, 0003, and 0004). This script's
only job is to add entries these generators haven't seen yet — a category,
subcategory, or tag "exists" the moment it's registered in the data file;
there's nothing else to create.

Called by the GitHub Actions workflow with a list of post file paths:
    python3 create_missing_pages.py _posts/2026-05-11-my-post.md ...

Outputs to $GITHUB_OUTPUT:
    created_count   — total number of entries added
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
CATEGORIES_DATA_FILE = ROOT / "_data" / "categories.yml"
TAGS_DATA_FILE = ROOT / "_data" / "tags.yml"

# Icon assigned to auto-created top-level categories in _data/categories.yml.
# Automation can't guess a meaningful icon, so this is a placeholder meant
# to be reviewed and replaced by hand.
DEFAULT_CATEGORY_ICON = "fas fa-folder"

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


def _yaml_unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ('"', "'"):
        return s[1:-1].replace('\\"', '"').replace('\\\\', '\\')
    return s


def _yaml_scalar(value: str) -> str:
    """Render a YAML scalar, quoting it only when needed (matches the
    existing style in _data/categories.yml: single-word names are bare,
    names containing a space or symbols are double-quoted)."""
    if re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9\-]*', value):
        return value
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def parse_categories_yaml(text: str) -> list[dict]:
    """Parse `_data/categories.yml` into an ordered list of category dicts:
    [{"name", "slug", "icon", "redirect_from": [...] (optional),
      "subcategories": [{"name", "slug", "redirect_from": [...] (optional)}, ...]}, ...]

    A minimal hand-rolled parser is used (instead of PyYAML) so the
    round-tripped file keeps its exact original formatting/quoting style.
    """
    categories: list[dict] = []
    current: dict | None = None
    pending_sub: dict | None = None
    in_subs = False
    in_cat_redirects = False
    in_sub_redirects = False

    for raw_line in text.splitlines():
        if not raw_line.strip():
            continue
        indent = len(raw_line) - len(raw_line.lstrip(' '))
        line = raw_line.strip()

        m = re.match(r'^-\s*name:\s*(.+)$', line)
        if m and indent == 0:
            current = {"name": _yaml_unquote(m.group(1)), "slug": "",
                       "icon": "", "subcategories": []}
            categories.append(current)
            in_subs = False
            in_cat_redirects = False
            in_sub_redirects = False
            pending_sub = None
            continue

        if current is None:
            continue

        if indent == 2 and line.startswith('slug:'):
            current["slug"] = _yaml_unquote(line.split(':', 1)[1])
            in_subs = False
            in_cat_redirects = False
            continue
        if indent == 2 and line.startswith('icon:'):
            current["icon"] = _yaml_unquote(line.split(':', 1)[1])
            in_cat_redirects = False
            continue
        if indent == 2 and line.startswith('redirect_from:'):
            in_cat_redirects = True
            in_subs = False
            current["redirect_from"] = []
            continue
        if indent == 2 and line.startswith('subcategories:'):
            in_subs = True
            in_cat_redirects = False
            continue
        if in_cat_redirects and indent == 4 and line.startswith('-'):
            current["redirect_from"].append(_yaml_unquote(line[1:].strip()))
            continue

        if in_subs:
            m2 = re.match(r'^-\s*name:\s*(.+)$', line)
            if m2 and indent == 4:
                pending_sub = {"name": _yaml_unquote(m2.group(1)), "slug": ""}
                current["subcategories"].append(pending_sub)
                in_sub_redirects = False
                continue
            if indent == 6 and line.startswith('slug:') and pending_sub is not None:
                pending_sub["slug"] = _yaml_unquote(line.split(':', 1)[1])
                in_sub_redirects = False
                continue
            if indent == 6 and line.startswith('redirect_from:') and pending_sub is not None:
                in_sub_redirects = True
                pending_sub["redirect_from"] = []
                continue
            if in_sub_redirects and indent == 8 and line.startswith('-') and pending_sub is not None:
                pending_sub["redirect_from"].append(_yaml_unquote(line[1:].strip()))
                continue

    return categories


def serialize_categories_yaml(categories: list[dict]) -> str:
    """Render category dicts back into the file's original layout."""
    blocks = []
    for cat in categories:
        lines = [
            f"- name: {_yaml_scalar(cat['name'])}",
            f"  slug: {cat['slug']}",
            f"  icon: \"{cat['icon']}\"",
        ]
        cat_redirects = cat.get("redirect_from") or []
        if cat_redirects:
            lines.append("  redirect_from:")
            for r in cat_redirects:
                lines.append(f"    - {r}")
        subs = cat.get("subcategories") or []
        if subs:
            lines.append("  subcategories:")
            for sub in subs:
                lines.append(f"    - name: {_yaml_scalar(sub['name'])}")
                lines.append(f"      slug: {sub['slug']}")
                sub_redirects = sub.get("redirect_from") or []
                if sub_redirects:
                    lines.append("      redirect_from:")
                    for r in sub_redirects:
                        lines.append(f"        - {r}")
        else:
            lines.append("  subcategories: []")
        blocks.append("\n".join(lines))
    return "\n".join(blocks) + "\n"


def sync_categories_data(
    missing_cats:    dict[str, str],
    missing_subcats: dict[tuple[str, str], tuple[str, str]],
) -> tuple[list[tuple[str, str]], list[tuple[str, str, str, str]]]:
    """
    Add newly used categories/subcategories to _data/categories.yml — the
    single source of truth _plugins/category_pages_generator.rb and
    _plugins/feed_generator.rb read at build time.

    Returns (added_categories, added_subcategories) as
    [(name, slug)] / [(cat_name, cat_slug, sub_name, sub_slug)] for reporting.
    """
    text = CATEGORIES_DATA_FILE.read_text(encoding='utf-8') if CATEGORIES_DATA_FILE.exists() else ""
    categories = parse_categories_yaml(text)
    by_slug = {cat["slug"]: cat for cat in categories}

    added_cats: list[tuple[str, str]] = []
    added_subs: list[tuple[str, str, str, str]] = []

    def _ensure_category(slug: str, original: str) -> dict:
        cat = by_slug.get(slug)
        if cat is None:
            cat = {"name": original, "slug": slug, "icon": DEFAULT_CATEGORY_ICON, "subcategories": []}
            categories.append(cat)
            by_slug[slug] = cat
            added_cats.append((original, slug))
            print(
                f"✅ Added to _data/categories.yml: category '{original}' "
                f"(icon defaulted to '{DEFAULT_CATEGORY_ICON}' — please review)"
            )
        return cat

    for slug, original in sorted(missing_cats.items()):
        _ensure_category(slug, original)

    for (cat_slug, sub_slug), (cat_original, sub_original) in sorted(missing_subcats.items()):
        cat = _ensure_category(cat_slug, cat_original)
        existing_sub_slugs = {s["slug"] for s in cat["subcategories"]}
        if sub_slug not in existing_sub_slugs:
            cat["subcategories"].append({"name": sub_original, "slug": sub_slug})
            added_subs.append((cat_original, cat_slug, sub_original, sub_slug))
            print(f"✅ Added to _data/categories.yml: subcategory '{sub_original}' under '{cat_original}'")

    if added_cats or added_subs:
        CATEGORIES_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        CATEGORIES_DATA_FILE.write_text(serialize_categories_yaml(categories), encoding='utf-8')

    return added_cats, added_subs


def parse_tags_yaml(text: str) -> list[dict]:
    """Parse `_data/tags.yml` into an ordered list of tag dicts:
    [{"name", "slug", "redirect_from": [...] (optional)}, ...]

    A minimal hand-rolled parser is used (instead of PyYAML) so the
    round-tripped file keeps its exact original formatting/quoting style,
    matching parse_categories_yaml.
    """
    tags: list[dict] = []
    current: dict | None = None
    in_redirects = False

    for raw_line in text.splitlines():
        if not raw_line.strip():
            continue
        indent = len(raw_line) - len(raw_line.lstrip(' '))
        line = raw_line.strip()

        m = re.match(r'^-\s*name:\s*(.+)$', line)
        if m and indent == 0:
            current = {"name": _yaml_unquote(m.group(1)), "slug": ""}
            tags.append(current)
            in_redirects = False
            continue

        if current is None:
            continue

        if indent == 2 and line.startswith('slug:'):
            current["slug"] = _yaml_unquote(line.split(':', 1)[1])
            in_redirects = False
            continue
        if indent == 2 and line.startswith('redirect_from:'):
            in_redirects = True
            current["redirect_from"] = []
            continue
        if in_redirects and indent == 4 and line.startswith('-'):
            current["redirect_from"].append(_yaml_unquote(line[1:].strip()))
            continue

    return tags


def serialize_tags_yaml(tags: list[dict]) -> str:
    """Render tag dicts back into `_data/tags.yml`'s layout."""
    blocks = []
    for tag in tags:
        lines = [
            f"- name: {_yaml_scalar(tag['name'])}",
            f"  slug: {tag['slug']}",
        ]
        redirects = tag.get("redirect_from") or []
        if redirects:
            lines.append("  redirect_from:")
            for r in redirects:
                lines.append(f"    - {r}")
        blocks.append("\n".join(lines))
    return "\n".join(blocks) + "\n"


def sync_tags_data(missing_tags: dict[str, str]) -> list[tuple[str, str]]:
    """
    Add newly used tags to _data/tags.yml, the source of truth that
    _plugins/tag_pages_generator.rb reads at build time to create each
    /topicos/{slug}/ page (see docs/adr/0003-tag-pages-generated-from-data-file.md).

    Returns added tags as [(name, slug)] for reporting.
    """
    text = TAGS_DATA_FILE.read_text(encoding='utf-8') if TAGS_DATA_FILE.exists() else ""
    tags = parse_tags_yaml(text)
    by_slug = {t["slug"]: t for t in tags}

    added: list[tuple[str, str]] = []
    for slug, original in sorted(missing_tags.items()):
        if slug in by_slug:
            continue
        entry = {"name": original, "slug": slug}
        tags.append(entry)
        by_slug[slug] = entry
        added.append((original, slug))
        print(f"✅ Added to _data/tags.yml: tag '{original}' (slug: {slug})")

    if added:
        tags.sort(key=lambda t: t["slug"])
        TAGS_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        TAGS_DATA_FILE.write_text(serialize_tags_yaml(tags), encoding='utf-8')

    return added


def load_tag_slugs() -> set[str]:
    """Return the set of tag slugs already registered in _data/tags.yml."""
    if not TAGS_DATA_FILE.exists():
        return set()
    return {t["slug"] for t in parse_tags_yaml(TAGS_DATA_FILE.read_text(encoding='utf-8')) if t.get("slug")}


def load_category_data() -> list[dict]:
    if not CATEGORIES_DATA_FILE.exists():
        return []
    return parse_categories_yaml(CATEGORIES_DATA_FILE.read_text(encoding='utf-8'))


def load_category_slugs(categories: list[dict]) -> set[str]:
    """Return the set of category slugs already registered in _data/categories.yml."""
    return {c["slug"] for c in categories if c.get("slug")}


def load_subcategory_keys(categories: list[dict]) -> set[tuple[str, str]]:
    """Return the set of (cat_slug, sub_slug) pairs already registered in _data/categories.yml."""
    keys: set[tuple[str, str]] = set()
    for cat in categories:
        cat_slug = cat.get("slug")
        if not cat_slug:
            continue
        for sub in cat.get("subcategories") or []:
            sub_slug = sub.get("slug")
            if sub_slug:
                keys.add((cat_slug, sub_slug))
    return keys


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
    Return three dicts of items that need registering in the data files:
        missing_cats:    {slug: original_name}
        missing_tags:    {slug: original_name}
        missing_subcats: {(cat_slug, sub_slug): (cat_original, sub_original)}
    """
    categories_data  = load_category_data()
    existing_cats    = load_category_slugs(categories_data)
    existing_subcats = load_subcategory_keys(categories_data)
    existing_tags    = load_tag_slugs()

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


def build_pr_comment(
    added_tags:      list[tuple[str, str]],
    added_cat_data:  list[tuple[str, str]],
    added_sub_data:  list[tuple[str, str, str, str]],
    post_files:      list[str],
) -> str:
    total = len(added_tags) + len(added_cat_data) + len(added_sub_data)
    posts_list = '\n'.join(f"- `{f}`" for f in post_files)

    lines = [
        "## 🤖 Auto-registered categories/tags\n",
        f"The following **{total} entrie(s)** were automatically added to the data "
        f"files and committed to this branch based on the modified post(s). Their "
        f"pages and RSS feeds are generated at build time — nothing else to create:\n",
        f"<details><summary>Modified posts ({len(post_files)})</summary>\n\n"
        f"{posts_list}\n\n</details>\n",
    ]

    if added_cat_data or added_sub_data:
        lines.append(f"### 🗂️ _data/categories.yml ({len(added_cat_data) + len(added_sub_data)})\n")
        for original, slug in added_cat_data:
            lines.append(
                f"- category **{original}** (`{slug}`, icon defaulted to "
                f"`{DEFAULT_CATEGORY_ICON}` — please review)"
            )
        for cat_original, cat_slug, sub_original, sub_slug in added_sub_data:
            lines.append(f"- subcategory **{cat_original} › {sub_original}** (`{sub_slug}`)")
        lines.append("")

    if added_tags:
        lines.append(f"### 🏷️ _data/tags.yml ({len(added_tags)})\n")
        for original, slug in added_tags:
            lines.append(
                f"- tag **{original}** (`{slug}`) → `/topicos/{slug}/`"
            )
        lines.append("")

    lines += [
        "---",
        "> _Committed by `github-actions[bot]` · "
        "workflow: `sync-category-tag-data.yml`_",
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

    print(f"\n🔍 Scanning {len(post_files)} post file(s) for missing categories/tags...\n")

    missing_cats, missing_tags, missing_subcats = collect_missing(post_files)

    total_missing = len(missing_cats) + len(missing_tags) + len(missing_subcats)
    if total_missing == 0:
        print("\n✅ All categories, subcategories, and tags are already registered — nothing to add.")
        write_output('created_count', '0')
        write_output('pr_comment', '')
        return

    print("\n📝 Syncing _data/categories.yml...")
    added_cat_data, added_sub_data = sync_categories_data(missing_cats, missing_subcats)

    print("\n📝 Syncing _data/tags.yml...")
    added_tags = sync_tags_data(missing_tags)

    total_created = len(added_tags) + len(added_cat_data) + len(added_sub_data)
    comment = build_pr_comment(added_tags, added_cat_data, added_sub_data, post_files)

    write_output('created_count', str(total_created))
    write_output('pr_comment', comment)

    print(f"\n🎉 Done — {total_created} entrie(s) registered.")


if __name__ == '__main__':
    main()
