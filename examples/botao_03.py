#!/usr/bin/env python

import OPi.GPIO as GPIO
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

from pathlib import Path
from PIL import ImageFont, Image
from time import sleep


GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(13, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(15, GPIO.IN)



serial = i2c(port=0, address=0x3C)
device = ssd1306(serial, rotate=0)
#----------------#
# tela inicial   #
#----------------#

img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
logo = Image.open(img_path).convert("RGBA")
fff = Image.new(logo.mode, logo.size, (255,) * 4)

background = Image.new("RGBA", device.size, "white")
posn = ((device.width - logo.width) // 2, 0)
rot = logo.rotate(0, resample=Image.BILINEAR)
img = Image.composite(rot, fff, rot)
background.paste(img, posn)
device.display(background.convert(device.mode))
time.sleep(5)

#-----------------------
#----------------------
#---------------------

def make_font(name, size):
    font_path = str(Path(__file__).resolve().parent.joinpath('fonts', name))
    return ImageFont.truetype(font_path, size)

largura=(device.width) / 2
altura=(device.height) / 2
font1 = make_font("code2000.ttf", 12)
font2 = make_font("code2000.ttf", 35)
#with canvas(device, dither=True) as draw:
#    draw.rectangle((0,0,10,10), fill="white")


while True:
    if GPIO.input(13):
        print("(BOTÃO F1 LIGAD)")
        with canvas(device, dither=False) as draw:
            draw.rectangle((0,0,128,24), fill="white")
            draw.text((5, 5), "(BOTÃO F1 LIGADO)",font=font1,fill="black")
            draw.text((largura-25,altura-10), "(F1)",font=font2,fill="white")
        time.sleep(0.4)
    if GPIO.input(22):
        print("[BOTÃO F2 LIGADO]")
        with canvas(device, dither=False) as draw:
            draw.text((5, 5), "(BOTÃO F2 LIGADO)",font=font1,fill="white")
            draw.text((largura-25,altura-10), "(F2)",font=font2,fill="white")
        time.sleep(0.4)
    if GPIO.input(15):
        print("{BOTÃO F3 LIGADO}")
        with canvas(device) as draw:
            draw.text((5, 5), "(BOTÃO F3 LIGADO)",font=font1,fill="white")
            draw.text((largura-25,altura-10), "(F3)",font=font2,fill="white")
        time.sleep(0.4)
    if GPIO.input(15) and GPIO.input(22):
        print("{DOIS BOTÃO")
        with canvas(device) as draw:
            draw.text((5, 5), "(DOIS BOTÃO)",font=font1,fill="white")
            draw.text((largura-25,altura-10), "(F2F3)",font=font2,fill="white")
            draw.rectangle((10,10,10,10), fill="black")
        time.sleep(0.4)
