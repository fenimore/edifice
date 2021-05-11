#!/usr/bin/python3
import sys
import argparse
import logging
from inky import InkyWHAT

from PIL import ImageFont
from clear import clear
from api import save_png
from draw import prepare, show as draw
from write import fit_lines, draw_lines, show as write

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Inky command")
    parser.add_argument("--clear", action="store_true", default=False)
    parser.add_argument("--draw", action="store_true", default=False)
    parser.add_argument("--weather", action="store_true", default=False)
    parser.add_argument("--write", action="store_true", default=False)
    parser.add_argument("--border", action="store_true", default=False)
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
        logging.info(f"Drawing Inky {args.filename}")
        image = prepare(inky_display, args.filename)
        draw(inky_display, image)

    if args.write:
        logging.info(f"Writing Inky lines from stdin")
        font = ImageFont.truetype(args.font, args.font_size)
        # font = ImageFont.truetype(FredokaOne, args.font_size)
        lines = fit_lines(
            "\n".join(sys.stdin.readlines()).strip(),
            font,
            inky_display.WIDTH,
            padding=args.font_padding * 2,
        )
        logging.info(f"First Line: {lines[0]}...")
        image = draw_lines(
            inky_display,
            lines, font,
            origin=(args.font_padding, args.font_padding),
        )
        write(inky_display, image)

    if args.weather:
        logging.info("Plotting weather")
        filename = args.filename or "/tmp/weather_forecast.png"
        save_png(filename)
        image = prepare(inky_display, filename)
        draw(inky_display, image)
