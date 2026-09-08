---
status: proposed
---

# Per-post image folders, with the OG raster generated at build time instead of authored

Today a Post's images are flat files named after a short hand-picked slug — `/assets/img/posts/<slug>.svg` (`cover`) and `/assets/img/posts/<slug>.<ext>` (`image`) — except the Amsterdã post, which already keeps its gallery photos in an ad hoc per-post folder (`/assets/img/posts/amsterda-2026/`). That folder is the pattern this formalizes: every Post gets one folder, `/assets/img/posts/<post-slug>/` (the full Jekyll post slug, not a short curated name, so it needs no extra authoring), holding its Hero source and its Gallery images together.

`cover` stays the field name for the authored Hero source — SVG for the illustrated-post shape, raster for the travel-post shape — rather than introducing a new `hero:` field, so no front-matter migration is forced on existing posts. `image` stops being hand-authored: when the Hero source is SVG, a Jekyll generator plugin rasterizes it into `_site/` at build time and that generated file is used as the Open Graph asset; when the Hero source is already raster, nothing is generated — that file serves as both the on-page Hero and the OG asset directly. Generated rasters are never committed — they're build output like any other `_site/` artifact, regenerated on every build.

## Consequences

- Existing posts keep working unmigrated (flat files, hand-authored `image`) until moved to the folder shape — this is an opportunistic migration, not a forced backfill.
- `audit_blog.py`'s local-image and extension checks need to learn the `/assets/img/posts/<slug>/` folder convention alongside the flat one.
- The Jekyll build gains a new step: SVG→raster conversion for illustrated-post Heroes, which didn't exist before.
- See [`CONTEXT.md`](../../CONTEXT.md)'s **Hero** and **Gallery** terms for the domain definitions this plan builds on.
