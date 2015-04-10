__author__ = 'Mark Weinreuter'
import pygame
import py2cd
from py2cd.box import *
from py2cd.objekte import *


class Linie(ZeichenbaresObjekt):
    """
    Eine Linie die angezeigt werden kann.
    """

    def render(self, pyg_zeichen_flaeche):
        return pygame.draw.line(pyg_zeichen_flaeche, self.farbe,
                                (self.x_intern, self.y_intern),
                                (self.x_intern + self.ende[0], self.y_intern + self.ende[1]), self.dicke)

    def __init__(self, start, ende, farbe=(0, 0, 0), dicke=1):
        """

        :param start
        :type start: tuple[int]
        :param ende
        :type ende: tuple[int]
        :param farbe:
        :type farbe: tuple[int]
        :param dicke:
        :type dicke: int
        :return:
        :rtype:
        """

        # punkte umrechnen, so dass diese bei 0,0 beginnen
        self.ende = (ende[0] - start[0], -(ende[1] - start[1]))
        self.dicke = dicke

        super().__init__(farbe, py2cd.spiel.Spiel.haupt_flaeche)

        # reihenfolge!
        self.x_intern = start[0]
        self.y_intern = start[1] - self.dimension.hoehe

    def berechne_groesse(self):
        return umgebendes_rechteck([(0, 0), self.ende], self._eltern_flaeche.dimension.hoehe)

