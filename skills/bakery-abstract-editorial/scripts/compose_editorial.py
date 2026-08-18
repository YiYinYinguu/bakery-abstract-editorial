#!/usr/bin/env python3
"""Compose an unchanged source photo with an approved abstract panel."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageColor, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a vertical editorial PNG by scaling/cropping the original photo "
            "and joining it directly to an approved lower panel."
        )
    )
    parser.add_argument("--source", required=True, type=Path, help="Original photo")
    parser.add_argument("--panel", required=True, type=Path, help="Approved panel image")
    parser.add_argument("--out", required=True, type=Path, help="Output PNG")
    parser.add_argument("--width", type=int, default=1024, help="Canvas width")
    parser.add_argument("--height", type=int, default=1536, help="Canvas height")
    parser.add_argument(
        "--photo-height", type=int, default=850, help="Upper photo region height"
    )
    parser.add_argument(
        "--photo-anchor-x", type=float, default=0.5, help="Photo crop anchor, 0..1"
    )
    parser.add_argument(
        "--photo-anchor-y", type=float, default=0.5, help="Photo crop anchor, 0..1"
    )
    parser.add_argument(
        "--panel-anchor-x", type=float, default=0.5, help="Panel crop anchor, 0..1"
    )
    parser.add_argument(
        "--panel-anchor-y", type=float, default=0.5, help="Panel crop anchor, 0..1"
    )
    parser.add_argument(
        "--panel-fit",
        choices=("cover", "contain"),
        default="cover",
        help="Fit approved panel into the lower region",
    )
    parser.add_argument(
        "--ivory", default="#F3F0E8", help="Background used by panel contain mode"
    )
    return parser.parse_args()


def validate(args: argparse.Namespace) -> None:
    if args.width <= 0 or args.height <= 0:
        raise SystemExit("width and height must be positive")
    if not 0 < args.photo_height < args.height:
        raise SystemExit("photo-height must be between 1 and height - 1")
    for value, label in (
        (args.photo_anchor_x, "photo-anchor-x"),
        (args.photo_anchor_y, "photo-anchor-y"),
        (args.panel_anchor_x, "panel-anchor-x"),
        (args.panel_anchor_y, "panel-anchor-y"),
    ):
        if not 0 <= value <= 1:
            raise SystemExit(f"{label} must be between 0 and 1")
    if not args.source.is_file():
        raise SystemExit(f"source not found: {args.source}")
    if not args.panel.is_file():
        raise SystemExit(f"panel not found: {args.panel}")


def cover(
    image: Image.Image, size: tuple[int, int], anchor: tuple[float, float]
) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    overflow_x = resized.width - target_w
    overflow_y = resized.height - target_h
    left = round(overflow_x * anchor[0])
    top = round(overflow_y * anchor[1])
    return resized.crop((left, top, left + target_w, top + target_h))


def contain(image: Image.Image, size: tuple[int, int], ivory: str) -> Image.Image:
    fitted = ImageOps.contain(image, size, Image.Resampling.LANCZOS)
    background = Image.new("RGB", size, ImageColor.getrgb(ivory))
    left = (size[0] - fitted.width) // 2
    top = (size[1] - fitted.height) // 2
    background.paste(fitted, (left, top))
    return background


def load_rgb(path: Path) -> Image.Image:
    with Image.open(path) as opened:
        return ImageOps.exif_transpose(opened).convert("RGB")


def main() -> None:
    args = parse_args()
    validate(args)

    panel_height = args.height - args.photo_height
    photo = cover(
        load_rgb(args.source),
        (args.width, args.photo_height),
        (args.photo_anchor_x, args.photo_anchor_y),
    )
    panel_source = load_rgb(args.panel)
    if panel_source.width <= panel_source.height:
        raise SystemExit(
            "panel must be a landscape lower-panel image, not a complete vertical poster"
        )
    if args.panel_fit == "cover":
        panel = cover(
            panel_source,
            (args.width, panel_height),
            (args.panel_anchor_x, args.panel_anchor_y),
        )
    else:
        panel = contain(panel_source, (args.width, panel_height), args.ivory)

    canvas = Image.new("RGB", (args.width, args.height), ImageColor.getrgb(args.ivory))
    canvas.paste(photo, (0, 0))
    canvas.paste(panel, (0, args.photo_height))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.out, format="PNG", optimize=True)
    print(
        f"saved {args.out} ({args.width}x{args.height}; "
        f"photo={args.photo_height}, panel={panel_height})"
    )


if __name__ == "__main__":
    main()
