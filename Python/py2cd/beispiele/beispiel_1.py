import sys
sys.path.append('..')

from py2cd.poly import Linien, Polygon
from py2cd.spiel import Spiel
from py2cd.text import Schrift, Text
from py2cd.rechteck import Rechteck
from py2cd.farben import *
from py2cd.flaeche import ZeichenFlaeche

__author__ = 'Mark Weinreuter'

def aktualisiere(dt):
    # t.aendere_position(0, 1)

    print(p.x, p.x_intern)
    print(p.y, p.y_intern)

    p.aendere_position(1, -1)
    p_box.aendere_position(1, -1)
    r.aendere_position(.1, .1)
    #flaeche.aendere_position(1, .1)
    pass


Spiel.init(300, 300, "Hallo Welt", aktualisiere)
zf = Spiel.lese_zeichen_flaeche()
flaeche = ZeichenFlaeche( ZeichenFlaeche.neue_pygame_flaeche(250, 250, False),  GELB)
zf.fuege_hinzu(flaeche)

p = Polygon([(20, 20), (10, 40), (40, 50), (50, 20)])
l = Linien([(300, 20), (400, 40), (50, 200)], True)
r = Rechteck(0,0, 40, 40, BLAU)

schrift = Schrift(20)
t = Text("Hallo Welt", 200, 0, schrift, BLAU, ROT)

p_box = Rechteck(p.dimension.x, p.dimension.y, p.dimension.breite, p.dimension.hoehe, GRUEN)
# p_box = Rechteck(l.dimension.x, l.dimension.y, l.dimension.breite, l.dimension.hoehe, GRUEN)


flaeche.zentriere()
flaeche.fuege_hinzu(r)
t.zentriere()

Spiel.starten()