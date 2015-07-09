

__author__ = 'Mark Weinreuter'

import math

from py2cd.spiel import Spiel
from py2cd.farben import *
from py2cd.mathe import Plot
from py2cd.linie import Linie

Spiel.init(640, 480, "Hallo Mathe")

plot = Plot(lambda x: 0, -4, 4, SCHWARZ, 100, 100)
plot.zentriere()

yAchse = Linie((Spiel.breite / 2, Spiel.hoehe), (Spiel.breite / 2, -Spiel.hoehe),  SCHWARZ)
yAchse.zentriere()

# Sigmoid
plot = Plot(lambda x: -1 *math.cos(x) + -1 * math.sin(x), -4, 4, BLAU, 100, 100)
plot.zentriere()

plot = Plot(lambda x: -.5 * math.cos(x) + 0 * math.sin(x), -4, 4, ROT, 100, 100)
plot.zentriere()

plot = Plot(lambda x: 0 * math.cos(x) + 1 * math.sin(x), -4, 4, GRUEN, 100, 100)
plot.zentriere()

Spiel.starten()
