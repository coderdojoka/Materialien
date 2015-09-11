__author__ = 'Mark Weinreuter'

import pygame

from py2cd.objekte import ZeichenbaresElement


class Kreis(ZeichenbaresElement):
    """
    Ein Rechteck, das angezeigt werden kann.
    """

    def render(self, pyg_zeichen_flaeche):
        # Mitte verschieben, damit x,y immer der linke Rand ist
        pygame.draw.circle(pyg_zeichen_flaeche, self.farbe,
                           (int(self.x + self.radius), int(self.y + self.radius)), self.radius, self.dicke)

    def __init__(self, x, y, radius, farbe=(0, 0, 0), dicke=0, eltern_flaeche=None):
        """
        Erstellt ein neues Rechteck mit den gegebenen Maßen.
        :param x:
        :type x: float
        :param y:
        :type y: float
        :param radius:
        :type radius: float
        :param eltern_flaeche:
        :type eltern_flaeche: py2cd.flaeche.ZeichenFlaeche
        :param farbe:
        :type farbe: tuple[inŧ]
        :param dicke:
        :type dicke: int
        :return:
        :rtype:
        """
        super().__init__(x, y, radius * 2, radius * 2, farbe, eltern_flaeche)
        self.radius = radius
        self.dicke = dicke
