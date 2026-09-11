#!/usr/bin/env python3
"""Render the social preview card (og-image.png, 1200x630) for Awesome Obsidian.

Usage:  python3 scripts/generate_og_image.py [output_path]
Default output: docs/og-image.png
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 630
BG = (18, 16, 28)          # near-black, Obsidian-ish
PURPLE = (124, 58, 237)    # #7c3aed, Obsidian signature purple
TEXT = (244, 244, 250)
MUTED = (168, 162, 190)

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
REGULAR = str(FONT_DIR / "Arial.ttf")
BOLD = str(FONT_DIR / "Arial Bold.ttf")

TITLE = "Awesome Obsidian"
SUBTITLE = "Best Obsidian plugins, themes & workflows"
TAGLINE = "Curated by use case  ·  Core-first picks  ·  Monthly new-plugin tracker"
FOOTER = "awesomedog.github.io/awesome-obsidian"


def load(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def glow(img: Image.Image, box, color: tuple, radius: int, alpha: int) -> None:
    """Paint a soft radial glow inside `box`."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse(box, fill=color + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(radius))
    img.alpha_composite(layer)


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "docs" / "og-image.png"
    img = Image.new("RGBA", (W, H), BG + (255,))
    draw = ImageDraw.Draw(img)

    # Ambient purple glows in two corners.
    glow(img, (-180, -220, 620, 420), PURPLE, 120, 150)
    glow(img, (700, 320, 1420, 900), (88, 40, 180), 140, 110)

    # Thin purple rule anchoring the left edge of the text block.
    draw.rectangle([(96, 168), (102, 322)], fill=PURPLE)

    f_title = load(BOLD, 92)
    f_sub = load(REGULAR, 46)
    f_tag = load(REGULAR, 28)
    f_foot = load(REGULAR, 24)

    draw.text((136, 158), TITLE, font=f_title, fill=TEXT)
    draw.text((136, 268), SUBTITLE, font=f_sub, fill=(214, 208, 236))
    draw.text((136, 356), TAGLINE, font=f_tag, fill=MUTED)

    # Footer with a small purple dot as a logo mark.
    draw.ellipse([(136, 512), (156, 532)], fill=PURPLE)
    draw.text((172, 510), FOOTER, font=f_foot, fill=MUTED)

    # Subtle bottom border.
    draw.rectangle([(0, H - 6), (W, H)], fill=PURPLE)

    img.convert("RGB").save(out, "PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
