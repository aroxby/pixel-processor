#!/usr/bin/env python3
from PIL import Image


def tranform(r, g, b):
    # if (b * 1.75 > r + g) and b > 16:
    tmp = b
    b = g // 2
    g = tmp
    r = r // 2
    return r, g, b

def main():
    im = Image.open('blue-flames.jpg')
    pixels = list(im.getdata())
    for i in range(len(pixels)):
        pixels[i] = tranform(*pixels[i])
    im.putdata(pixels)
    im.save('green-flames.png')

if __name__ == '__main__':
    main()
