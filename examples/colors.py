#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-2020 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Color rendering demo.
"""

import math
import time
import random
from pathlib import Path
from demo_opts import get_device
from luma.core.render import canvas
from PIL import Image

from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from luma.core.interface.serial import i2c

def main():
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'balloon.png'))
    balloon = Image.open(img_path) \
        .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
        .convert(device.mode)

    while True:
        # Image display
        device.display(balloon)
        time.sleep(5)

        # Cycle through some primary colours
        for color in ["black", "white", "red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
            with canvas(device, dither=True) as draw:
                draw.rectangle(device.bounding_box, fill=color)
                size = draw.textsize(color)
                left = (device.width - size[0]) // 2
                top = (device.height - size[1]) // 2
                right = left + size[0]
                bottom = top + size[1]
                draw.rectangle((left - 1, top, right, bottom), fill="black")
                draw.text((left, top), text=color, fill="white")

            time.sleep(3)

        # Rainbow
        w = 4
        with canvas(device, dither=True) as draw:
            for i in range(device.width // w):
                r = int(math.sin(0.3 * i + 0) * 127) + 128
                g = int(math.sin(0.3 * i + 2) * 127) + 128
                b = int(math.sin(0.3 * i + 4) * 127) + 128
                rgb = (r << 16) | (g << 8) | b
                draw.rectangle((i * w, 0, (i + 1) * w, device.height), fill=rgb)

            size = draw.textsize("rainbow")
            left = (device.width - size[0]) // 2
            top = (device.height - size[1]) // 2
            right = left + size[0]
            bottom = top + size[1]
            draw.rectangle((left - 1, top, right, bottom), fill="black")
            draw.text((left, top), text="rainbow", fill="white")

        time.sleep(5)

        # Gradient
        with canvas(device, dither=True) as draw:
            for y in range(device.height):
                for x in range(device.width):
                    r = int(min(x / (device.width / 256), 255))
                    g = int(min(y / (device.height / 256), 255))
                    b = 0
                    draw.point((x, y), fill=(r, g, b))

            size = draw.textsize("gradient")
            left = (device.width - size[0]) // 2
            top = (device.height - size[1]) // 2
            right = left + size[0]
            bottom = top + size[1]
            draw.rectangle((left - 1, top, right, bottom), fill="black")
            draw.text((left, top), text="gradient", fill="white")

        time.sleep(5)

        # Random blocks
        w = device.width // 12
        h = device.height // 8
        for _ in range(40):
            with canvas(device, dither=True) as draw:
                for x in range(12):
                    for y in range(8):
                        color = random.randint(0, 2 ** 24)
                        left = x * w
                        right = (x + 1) * w
                        top = y * h
                        bottom = (y + 1) * h
                        draw.rectangle((left, top, right - 2, bottom - 2), fill=color)

                time.sleep(0.25)


if __name__ == "__main__":
    try:
        serial = i2c(port=0, address=0x3C)
        device = ssd1306(serial, rotate=0)
        main()
    except KeyboardInterrupt:
        pass
