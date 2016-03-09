import sys

__author__ = 'Mark Weinreuter'

sys.path.append('..')
from codoGPIO import *

eingang(18)

while True:
    ist_unten = GPIO.input(18)
    if not ist_unten:
        print('Button gedrückt')
        time.sleep(0.2)
