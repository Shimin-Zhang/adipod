#!/usr/bin/env python3
"""Convert any image into the ADI Pod stylized dither effect.

Replicates the site's DitherBackground.astro shader logic:
  - 8×8 Bayer ordered dithering
  - 45° rotation of the dither grid
  - Configurable cell size (default 2px)
  - Optional neon color mode (dark purple/teal gradient from the site)

Usage:
    python scripts/dither_image.py input.jpg                  # → B&W dither
    python scripts/dither_image.py input.jpg --neon            # → dark neon colors
    python scripts/dither_image.py input.jpg --size 4          # larger cells
    python scripts/dither_image.py input.jpg --gamma 2.0       # adjust gamma
    python scripts/dither_image.py input.jpg -o out.png        # explicit output
"""
import argparse
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image


# 8×8 Bayer matrix — identical to the GLSL shader
BAYER_8x8 = np.array([
    [ 0, 32,  8, 40,  2, 34, 10, 42],
    [48, 16, 56, 24, 50, 18, 58, 26],
    [12, 44,  4, 36, 14, 46,  6, 38],
    [60, 28, 52, 20, 62, 30, 54, 22],
    [ 3, 35, 11, 43,  1, 33,  9, 41],
    [51, 19, 59, 27, 49, 17, 57, 25],
    [15, 47,  7, 39, 13, 45,  5, 37],
    [63, 31, 55, 23, 61, 29, 53, 21],
], dtype=np.float64) / 64.0

# Neon palette from DitherBackground.astro (dark theme), boosted for standalone use.
# Original shader values are ~15% max brightness (subtle background); we scale up
# the lit colors so the dither pattern is clearly visible in a standalone image.
NEON_DARK = np.array([0.059, 0.059, 0.067])   # #0f0f11
NEON_C1   = np.array([0.55,  0.12,  0.45])    # magenta-purple (boosted)
NEON_C2   = np.array([0.08,  0.45,  0.55])    # teal (boosted)
NEON_C3   = np.array([0.38,  0.08,  0.55])    # deep purple (boosted)


def _neon_color(uv_x: np.ndarray, uv_y: np.ndarray) -> np.ndarray:
    """Compute the neon hue gradient, matching the shader (time=0)."""
    h = np.mod(uv_x * 0.7 + uv_y * 0.3, 1.0)

    # Three-segment linear gradient: c1→c2→c3→c1
    nc = np.zeros((*h.shape, 3), dtype=np.float64)
    m1 = h < 0.33
    m2 = (~m1) & (h < 0.66)
    m3 = ~(m1 | m2)

    t1 = (h * 3.0)[..., None]
    t2 = ((h - 0.33) * 3.0)[..., None]
    t3 = ((h - 0.66) * 3.0)[..., None]

    nc[m1] = NEON_C1 * (1 - t1[m1]) + NEON_C2 * t1[m1]
    nc[m2] = NEON_C2 * (1 - t2[m2]) + NEON_C3 * t2[m2]
    nc[m3] = NEON_C3 * (1 - t3[m3]) + NEON_C1 * t3[m3]
    return nc


def dither_image(
    input_path: str,
    output_path: str | None = None,
    cell_size: int = 2,
    gamma: float = 1.0,
    neon: bool = False,
) -> str:
    img = Image.open(input_path).convert("RGB")
    src = np.asarray(img, dtype=np.float64) / 255.0
    h, w = src.shape[:2]

    # Luma (BT.601, matches the shader)
    luma = src[:, :, 0] * 0.299 + src[:, :, 1] * 0.587 + src[:, :, 2] * 0.114
    luma = np.power(luma, gamma)

    # Sample image at cell centres (floor(px/cell)*cell + cell/2)
    ys = np.arange(h)
    xs = np.arange(w)
    cx = (np.floor(xs / cell_size) * cell_size + cell_size * 0.5).astype(int).clip(0, w - 1)
    cy = (np.floor(ys / cell_size) * cell_size + cell_size * 0.5).astype(int).clip(0, h - 1)
    cell_luma = luma[np.ix_(cy, cx)]

    # Pixel coordinate grids
    yy, xx = np.meshgrid(ys, xs, indexing="ij")

    # Rotate 45° (matching the shader's a45=0.7854)
    cos45 = math.cos(math.pi / 4)
    sin45 = math.sin(math.pi / 4)
    rpx_x = cos45 * xx - sin45 * yy
    rpx_y = sin45 * xx + cos45 * yy

    # Bayer threshold lookup at floor(rotated_px / cell)
    bx = np.floor(rpx_x / cell_size).astype(int) % 8
    by = np.floor(rpx_y / cell_size).astype(int) % 8
    threshold = BAYER_8x8[by, bx]

    # Threshold: lit where luma > bayer value
    lit = cell_luma > threshold

    if neon:
        # UV coordinates normalized [0,1]
        uv_x = xx.astype(np.float64) / w
        uv_y = yy.astype(np.float64) / h
        nc = _neon_color(uv_x, uv_y)

        # mix(dark, neon_color, lit)
        result = np.zeros((h, w, 3), dtype=np.float64)
        lit3 = lit[..., None]
        result = NEON_DARK * (1 - lit3) + nc * lit3
        out = Image.fromarray((result * 255).clip(0, 255).astype(np.uint8))
    else:
        out = Image.fromarray((lit.astype(np.uint8) * 255)).convert("L")

    if output_path is None:
        p = Path(input_path)
        suffix = "_dithered_neon" if neon else "_dithered"
        output_path = str(p.with_stem(p.stem + suffix).with_suffix(".png"))

    out.save(output_path)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Stylized Bayer dither (ADI Pod style)")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("-o", "--output", help="Output image path (default: <input>_dithered.png)")
    parser.add_argument("--size", type=int, default=2, help="Dither cell size in pixels (default: 2)")
    parser.add_argument("--gamma", type=float, default=1.0, help="Gamma correction (default: 1.0)")
    parser.add_argument("--neon", action="store_true", help="Apply dark neon purple/teal color scheme")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    out = dither_image(args.input, args.output, cell_size=args.size, gamma=args.gamma, neon=args.neon)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
