__author__ = 'Mark Weinreuter'

import pygame

from py2cd.objekte import ZeichenbaresObjekt


class Rechteck(ZeichenbaresObjekt):
    """
    Ein Rechteck, das angezeigt werden kann.
    """

    def render(self, pyg_zeichen_flaeche):
        pygame.draw.rect(pyg_zeichen_flaeche, self.farbe,
                         (self.x, self.y, self.breite, self.hoehe),
                         self.dicke)

    def __init__(self, x, y, breite, hoehe, eltern_flaeche, farbe=(0, 0, 0), dicke=0):
        """
        Erstellt ein neues Rechteck mit den gegebenen Maßen.
        :param x:
        :type x: float
        :param y:
        :type y: float
        :param breite:
        :type breite: float
        :param hoehe:
        :type hoehe: float
        :param eltern_flaeche:
        :type eltern_flaeche: py2cd.flaeche.ZeichenFlaeche
        :param farbe:
        :type farbe: tuple[inŧ]
        :param dicke:
        :type dicke: int
        :return:
        :rtype:
        """
        super().__init__(x, y, breite, hoehe, eltern_flaeche, farbe)
        self.dicke = dicke