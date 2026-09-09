# Tecnologia & Viagens Blog

A Jekyll blog mixing software engineering and travel/career writing. This glossary defines how content is modeled — a Post's shape (Hero, Gallery, Category, Tag, Series, Trip, Country, Published date, Updated date, Table of Contents) and the site's two standalone pages, Journey and Editorial Notes.

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
One of a curated set of nations a Trip visited, defined in `_data/countries.yml` and declared per-Post via the `countries` front matter field. Identified by its English name (the entry's `name`, e.g. "United Kingdom") — that is the value a Post declares and the audit checks; the pt-BR label (`name_pt`, e.g. "Reino Unido") is a display translation applied only when the UI language is pt-BR (ADR 0010). Curated the same way as Category — an unregistered or misspelled value fails the audit — because it drives the grouping in the travels page's "articles by country" table. Deliberately hand-authored per Trip rather than derived from `location`/`locations` labels, since a label's trailing segment isn't always a Country (e.g. "Comino" is part of Malta, not its own Country).

**Hero**:
A Post's primary image — shown in list/card thumbnails, at the top of the Post page, and via Open Graph/Twitter Card when shared. Nearly every Post has one. Authored one of two ways: an SVG matching the site's brand tokens (Playfair Display / Source Serif 4 / JetBrains Mono; palette including `#f5f0e8`, `#2d6a4f`, `#1a1714`, `#b85c00`) plus a separate raster file for sharing — the illustrated-post shape (front matter fields `cover` + `image`) — or a single raster photo serving both roles directly — the travel-post shape (`image` only, no `cover`).
_Avoid_: Cover image, Social image, featured image, post image, OG image, thumbnail — Hero is canonical regardless of which front-matter field or file shape backs it.

**Gallery**:
A set of images embedded in a Post's body content (not front matter) and shown to readers via a lightbox, enabled per-Post with the `gallery: true` front matter flag. Independent of Hero — a Post may have a Gallery, a Hero, both, or neither, though nearly every Post has a Hero.

**Published date**:
The day a Post went live (front matter `date`). Every Post has one and it is always shown with the Post.
_Avoid_: Date, post date, created date.

**Updated date**:
The most recent day a Post's content changed after it went live, shown beside the Published date only when it falls on a different day. Derived from the Post's edit history (ADR 0007), never hand-authored.
_Avoid_: Last modified, modification date — those name the mechanism and the front matter field, not the concept; Revised on.

**Table of Contents**:
A navigable list of a Post's section headings, offered alongside the Post body only when the Post has enough sections to be worth jumping between. Readers see it as "Sumário" in the Portuguese UI; that is display copy for the same concept, as with Tag/"Tópico". Abbreviated TOC in code.
_Avoid_: Summary — in English that names an abstract, and a Post's description already plays that role.

**Journey**:
The standalone page at `/trajetoria/`, a timeline of the author's life and career (`_data/journey.yml`). Not a Post — carries no Category, Tag, or Series. Authored bilingually in a single file (both pt-BR and en, switched client-side), unlike a Post, which has exactly one Post language.
_Avoid_: Timeline — Journey is the canonical name for the page; "timeline" describes its layout, not the concept.

**Editorial Notes**:
The standalone page at `/notas-editoriais/`, documenting the blog's own production process — why it exists, how posts get made (including AI's role), and its sourcing/correction/privacy policies (`_data/editorial.yml`). Not a Post; structured the same way as Journey (single bilingual file, no Category, Tag, or Series) despite unrelated content — the two are independent concepts, not variants of a shared "page" type.
_Avoid_: Colophon, About page — Editorial Notes is canonical.
