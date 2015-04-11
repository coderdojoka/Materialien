__author__ = 'Mark Weinreuter'

import math
import os
import sys

# wir sind in beispiele
os.chdir("../../")
sys.path.append("py2cd")

from py2cd.spiel import Spiel
from py2cd.farben import *
from py2cd.flaeche import ZeichenFlaeche, neue_pygame_flaeche
from py2cd.mathe import Plot


Spiel.init(640, 480, "Hallo Mathe")
zf = Spiel.gib_zeichen_flaeche()
flaeche = ZeichenFlaeche(0, 0, neue_pygame_flaeche(300, 300, True), zf, (0, 0, 0, 0))

# Plotet eine Sinusfunktion
plot = Plot(lambda x: math.sin(x), -12, 12, zf, vergroesserung=20)
plot.zentriere()

# Parabel :D
plot = Plot(lambda x: x ** 2, -4, 4, zf, GRUEN, 20)
plot.zentriere()

Spiel.starten()