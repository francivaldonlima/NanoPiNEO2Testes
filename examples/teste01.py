#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-2020 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Display the Raspberry Pi logo (loads image as .png).
"""

from pathlib import Path
from demo_opts import get_device
from PIL import Image
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep


def main():
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")
    fff = Image.new(logo.mode, logo.size, (255,) * 4)

    background = Image.new("RGBA", device.size, "black")
    posn = ((device.width - logo.width) // 2, 0)

    while True:
        for angle in range(0, 360, 2):
            rot = logo.rotate(angle, resample=Image.BILINEAR)
            img = Image.composite(rot, fff, rot)
            background.paste(img, posn)
            device.display(background.convert(device.mode))


if __name__ == "__main__":
    try:
        serial = i2c(port=0, address=0x3C)
        device = ssd1306(serial, rotate=0)

        main()
    except KeyboardInterrupt:
        pass
