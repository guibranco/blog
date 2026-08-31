# Tecnologia & Viagens Blog

A Jekyll blog mixing software engineering and travel/career writing. This glossary defines how content is modeled — a Post's shape and how it relates to Category, Tag, Series, Trip, and Country.

## Language

**Post**:
A single article in `_posts/`. Every Post belongs to at least one Category, may carry any number of Tags, may belong to a Series, and may be a Trip.

**Post language**:
The single language a Post is written in — `en` or `pt-BR` — declared via the mandatory `lang` front matter field and validated in CI (`audit_blog.py`). Independent of Category, Tag, and Series; a Post has exactly one language and no translated counterpart exists elsewhere in the blog — switching the site's UI language relabels chrome (buttons, dates) around a Post, it never changes which Post is being read.
_Avoid_: Locale — Post language is only the `en`/`pt-BR` distinction, not a broader locale (date/currency formatting, region).

**Category**:
One of a small, curated set of top-level content areas (Career, Coding, Infrastructure, Hobbies, Investments, …), defined in `_data/categories.yml`. A Post may belong to more than one Category.
_Avoid_: Topic — Category is curated and finite; that's what distinguishes it from Tag.

**Subcategory**:
A refinement of exactly one parent Category (e.g. Career › Working Abroad), also curated in `_data/categories.yml`. Never spans more than one Category.

**Tag**:
A freeform label a Post carries (front matter field `tags`). Any string becomes a Tag the moment a Post uses it — there is no curated list, unlike Category. Displayed to readers as "Tópico"/"Tópicos" in the site's Portuguese UI; that's a translation of the same concept, not a competing term.
_Avoid_: Topic — as the English domain term. Code, docs, and this glossary say Tag; "Tópico" is pt-BR display copy only.

**Series**:
An ordered group of Posts forming one multi-part piece, declared via the `series` front matter slug. Series membership is independent of Category and Tag.

**Trip**:
A Post carrying a `location` or `locations` front matter value (lat/lng/label) plus a `countries` value naming the Country/Countries it covers. Independent of Category — a Trip can belong to any Category, not just a travel-related one. A single Trip may span more than one Country (e.g. a road trip crossing a border).
_Avoid_: Travel post — use Trip.

**Country**:
One of a curated set of nations a Trip visited, defined in `_data/countries.yml` and declared per-Post via the `countries` front matter field. Curated the same way as Category — an unregistered or misspelled value fails the audit — because it drives the grouping in the travels page's "articles by country" table. Deliberately hand-authored per Trip rather than derived from `location`/`locations` labels, since a label's trailing segment isn't always a Country (e.g. "Comino" is part of Malta, not its own Country).

**Cover image**:
A Post's on-page hero background (front matter field `cover`). Normally an SVG authored to match the site's brand tokens (Playfair Display / Source Serif 4 / JetBrains Mono; palette including `#f5f0e8`, `#2d6a4f`, `#1a1714`, `#b85c00`), sized to 1200×630.

**Social image**:
The raster image that feeds Open Graph/Twitter card tags (front matter field `image`). Must be a raster format (PNG/JPG/GIF) — social crawlers don't reliably render SVG.
_Avoid_: OG image, thumbnail — Social image is canonical.
