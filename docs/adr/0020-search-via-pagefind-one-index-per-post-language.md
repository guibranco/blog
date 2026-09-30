---
status: accepted
---

# Search runs on Pagefind, with one index per Post language

`/busca/` used Lunr.js over `search.json`, a Liquid template that dumped every Post (title, fields and up to 5,000 characters of body) into one file. Every visitor downloaded all of it before the first result, about 330 KB for 62 Posts, growing with the archive. Lunr's default pipeline is English only: Portuguese Posts went through the English stemmer and stop-word list, and nothing folded accents, so "analise" did not find "análise" (GitHub issue #189).

**The index is built by Pagefind after `jekyll build`, and only Post bodies go in.** `deploy.yml` runs the Pagefind CLI over `_site/`. It is installed with pip from `requirements-search.txt`, pinned by version and sha256 like the image tooling. Pagefind writes `_site/pagefind/`, a chunked index the browser fetches piece by piece: the chunks a query needs, then one fragment per result shown. `data-pagefind-body` sits only on the Post layout's article body, so home, Category, Tag and other listing pages stay out and no Post appears twice. The page fields come from the Post's own markup: the title and description from the hero, the rest from a hidden block, `_includes/search-index-fields.html`.

- **Searchable fields** are Pagefind metadata: title, description, Categories and Tags. They carry the same relative boosts the Lunr index used (10, 4, 6 and 6 against the body's 1), passed as `metaWeights`.
- **Display and sort values** (Published date, Updated date, Reading time and a title key) are Pagefind filters and sorts, not metadata. Pagefind indexes every metadata value as searchable words and matches word prefixes, so a date kept there would make "23" match every Post published on a 23rd. For the same reason the block sets an empty `image`, which stops Pagefind from storing the Hero's path, where "blog" or "png" would otherwise match nearly every Post.
- **Every Post carries all four sort keys.** Pagefind drops a page from a sorted search when it lacks the key, without any error.

**Each Post language gets its own index, and the search page searches each with its own stemmer.** Pagefind splits the index by `<html lang>`, which the Post layout takes from the mandatory `lang` (ADR-0006), so Portuguese Posts are stemmed as Portuguese and English Posts as English. Pagefind also normalizes diacritics on both sides, so accents never block a match; an exact accent match only ranks higher. In the browser, one Pagefind instance searches the index of its page's `<html lang>`. An index merged into it with `mergeIndex` is searched with that instance's WebAssembly, so its stemmer would be the page's language, not the Post's. The search page therefore imports `pagefind.js` once per language under a distinct URL (`?lang=en`). Each import is a separate module with its own worker and WebAssembly. Each is initialised with `<html lang>` briefly set to its language, inside one synchronous step, and the page's own value is restored before anything renders.

**The page merges the languages itself.** By relevance, results are sorted by Pagefind's score, which is comparable because both indexes use the same ranking and weights. With a sort chosen, each index already returns its hits in order, and the page merges the two lists by comparing their heads. Pagefind's own multi-index sort only interleaves the lists. Each result's data is a separate fetch, so the page shows ten at a time with a "show more" button instead of rendering every match.

**The URL contract is unchanged, and all languages are searched by default.** `?q=` works as before, including from the sidebar and 404 forms. An empty query still lists every Post, newest first. A new, optional `?lang=pt-BR|en` narrows to one Post language, and every result shows its language badge. Filtering by the reader's UI language by default would hide half the archive: a Post has exactly one language and no translation, and the UI language never changes which Post is read (CONTEXT.md, **Post language**).

## Consequences

- The per-language modules rely on Pagefind 1.5 reading `<html lang>` synchronously inside `init()`. A future version that reads it later would put both modules on the page's language. The page then drops duplicate hit ids, so search keeps working, but English Posts would be stemmed as Portuguese. The pin sits in `requirements-search.txt`; after a bump, check that an English query such as "deployment" still finds "deploying".
- `search.json` and the Lunr script are gone. ADR-0013 names `search.json` among the readers of `reading_time`; the reader is now the index-fields include.
- `check_search_index.py` fails the deploy if the index is missing a Post or a language, or if a Post lacks a sort key. Those are the ways a template change could silently empty search.
- `jekyll serve` alone has no index. The page then says search is unavailable; running Pagefind once fills `_site/pagefind/`, and `keep_files` preserves it across regenerations (README, "Desenvolvimento local").
- Alphabetical order uses the title slug (`slugify: "latin"`), so accents and punctuation do not affect it, the same way the old `localeCompare` ignored them.
- The Pagefind CLI also writes its prebuilt UI bundles into `_site/pagefind/`. The site does not load them.
