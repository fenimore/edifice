from palette import inky_palette

from PIL import Image


def resize(image, max_width, max_height):
    """
    resize an image so that it's longest dimension is somewhere in the
    WIDTHxHEIGHT window, for further cropping down the line
    """
    width, height = image.size

    if width > height:
        new_width = int(float(width) / height * max_height)
        new_height = max_height
    else:
        new_width = max_width
        new_height = int(float(height) / width * max_width)

    return image.resize((new_width, new_height), resample=Image.LANCZOS)


def crop(image, max_width, max_height):
    """
    crop an image to WIDTHxHEIGHT in the center of
    whatever space is available in the image
    """
    width, height = image.size
    # we want a center crop, so we need to start the crop half the difference
    # of the widths from the left edge, and half the difference of the
    # heights from the top edge
    left = abs(width - max_width) / 2
    top = abs(height - max_height) / 2
    right = max_width + left
    bottom = max_height + top

    return image.crop((left, top, right, bottom))


def show(inky_display, image):
    palette_img = Image.new("P", (1, 1))
    palette_img.putpalette(inky_palette)
    inky_image = image.convert("RGB").quantize(palette=palette_img)
    # rotate image if necessary due to power cord
    # img = img.rotate(180, expand=True)
    inky_display.set_image(inky_image)
    inky_display.show()


def prepare(inky_display, filename):
    image = Image.open(filename)
    resized_image = resize(image, inky_display.WIDTH, inky_display.HEIGHT)
    cropped_image = crop(resized_image, inky_display.WIDTH, inky_display.HEIGHT)
    return cropped_image

if __name__ == '__main__':
    import argparse
    from inky import InkyWHAT
    from clear import clear
    parser = argparse.ArgumentParser(description="Draw image on inky")
    parser.add_argument("--filename", type=str)
    parser.add_argument("--clear", action="store_true", default=False)
    args = parser.parse_args()

    inky_display = InkyWHAT("black")
    if args.clear:
        clear(inky_display)

    image = prepare(inky_display, args.filename)
    show(inky_display, image)
