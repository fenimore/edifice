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


def fit_lines(
        text: str,
        font: ImageFont,
        max_width: int,
        padding: int = 0
) -> List[str]:
    """
    Split text into lines which fit the Inky width
    using a given ImageFont font.
    """
    width  = font.getbbox(text)[2]
    if width <= max_width:
        return [text]

    print(text)
    words = text.split(" ")
    lines = []
    current_line = words.pop(0)
    for word in words:
        width = font.getbbox(f"{current_line} {word}")[2]
        if width + padding > max_width:
            lines.append(current_line)
            current_line = f"{word} "
            continue
        else:
            current_line += f" {word}"

    lines.append(current_line)
    return lines


def draw_lines(
        inky_display: InkyWHAT,
        lines: str,
        font: ImageFont,
        origin: Tuple[int, int] = (0, 0),
        rotate: bool = False,
):
    """
    You must include file_lines so I can align the padding/origins
    """
    origin_x, origin_y = origin

    image = Image.new(
        "RGB",
        (inky_display.WIDTH, inky_display.HEIGHT),
        (255, 255, 255),
    )
    if rotate:
        image = image.rotate(270, expand=True)
    else:
        image = image.rotate(180, expand=True)


    draw = ImageDraw.Draw(image)
    draw.multiline_text(
        (origin_x, origin_y),
        lines,
        font=font,
        fill=(0, 0, 0),
    )
    return image
