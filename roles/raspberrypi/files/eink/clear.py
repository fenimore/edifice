from palette import inky_palette
from PIL import Image


def clear(inky_display):
    image = Image.new(
        "RGB",
        (inky_display.WIDTH, inky_display.HEIGHT),
        (255, 255, 255),
    )
    palette_image = Image.new("P", (1, 1))
    palette_image.putpalette(inky_palette)
    inky_image = image.convert("RGB").quantize(palette=palette_image)

    inky_display.set_image(inky_image)
    inky_display.show()
