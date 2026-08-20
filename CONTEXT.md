# Tecnologia & Viagens Blog

A Jekyll blog mixing software engineering and travel/career writing. This glossary defines how content is modeled — a Post's shape and how it relates to Category, Tag, Series, and Trip.

## Language

**Post**:
A single article in `_posts/`. Every Post belongs to at least one Category, may carry any number of Tags, may belong to a Series, and may be a Trip.

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
A Post carrying a `location` or `locations` front matter value (lat/lng/label). Independent of Category — a Trip can belong to any Category, not just a travel-related one.
_Avoid_: Travel post — use Trip.

**Cover image**:
A Post's on-page hero background (front matter field `cover`). Normally an SVG authored to match the site's brand tokens (Playfair Display / Source Serif 4 / JetBrains Mono; palette including `#f5f0e8`, `#2d6a4f`, `#1a1714`, `#b85c00`), sized to 1200×630.

**Social image**:
The raster image that feeds Open Graph/Twitter card tags (front matter field `image`). Must be a raster format (PNG/JPG/GIF) — social crawlers don't reliably render SVG.
_Avoid_: OG image, thumbnail — Social image is canonical.
