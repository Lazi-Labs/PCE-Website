# PCE Website Rebuild — working folder

Rebuild of callperfectcatch.com (old vendor being cut). Design work happens in the
**"PCE Website" Claude Design project** (`b166afc9-f1a8-4a50-b511-3c56054ad40c`).

## What's here

- `archive.tar.gz` — full wp-content export from the live WordPress site (256MB, pulled 2026-08-13). Gitignored.
- `extracted/` — the export unpacked (gitignored):
  - `wp-content/uploads/20*/` — the complete media library (610 originals, WP size-variants excluded)
  - `wp-content/uploads/elementor/css/post-7.css` — **the Elementor global design kit** (colors, type, button/input specs). Source of truth for brand tokens.
  - `wp-content/uploads/elementor/css/post-*.css` — per-page layout CSS (~120 pages)
  - `wp-content/uploads/2026/05/Burbank-Big-Regular-Bold-1.woff2` — custom display font
  - `wp-content/uploads/clean.sql` — fresh-install seed only; **no post/page data** (Elementor page JSON is not in this export)
- `media-originals.txt` — index of the 610 original media files

## Key facts learned from the export (2026-08-13)

- Display font is **Burbank Big Bold** (custom, self-hosted) for ALL headings and buttons — not Sofia Sans.
- Body font is **Sofia Sans** 18px/1.9 — Roboto is not used anywhere.
- Kit text color is `#001E33` (not `#0C0D0E`).
- Button spec: coral `#F24E45` fill, border `1px 1px 4px` in `#A7130C`, radius 12px, padding 16/28/13, hover inverts to deep-red fill. Form inputs mirror it with teal borders.

## Related

- Page structure/copy: 133-page HTML+Markdown archive at
  `~/yr/00-storage/pce/PCE-Website/callperfectcatch_public_rebuild_handoff_2026-08-08/`
- Design project holds: brand tokens (`styles.css`), Burbank woff2, full-res logo,
  kit CSS (`reference/elementor-kit.css`), media inventory card (`reference/media-library.html`).
