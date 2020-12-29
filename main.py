#!/usr/bin/env python3
from PIL import Image


def tranform(r, g, b):
    tmp = b
    b = g // 2
    g = tmp
    r = r // 2
    return r, g, b


def main():
    im = Image.open('blue-flames.jpg')
    input_pixels = im.getdata()
    output_pixels = tuple(tranform(*pixel) for pixel in input_pixels)
    im.putdata(output_pixels)
    im.save('green-flames.png')


if __name__ == '__main__':
    main()
