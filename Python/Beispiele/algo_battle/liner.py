from algorithmus import *
from arena import *

__author__ = 'Mark Weinreuter'


class Liner(Algorithmus):
    def __init__(self):
        super().__init__("HardLiner")
        self.richtung = LINKS
        self.reihe_aendern = False
        self.linker_rand = True

        self.reihen_aender_richtung = UNTEN
        if self.abstand_oben() > self.abstand_unten():
            self.reihen_aender_richtung = OBEN

    def gib_richtung(self, letzter_zustand):

        # Überprüfen, ob wir nicht mehr weiter können
        if letzter_zustand == RAND or letzter_zustand == BELEGT:

            if self.richtung_horizontal():
                self.richtung = self.reihen_aender_richtung
                self.reihe_aendern = True
            else:
                self.drehe_vertikal()
                self.reihen_aender_richtung = self.richtung

        elif self.reihe_aendern:
            self.reihe_aendern = False

            if self.linker_rand:
                self.richtung = RECHTS
            else:
                self.richtung = LINKS

            self.linker_rand = not self.linker_rand

        return self.richtung
