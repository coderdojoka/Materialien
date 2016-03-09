__author__ = 'Mark Weinreuter'

from codoGPIO import *

# Schreibe hier dein Programm

print('Starte Temparaturmessung')
datei_name = "messwerte_%d.txt" % time.time()


def speichere_wert(wert):
    with open(datei_name, mode="a") as datei:
        datei.write(str(wert) + "\n")


while True:
    temp = temparatur()
    sage("Es hat:", temp, "Grad")
    speichere_wert(temp)
    warte(2)
