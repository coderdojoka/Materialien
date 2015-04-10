__author__ = 'Mark Weinreuter'

import pygame
import py2cd
from py2cd.objekte import *
from py2cd.box import *


class Polygon(ZeichenbaresObjekt):
    def __init__(self, punkte, farbe=(0, 0, 0), dicke=0):
        """
        Erstellt ein neues Polygon mit den gegebenen Eckpunkte
        :param punkte:
        :type punkte: list [int, int]
        :param dicke:
        :type dicke: int
        :param farbe:
        :type farbe: tuple [int]
        :return:
        :rtype:
        """

        x = punkte[0][0]  # x und y speichern und später setzen
        y = punkte[0][1]
        self.punkte = [(p[0] - punkte[0][0], -(p[1] - punkte[0][1])) for p in punkte]
        """
        Die Punkteliste. Die Punkte werden so umgerechnet, dass sie relativ zum Startpunkt sind.
        :type: list[int, int]
        """
        self._verschobene_punkte = punkte
        """ Interne Liste mit x,y Verschiebung """

        self.dicke = dicke
        """ Die Dicke mit der das Polygon gezeichnet wird, 0=> gefüllt
        :type: int
        """

        # parent init()
        super().__init__(farbe, py2cd.spiel.Spiel.haupt_flaeche)


        # position jetzt setzen
        self.x_intern = x
        self.y_intern = y - self.dimension.hoehe  # cheat um für den setter zu überlisten :D

        self.position_geaendert = self._aktualisiere_punkte  # aktualisierungsfunktion bei punktänderung
        self._aktualisiere_punkte()

    def render(self, pyg_zeichen_flaeche):
        return pygame.draw.polygon(pyg_zeichen_flaeche, self.farbe, self._verschobene_punkte, self.dicke)

    def _aktualisiere_punkte(self):
        self._verschobene_punkte = [(p[0] + self.x_intern, p[1] + self.y_intern) for p in self.punkte]

    def berechne_groesse(self):
        return umgebendes_rechteck(self.punkte, self._eltern_flaeche.dimension.hoehe)


class Linien(Polygon):
    """
    Mehrere Linie zwischen den angegebenen Punkten. Alle Punkte werden der Reihe nach verbunden. 1 -> 2 -> 3...
    """

    def berechne_groesse(self):
        return umgebendes_rechteck(self.punkte, self._eltern_flaeche.dimension.hoehe)

    def render(self, pyg_zeichen_flaeche):
        return pygame.draw.lines(pyg_zeichen_flaeche, self.farbe, self._geschlossen, self._verschobene_punkte,
                                 self.dicke)

    def __init__(self, punkte, geschlossen=False, farbe=(0, 0, 0), dicke=1):
        self._geschlossen = geschlossen

        super().__init__(punkte, farbe, dicke)