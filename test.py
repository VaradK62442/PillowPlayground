from PIL import Image

im = Image.open("./images/sdvIcon.png")

# attributes
print(im.format, im.size, im.mode)

# show image in image program
# im.show()

x_size, y_size = im.size

# copy subrectangle from image
box = (0, 0, int(x_size/2), y_size) # from (0, 0) to (x/2, y) i.e. left half of image
region = im.crop(box)

# process subrectangle, paste it back
region = region.transpose(Image.Transpose.ROTATE_180) # rotate left half by 180 degrees
im.paste(region, box) # replace image with transformed region

# im.show()

def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

im2 = Image.open("./images/gibby.jpg")
rolled = roll(im2, 128)

def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

merged = merge(im, rolled)
# merged.show()

im3 = Image.open("./images/jirachi.png")
r, g, b, a = im3.split()
im3 = Image.merge("RGBA", (b, g, a, r))
# im3.show()