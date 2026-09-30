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
NUMBER = re.compile(r"\d+(\.\d+)?")


def indexed_pages(site: Path) -> list[Path]:
    """The built pages Pagefind indexes: those tagged data-pagefind-body, outside its own output."""
    pages = []
    for page in sorted(site.rglob("*.html")):
        if page.is_relative_to(site / "pagefind"):
            continue
        if "data-pagefind-body" in page.read_text(encoding="utf-8"):
            pages.append(page)
    return pages


def page_language(html: str) -> str | None:
    match = HTML_LANG.search(html)
    return match.group(1).lower() if match else None


def sort_key_errors(html: str) -> list[str]:
    """Why sorting would drop this page, if anything is missing or malformed."""
    sorts = {key: value.strip() for key, value in SORT_VALUE.findall(html)}
    errors = [
        f"no value for sort key '{key}' — sorting by it would drop this Post"
        for key in SORT_KEYS
        if not sorts.get(key)
    ]
    reading_time = sorts.get("reading_time")
    if reading_time and not NUMBER.fullmatch(reading_time):
        errors.append(f"reading_time '{reading_time}' is not a number")
    return errors


def expected_counts(site: Path, pages: list[Path]) -> tuple[Counter, list[str]]:
    """Posts per language as built, plus every per-page problem found."""
    expected: Counter = Counter()
    errors = []
    for page in pages:
        rel = page.relative_to(site).as_posix()
        html = page.read_text(encoding="utf-8")
        lang = page_language(html)
        if lang is None:
            errors.append(f"{rel}: indexed page without <html lang>")
            continue
        expected[lang] += 1
        errors.extend(f"{rel}: {error}" for error in sort_key_errors(html))
    return expected, errors


def indexed_counts(entry_path: Path) -> Counter:
    """Posts per language according to Pagefind's own entry file."""
    languages = json.loads(entry_path.read_text(encoding="utf-8")).get("languages", {})
    return Counter({lang: info.get("page_count", 0) for lang, info in languages.items()})


def coverage_errors(expected: Counter, indexed: Counter) -> list[str]:
    if not expected:
        return ["no page carries data-pagefind-body — nothing would be searchable"]
    return [
        f"language '{lang}': {expected[lang]} Posts built, {indexed[lang]} in the index"
        for lang in sorted(set(expected) | set(indexed))
        if expected[lang] != indexed[lang]
    ]


def main() -> None:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    entry_path = site / "pagefind" / "pagefind-entry.json"
    if not entry_path.is_file():
        raise SystemExit(f"::error::{entry_path} not found — did Pagefind run?")

    expected, errors = expected_counts(site, indexed_pages(site))
    indexed = indexed_counts(entry_path)
    errors.extend(coverage_errors(expected, indexed))

    for lang in sorted(indexed):
        print(f"{lang}: {indexed[lang]} Posts indexed")
    if errors:
        for error in errors:
            print(f"::error::{error}")
        sys.exit(1)
    print(f"Search index OK — {sum(indexed.values())} Posts in {len(indexed)} languages.")


if __name__ == "__main__":
    main()
