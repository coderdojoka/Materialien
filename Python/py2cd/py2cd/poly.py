__author__ = 'Mark Weinreuter'

import pygame

from py2cd.objekte import *
from py2cd.box import *


class Polygon(ZeichenbaresObjekt):

    def __init__(self, punkte, eltern_flaeche, farbe=(0, 0, 0), dicke=0):
        """
        Erstellt ein neues Polygon mit den gegebenen Eckpunkte
        :param punkte:
        :type: punkte: list [int, int]
        :param eltern_flaeche:
        :type eltern_flaeche: py2cd.flaeche.ZeichenFlaeche
        :param farbe:
        :type: farbe: tuple [int]
        :param dicke:
        :type: dicke: int
        :return:
        :rtype:
        """

        # Konvertiere die Punkte so, das der erset Punkt bei (0,0) liegt und der erste Punkt wird als x,y-Koordinaten
        x = punkte[0][0]
        y = punkte[0][1]
        self._punkte = [(p[0] - x, (p[1] - y)) for p in punkte]
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

        # berechne die Größe
        dim = berechne_groesse(self._punkte)

        # Eltern init()
        super().__init__(x, y, dim[0], dim[1], eltern_flaeche, farbe, self._aktualisiere_punkte)

    def render(self, pyg_zeichen_flaeche):
        return pygame.draw.polygon(pyg_zeichen_flaeche, self.farbe, self._verschobene_punkte, self.dicke)

    def _aktualisiere_punkte(self):
        self._verschobene_punkte = [(p[0] + self.x, p[1] + self.y) for p in self._punkte]


class Linien(Polygon):
    """
    Mehrere Linie zwischen den angegebenen Punkten. Alle Punkte werden der Reihe nach verbunden. 1 -> 2 -> 3...
    """

    def render(self, pyg_zeichen_flaeche):
        return pygame.draw.lines(pyg_zeichen_flaeche, self.farbe, self._geschlossen, self._verschobene_punkte,
                                 self.dicke)

    def __init__(self, punkte, eltern_flaeche, geschlossen=False, farbe=(0, 0, 0), dicke=1):
        """
        Erstellt ein neues Liniensystem aus den gegebenen Punkten
        :param punkte:
        :type punkte: list[tuple[float]]
        :param eltern_flaeche:
        :type eltern_flaeche: py2cd.flaeche.ZeichenFlaeche
        :param geschlossen:
        :type geschlossen: bool
        :param farbe:
        :type farbe: tuple[int]
        :param dicke:
        :type dicke: int
        :return:
        :rtype:
        """
        self._geschlossen = geschlossen

        super().__init__(punkte, eltern_flaeche, farbe, dicke)