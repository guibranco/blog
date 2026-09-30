#!/usr/bin/env python3
"""
check_search_index.py — verify the Pagefind index covers every Post

Runs in deploy.yml right after `python3 -m pagefind --site _site` (ADR-0020).
Pagefind only indexes pages carrying `data-pagefind-body`, splits them by
their <html lang>, and silently drops a page from a sorted search when it
lacks a sort key. A template change that loses any of those would ship a
search page that quietly misses Posts, so this check fails the deploy instead:

  1. Every built page with `data-pagefind-body` (every Post) is counted by its
     <html lang>, and each language's count must equal the page_count of that
     language's index in pagefind/pagefind-entry.json — no language missing,
     none extra.
  2. Every such page carries a non-empty value for each sort key /busca/
     orders by (see _includes/search-index-fields.html), and reading_time is
     a number so Pagefind sorts it numerically.

Standard library only; runs on the workflow's Python 3.12.

Usage:
  python3 .github/scripts/check_search_index.py [SITE_DIR]   # default: _site
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

SORT_KEYS = ("date", "updated", "reading_time", "title_key")

HTML_LANG = re.compile(r"<html\b[^>]*\blang=\"([^\"]+)\"", re.IGNORECASE)
SORT_VALUE = re.compile(r"data-pagefind-sort=\"([a-z_]+)\"[^>]*>([^<]*)<")


def main() -> None:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    entry_path = site / "pagefind" / "pagefind-entry.json"
    if not entry_path.is_file():
        raise SystemExit(f"::error::{entry_path} not found — did Pagefind run?")

    errors = []
    expected = Counter()
    for page in sorted(site.rglob("*.html")):
        if page.is_relative_to(site / "pagefind"):
            continue
        html = page.read_text(encoding="utf-8")
        if "data-pagefind-body" not in html:
            continue
        rel = page.relative_to(site).as_posix()

        lang = HTML_LANG.search(html)
        if not lang:
            errors.append(f"{rel}: indexed page without <html lang>")
            continue
        expected[lang.group(1).lower()] += 1

        sorts = {key: value.strip() for key, value in SORT_VALUE.findall(html)}
        for key in SORT_KEYS:
            if not sorts.get(key):
                errors.append(f"{rel}: no value for sort key '{key}' — sorting by it would drop this Post")
        if sorts.get("reading_time") and not re.fullmatch(r"\d+(\.\d+)?", sorts["reading_time"]):
            errors.append(f"{rel}: reading_time '{sorts['reading_time']}' is not a number")

    languages = json.loads(entry_path.read_text(encoding="utf-8")).get("languages", {})
    indexed = Counter({lang: info.get("page_count", 0) for lang, info in languages.items()})

    if not expected:
        errors.append("no page carries data-pagefind-body — nothing would be searchable")
    for lang in sorted(set(expected) | set(indexed)):
        if expected[lang] != indexed[lang]:
            errors.append(f"language '{lang}': {expected[lang]} Posts built, {indexed[lang]} in the index")

    for lang in sorted(indexed):
        print(f"{lang}: {indexed[lang]} Posts indexed")
    if errors:
        for error in errors:
            print(f"::error::{error}")
        sys.exit(1)
    print(f"Search index OK — {sum(indexed.values())} Posts in {len(indexed)} languages.")


if __name__ == "__main__":
    main()
