import pygame
import py2cd
from py2cd.objekte import ZeichenbaresObjekt
from py2cd.box import Box

__author__ = 'Mark Weinreuter'


class Rechteck(ZeichenbaresObjekt):
    """
    Ein Rechteck, das angezeigt werden kann.
    """

    def berechne_groesse(self):
        return Box(0, 0, self.breite, self.hoehe)

    def render(self, pyg_zeichen_flaeche):
        return pygame.draw.rect(pyg_zeichen_flaeche, self.farbe,
                                (self.x_intern, self.y_intern, self.breite, self.hoehe),
                                self.dicke)

    def __init__(self, x, y, breite, hoehe, farbe=(0, 0, 0), dicke=0):
        self.breite = breite
        self.hoehe = hoehe
        self.dicke = dicke

        super().__init__(farbe, py2cd.spiel.Spiel.haupt_flaeche)
        # nach init
        self.setze_position(x, y)