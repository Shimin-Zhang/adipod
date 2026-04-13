# Create OG/Social Card Image for a Topic Post

Generate a dithered neon OG image for a topic article and wire it into the post.

## Inputs

Ask the user which topic post needs an OG image. Read the article to understand the subject matter.

## Steps

### 1. Find a source image

Search Unsplash (or Pexels/Pixabay) using Playwright for a large, high-contrast, royalty-free **cyberpunk-themed** image. The ADI Pod brand uses industrial/cyberpunk imagery — networks, cables, circuit boards, machines, gears, server racks, neon cityscapes, mechanical parts, fiber optics, etc. Pick something that works as a visual metaphor for the article's theme — e.g. tangled cables for complexity, gears for orchestration, circuit boards for architecture, fiber optics for data flow.

Prefer images with:
- **Grounded and detailed** — real-world photographs of physical objects, not abstract renders or bokeh. Server racks with patch cables, close-up PCBs, industrial machinery, mechanical watches, engine parts, etc.
- Clear shapes and strong contrast (dithering destroys subtle gradients)
- Lots of fine detail and texture (the dither effect rewards complexity)
- Large resolution (2000px+ on the long side)
- Free license (no attribution required)

Avoid: abstract light trails, bokeh, 3D renders, AI-generated art, stock-photo-style compositions.

Download to `images/<slug>-source.jpg`.

### 2. Dither with neon colors

```bash
python scripts/dither_image.py images/<slug>-source.jpg --neon --size 2
```

This produces `images/<slug>-source_dithered_neon.png` using the site's dark purple/teal Bayer dither effect.

Review the output — if too dark, add `--gamma 1.5` or `--gamma 2.0`. If too busy, try `--size 3` or `--size 4`.

### 3. Add text overlay

```bash
python scripts/add_text_overlay.py images/<slug>-source_dithered_neon.png \
    --title "Title Line 1\nLine 2" \
    --subtitle "Subtitle text here" \
    -o images/<slug>-og.png
```

Guidelines for title text:
- Break the title into 2-3 short lines using `\n`
- Keep each line under ~20 characters for readability at 72px
- The subtitle should be 1 line summarizing the article scope
- Use `--title-size 60` if the title is long

Show the result to the user for approval before proceeding.

### 4. Deploy to site

The overlay script outputs both `.jpg` (for OG meta tags — best social crawler support) and `.webp` (for inline display) automatically. Just point `-o` directly at the public og directory:

```bash
python scripts/add_text_overlay.py images/<slug>-source_dithered_neon.png \
    --title "Title" --subtitle "Subtitle" \
    -o site/public/og/<slug>.png
# Outputs: site/public/og/<slug>.jpg + site/public/og/<slug>.webp
```

Add `ogImage: "/og/<slug>"` (no extension) to the topic post's YAML frontmatter.

The `ogImage` field flows through: `content.config.ts` (topics schema) → `[...slug].astro` → `ArticleLayout` → `BaseLayout`:
- **OG/Twitter meta tags** use `.jpg` (with `og:image:width/height/type`)
- **Inline hero** uses `<picture>` with WebP primary + JPEG fallback, `fetchpriority="high"`, `decoding="async"`, explicit `width`/`height` to prevent CLS

### 5. Verify

Show the user the final image and confirm the frontmatter update. Run `npx astro build` to verify no errors.

## Scripts Reference

| Script | Purpose |
|--------|---------|
| `scripts/dither_image.py` | Bayer dither with optional neon colors |
| `scripts/add_text_overlay.py` | Crop, gradient overlay, title/subtitle/byline |

### dither_image.py flags
- `--neon` — dark purple/teal color scheme
- `--size N` — cell size in pixels (default 2)
- `--gamma N` — brightness correction (default 1.0)
- `-o PATH` — output path

### add_text_overlay.py flags
- `--title TEXT` — title with `\n` for line breaks
- `--subtitle TEXT` — subtitle line
- `--byline TEXT` — bottom-right text (default: adipod.ai)
- `--title-size N` — font size (default: 72)
- `--width N` / `--height N` — output dimensions (default: 1200x630)
- `-o PATH` — output path (required)
