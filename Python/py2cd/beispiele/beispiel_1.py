__author__ = 'Mark Weinreuter'

from py2cd.poly import Linien, Polygon
from py2cd.spiel import Spiel
from py2cd.text import Schrift, Text
from py2cd.rechteck import Rechteck
from py2cd.farben import *
from py2cd.flaeche import ZeichenFlaeche, neue_pygame_flaeche


def aktualisiere(dt):
    l.aendere_position(1, -1)
    p_box.aendere_position(1, -1)
    r.aendere_position(.1, .1)


Spiel.init(300, 300, "Hallo Welt", aktualisiere)
zf = Spiel.gib_zeichen_flaeche()
flaeche = ZeichenFlaeche(0, 0, neue_pygame_flaeche(300, 300, True),  (0, 0, 0, 0), zf)

p = Polygon([(20, 200), (10, 240), (40, 250), (50, 220)], ROT)
l = Linien([(300, 20), (400, 40), (50, 200)], geschlossen=True)
r = Rechteck(0, 0, 40, 40, BLAU)

schrift = Schrift(20)
t = Text("Hallo Welt", 200, 0, schrift,  BLAU, ROT)

p_box = Rechteck(p.x, p.y, p.breite, p.hoehe,  ROT)
p_box = Rechteck(l.x, l.y, l.breite, l.hoehe, (255, 0, 0, 120))

flaeche.zentriere()
flaeche.fuege_hinzu(p_box)
t.zentriere()

Spiel.starten()
