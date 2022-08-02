#!/usr/bin/python3
import sys
import argparse
import logging

from inky import InkyWHAT
from PIL import ImageFont, Image

from font import FONTS
from clear import clear
from api import save_png
from palette import inky_palette
from draw import prepare
from write import fit_lines, draw_lines


def show(inky_display, image, rotate=False):
    palette_img = Image.new("P", (1, 1))
    palette_img.putpalette(inky_palette)
    inky_image = image.convert("RGB").quantize(palette=palette_img)
    if rotate:
        inky_image = inky_image.rotate(270, expand=True)
    else:
        inky_image = inky_image.rotate(180, expand=True)

    inky_display.set_image(inky_image)
    inky_display.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Inky command")
    parser.add_argument("--button", action="store_true", default=False)
    parser.add_argument("--clear", action="store_true", default=False)
    parser.add_argument("--draw", action="store_true", default=False)
    parser.add_argument("--weather", action="store_true", default=False)
    parser.add_argument("--write", action="store_true", default=False)
    parser.add_argument("--border", action="store_true", default=False)
    parser.add_argument("--rotate", action="store_true", default=False)
    parser.add_argument("--font", default="Gidole-Regular")
    parser.add_argument("--font-size", type=int, default=25)
    parser.add_argument("--font-padding", type=int, default=5)
    parser.add_argument(
        "--filename", type=str,
        help="resources/matisse.png|promenade_des_anglais.jpg"
    )
    args = parser.parse_args()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO
    )

    inky_display = InkyWHAT("black")

    if args.border:
        inky_display.set_border(inky_display.BLACK)

    if args.clear:
        logging.info("Clearing Inky")
        clear(inky_display)

    if args.draw and args.filename:
        logging.info(f"Preparing {args.filename}")
        image = prepare(inky_display, args.filename, args.rotate)
        logging.info(f"Drawing image to Inky")
        show(inky_display, image, args.rotate)

    if args.write:
        logging.info(f"Writing Inky lines from stdin")
        if args.rotate:
            max_width = inky_display.HEIGHT
        else:
            max_width = inky_display.WIDTH

        font = ImageFont.truetype(
            FONTS.get(args.font) or args.font,
            args.font_size
        )

        stdin = sys.stdin.readlines()
        lines = []
        for line in stdin:
            lines.extend(
                fit_lines(
                    line.strip(),
                    font,
                    max_width,
                    padding=args.font_padding * 2,
                )
            )

        logging.info(f'Drawing: {lines}...')
        image = draw_lines(
            inky_display,
            "\n".join(lines),
            font,
            origin=(args.font_padding, args.font_padding),
            rotate=args.rotate,
        )
        show(inky_display, image, args.rotate)

    if args.weather:
        logging.info("Plotting weather")
        filename = args.filename or "/tmp/weather_forecast.png"
        save_png(filename)
        image = prepare(inky_display, filename, args.rotate)
        draw(inky_display, image, args.rotate)
