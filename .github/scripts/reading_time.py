#!/usr/bin/env python3
"""
reading_time.py — reading-time estimate shared by the CI scripts

A line-for-line port of _plugins/reading_time.rb, the Jekyll plugin that fills
`reading_time` on every post whose front matter does not set it. Two scripts
need the same number outside the Jekyll build:

  * audit_blog.py — warns when a hand-authored `reading_time:` has drifted
    away from what the plugin would compute;
  * build_og_cards.py — prints the reading time on generated Open Graph cards
    for posts that no longer carry the field.

Keep this module and the Ruby plugin in sync: same stripping, same word
regex, same rates. Rates can be overridden in _config.yml:

    reading_time:
      words_per_minute: 200
      code_words_per_minute: 150
      seconds_per_image: 10

Run directly to print the counts and estimate for one or more posts:

    python3 .github/scripts/reading_time.py _posts/2026-04-10-meu-novo-artigo.md
"""

from __future__ import annotations

import math
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_FILE = ROOT / "_config.yml"

DEFAULTS = {
    "words_per_minute": 200,
    "code_words_per_minute": 150,
    "seconds_per_image": 10,
}

FENCED_CODE   = re.compile(r"^[ \t]{0,3}((`|~)\2{2,})(?!\2)[^\n]*\n.*?^[ \t]{0,3}\1\2*[ \t]*$\n?", re.S | re.M)
PRE_BLOCK     = re.compile(r"<pre\b[^>]*>.*?</pre\s*>", re.S | re.I)
HTML_COMMENT  = re.compile(r"<!--.*?-->", re.S)
SCRIPT_STYLE  = re.compile(r"<(script|style)\b[^>]*>.*?</\1\s*>", re.S | re.I)
LIQUID_TAG    = re.compile(r"\{%.*?%\}", re.S)
LIQUID_OBJECT = re.compile(r"\{\{.*?\}\}", re.S)
HTML_TAG      = re.compile(r"</?[A-Za-z][^>]*>", re.S)
HTML_ENTITY   = re.compile(r"&(?:#\d+|#x[0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);")
MD_IMAGE      = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
MD_LINK       = re.compile(r"\[([^\]]*)\]\([^)]*\)")
MD_LINK_DEF   = re.compile(r"^[ \t]{0,3}\[[^\]]+\]:[ \t]*\S.*$", re.M)
# Ruby's [[:alnum:]] is letters + digits in any script; Python's \w adds "_".
WORD          = re.compile(r"[^\W_]+(?:['’\-][^\W_]+)*")

IMAGE_MARKERS = [
    re.compile(r"!\[[^\]]*\]\([^)]*\)"),               # ![alt](src)
    re.compile(r"<img\b", re.I),                       # <img …>
    re.compile(r"\{%-?\s*include\s+photo\.html\b"),    # {% include photo.html … %}
]

CONFIG_NUMBER = re.compile(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?")


class ReadingTimeConfigError(ValueError):
    """Raised when the reading-time configuration cannot be calculated safely."""


@dataclass(frozen=True)
class Counts:
    prose: int
    code: int
    images: int


def words(text: str) -> int:
    return len(WORD.findall(text))


def strip_markup(text: str) -> str:
    text = HTML_COMMENT.sub(" ", text)
    text = SCRIPT_STYLE.sub(" ", text)
    text = LIQUID_TAG.sub(" ", text)
    text = LIQUID_OBJECT.sub(" ", text)
    text = MD_LINK_DEF.sub(" ", text)
    text = MD_IMAGE.sub(r"\1", text)
    text = MD_LINK.sub(r"\1", text)
    text = HTML_TAG.sub(" ", text)
    text = HTML_ENTITY.sub(" ", text)
    return text


def count(body: str) -> Counts:
    """Word counts of a post body (everything after the front matter)."""
    text = unicodedata.normalize("NFC", body.replace("\r\n", "\n"))

    images = sum(len(marker.findall(text)) for marker in IMAGE_MARKERS)

    code = 0

    def take_fence(m: re.Match) -> str:
        nonlocal code
        lines = m.group(0).splitlines()          # opening fence, body…, closing fence
        code += words("\n".join(lines[1:-1]))
        return " "

    def take_pre(m: re.Match) -> str:
        nonlocal code
        code += words(strip_markup(m.group(0)))
        return " "

    text = FENCED_CODE.sub(take_fence, text)
    text = PRE_BLOCK.sub(take_pre, text)

    return Counts(prose=words(strip_markup(text)), code=code, images=images)


def estimate(body: str, config: dict | None = None) -> int:
    """Estimated reading time in whole minutes (never below 1)."""
    cfg = validated_config(config)
    c = count(body)
    minutes = (
        c.prose / cfg["words_per_minute"]
        + c.code / cfg["code_words_per_minute"]
        + c.images * cfg["seconds_per_image"] / 60.0
    )
    return max(math.ceil(minutes), 1)


def validated_config(config: dict | None = None) -> dict:
    if config is not None and not isinstance(config, dict):
        raise ReadingTimeConfigError(
            "Invalid reading_time configuration: expected a mapping"
        )

    merged = {**DEFAULTS, **(config or {})}
    requirements = {
        "words_per_minute": ("a positive number", lambda value: value > 0),
        "code_words_per_minute": ("a positive number", lambda value: value > 0),
        "seconds_per_image": ("a non-negative number", lambda value: value >= 0),
    }
    for key, (description, predicate) in requirements.items():
        value = merged[key]
        valid = (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(value)
            and predicate(value)
        )
        if not valid:
            raise ReadingTimeConfigError(
                f"Invalid reading_time configuration: `reading_time.{key}` "
                f"must be {description} (got {value!r})"
            )
    return merged


def load_config(config_file: Path = CONFIG_FILE) -> dict:
    """Read the `reading_time:` block of _config.yml without PyYAML.

    Only flat `key: <number>` lines indented under `reading_time:` are
    understood — the same shape the Ruby plugin documents.
    """
    if not config_file.exists():
        return {}
    overrides: dict[str, int | float] = {}
    in_block = False
    for line in config_file.read_text(encoding="utf-8").splitlines():
        block = re.match(r"^reading_time:\s*(.*?)\s*$", line)
        if block:
            trailing = block.group(1)
            if trailing and not trailing.startswith("#"):
                raise ReadingTimeConfigError(
                    "Invalid reading_time configuration: expected a mapping"
                )
            in_block = True
            continue
        if in_block:
            m = re.match(r"^\s+([a-z_]+):\s*(.*?)\s*$", line)
            if m and m.group(1) in DEFAULTS:
                key = m.group(1)
                raw_value = re.sub(r"\s+#.*$", "", m.group(2)).strip()
                if not CONFIG_NUMBER.fullmatch(raw_value):
                    requirement = (
                        "a non-negative number"
                        if key == "seconds_per_image"
                        else "a positive number"
                    )
                    raise ReadingTimeConfigError(
                        f"Invalid reading_time configuration: `reading_time.{key}` "
                        f"must be {requirement} (got {raw_value!r})"
                    )
                overrides[key] = (
                    float(raw_value)
                    if any(marker in raw_value.lower() for marker in (".", "e"))
                    else int(raw_value)
                )
                continue
            if line.strip() and not line.startswith((" ", "\t")):
                in_block = False
    validated_config(overrides)
    return overrides


def split_body(text: str) -> str:
    """Return everything after the front matter block (or the whole text)."""
    m = re.match(r"^---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    return text[m.end():] if m else text


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    config = load_config()
    for arg in argv:
        path = Path(arg)
        body = split_body(path.read_text(encoding="utf-8"))
        c = count(body)
        print(f"{path.name}: {estimate(body, config)} min "
              f"(prose={c.prose} code={c.code} images={c.images})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
