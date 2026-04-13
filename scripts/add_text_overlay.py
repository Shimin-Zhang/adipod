#!/usr/bin/env python3
"""Overlay article title + subtitle on a dithered image for OG/social cards.

Usage:
    python scripts/add_text_overlay.py images/dithered.png \\
        --title "AI Coding Agents\\nCompared" \\
        --subtitle "Claude Code, Codex, Cursor, Pi Agent, and the Rest" \\
        -o images/og-card.png

    python scripts/add_text_overlay.py images/dithered.png \\
        --title "Topic Title" \\
        --byline "adipod.ai" \\
        --width 1200 --height 630
"""
import argparse
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_BOLD = "/usr/share/fonts/opentype/fira/FiraSans-Bold.otf"
FONT_REG = "/usr/share/fonts/opentype/fira/FiraSans-Regular.otf"

# Default colors
TEXT_COLOR = (255, 255, 255)
SUBTITLE_COLOR = (180, 160, 220)  # soft lavender
BYLINE_COLOR = (120, 200, 220)    # teal accent


def make_og_image(
    input_path: str,
    output_path: str,
    title: str,
    subtitle: str = "",
    byline: str = "adipod.ai",
    width: int = 1200,
    height: int = 630,
    title_size: int = 72,
    subtitle_size: int = 24,
    byline_size: int = 20,
) -> str:
    img = Image.open(input_path).convert("RGB")
    w, h = img.size

    # Crop to target aspect ratio
    target_aspect = width / height
    current_aspect = w / h
    if current_aspect > target_aspect:
        new_w = int(h * target_aspect)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_aspect)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))

    img = img.resize((width, height), Image.LANCZOS)

    # Gradient overlay: transparent left → semi-dark right
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    for x in range(width):
        alpha = int(max(0, min(180, (x - width * 0.3) / (width * 0.7) * 180)))
        draw_overlay.line([(x, 0), (x, height)], fill=(0, 0, 0, alpha))

    img = img.convert("RGBA")
    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB")

    draw = ImageDraw.Draw(img)
    font_title = ImageFont.truetype(FONT_BOLD, title_size)
    font_sub = ImageFont.truetype(FONT_REG, subtitle_size)
    font_byline = ImageFont.truetype(FONT_REG, byline_size)

    margin_right = 60
    margin_bottom = 60

    # Byline at bottom-right
    bb_byline = draw.textbbox((0, 0), byline, font=font_byline)
    byline_w = bb_byline[2] - bb_byline[0]
    byline_x = width - margin_right - byline_w
    byline_y = height - margin_bottom
    draw.text((byline_x, byline_y), byline, fill=BYLINE_COLOR, font=font_byline)

    # Subtitle above byline
    anchor_y = byline_y
    if subtitle:
        sub_wrapped = textwrap.fill(subtitle, width=35)
        bb_sub = draw.multiline_textbbox((0, 0), sub_wrapped, font=font_sub)
        sub_h = bb_sub[3] - bb_sub[1]
        sub_w = bb_sub[2] - bb_sub[0]
        sub_x = width - margin_right - sub_w
        sub_y = byline_y - sub_h - 24
        draw.multiline_text((sub_x, sub_y), sub_wrapped, fill=SUBTITLE_COLOR, font=font_sub)
        anchor_y = sub_y

    # Title above subtitle (interpret \n as newlines)
    title_text = title.replace("\\n", "\n")
    bb_title = draw.multiline_textbbox((0, 0), title_text, font=font_title)
    title_h = bb_title[3] - bb_title[1]
    title_w = bb_title[2] - bb_title[0]
    title_x = width - margin_right - title_w
    title_y = anchor_y - title_h - 20
    draw.multiline_text((title_x, title_y), title_text, fill=TEXT_COLOR, font=font_title)

    # Save JPEG (for OG meta tags — best social crawler support) + WebP (for inline display)
    out = Path(output_path)
    jpg_path = out.with_suffix(".jpg")
    webp_path = out.with_suffix(".webp")

    img.save(str(jpg_path), "JPEG", quality=82, optimize=True)
    img.save(str(webp_path), "WEBP", quality=80, method=6)

    return str(jpg_path), str(webp_path)


def main():
    parser = argparse.ArgumentParser(description="Create OG/social card from dithered image")
    parser.add_argument("input", help="Input dithered image path")
    parser.add_argument("-o", "--output", required=True, help="Output image path")
    parser.add_argument("--title", required=True, help="Title text (use \\n for line breaks)")
    parser.add_argument("--subtitle", default="", help="Subtitle text")
    parser.add_argument("--byline", default="adipod.ai", help="Byline text (default: adipod.ai)")
    parser.add_argument("--width", type=int, default=1200, help="Output width (default: 1200)")
    parser.add_argument("--height", type=int, default=630, help="Output height (default: 630)")
    parser.add_argument("--title-size", type=int, default=72, help="Title font size (default: 72)")
    parser.add_argument("--subtitle-size", type=int, default=24, help="Subtitle font size (default: 24)")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    jpg, webp = make_og_image(
        args.input, args.output, args.title,
        subtitle=args.subtitle, byline=args.byline,
        width=args.width, height=args.height,
        title_size=args.title_size, subtitle_size=args.subtitle_size,
    )
    import os
    print(f"Saved: {jpg} ({os.path.getsize(jpg)//1024}K)")
    print(f"Saved: {webp} ({os.path.getsize(webp)//1024}K)")


if __name__ == "__main__":
    main()
