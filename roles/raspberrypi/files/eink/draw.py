from palette import inky_palette

from PIL import Image, ImageOps


def resize(image, max_width, max_height, rotate=False):
    """
    resize an image so that it's longest dimension is somewhere in the
    WIDTHxHEIGHT window, for further cropping down the line
    """
    width, height = image.size

    if (not rotate and width > height) or (rotate and width <= height):
        new_width = int(float(width) / height * max_height)
        new_height = max_height
    elif (not rotate and width <= height) or (rotate and width > height):
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


def prepare(inky_display, filename, rotate=False):
    image = Image.open(filename)
    if rotate:
        w, h = tuple(reversed((inky_display.WIDTH, inky_display.HEIGHT)))
    else:
        w, h = (inky_display.WIDTH, inky_display.HEIGHT)

    resized_image = resize(image, w, h, rotate)
    cropped_image = crop(resized_image, w, h)
    return cropped_image
