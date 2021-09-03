#!/usr/bin/env python

import OPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(13, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(15, GPIO.IN)

#GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(13):
        print("(BOTÃO F1 LIGAD)")
        time.sleep(0.4)
    if GPIO.input(22):
        print("[BOTÃO F2 LIGADO]")
        time.sleep(0.4)
    if GPIO.input(15):
        print("{BOTÃO F3 LIGADO}")
        time.sleep(0.4)


'''


_pin_map = {

DA PLACA:
    O=13
    2=22
    3=15
        # Physical pin to actual GPIO pin
            BOARD: {
                    3: 12,
                    5: 11,
                    7: 6,
                    8: 198,
                   10: 199,
                   11: 1,
                   12: 7,
                   13: 0,
                   15: 3,
                   16: 19,
                   18: 18,
                   19: 15,
                                                                                                                    21: 16,
                                                                                                                            22: 2,
                                                                                                                                    23: 14,
                                                                                                                                            24: 13,
                                                                                                                                                    26: 10
                                                                                                                                                        },
                                                                                                                                                        '''
