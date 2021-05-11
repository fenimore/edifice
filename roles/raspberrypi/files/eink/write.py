from typing import List, Tuple
import argparse
import logging

from palette import inky_palette
from clear import clear

from inky import InkyWHAT
from PIL import (
    Image,
    ImageDraw,
    ImageFont,
)


def fit_lines(text: str, font: ImageFont, max_width: int, padding: int = 0):
    """
    Split text into lines which fit the Inky width
    using a given ImageFont font.
    """
    w, _  = font.getsize(text)
    if w <= max_width:
        return [text]

    words = text.split(" ")
    lines = []
    current_line = words.pop(0)
    for word in words:
        w, _  = font.getsize(f"{current_line} {word}")
        if w + padding > max_width:
            lines.append(current_line)
            current_line = f"{word} "
            continue
        else:
            current_line += f" {word}"

    return lines


def draw_lines(
        inky_display: InkyWHAT,
        lines: List[str],
        font: ImageFont,
        origin: Tuple[int, int] = (0, 0),
        rotate: bool = False,
):
    """
    You must include file_lines so I can align the padding/origins
    """
    font_height = font.getsize("ABCD ")[1]

    origin_x, origin_y = origin

    image = Image.new(
        "RGB",
        (inky_display.WIDTH, inky_display.HEIGHT),
        (255, 255, 255),
    )
    # image.rotate(180, expand=True)
    draw = ImageDraw.Draw(image)
    draw.multiline_text(
        (origin_x, origin_y),
        "\n".join(lines),
        font=font,
        fill=(0, 0, 0),
    )
    return image


def show(inky_display, image):
    palette_img = Image.new("P", (1, 1))
    palette_img.putpalette(inky_palette)
    inky_image = image.convert("RGB").quantize(palette=palette_img)
    # rotate image if necessary due to power cord
    # img = img.rotate(180, expand=True)
    inky_display.set_image(inky_image)
    inky_display.show()


if __name__ == "__main__":
    import argparse
    from font_fredoka_one import FredokaOne

    parser = argparse.ArgumentParser(description="Write text to inky")
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--font-size", type=int, default=26)
    parser.add_argument("--clear", action="store_true", default=False)
    args = parser.parse_args()
    logger = logging.getLogger("eink")
    logger.setLevel("INFO")

    inky_display = InkyWHAT("black")
    if args.clear:
        logger.info("Clearing Display")
        clear(inky_display)
        exit(0)

    font = ImageFont.truetype(FredokaOne, args.font_size)
    text = "abcd efgh "  * args.count

    lines = fit_lines(text, font, inky_display.WIDTH)
    image = draw_lines(inky_display, lines, font, origin=(15, 15))
    show(inky_display, image)
