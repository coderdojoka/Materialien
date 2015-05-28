__author__ = 'Mark Weinreuter'

import pygame

from py2cd.objekte import ZeichenbaresElement


class Linie(ZeichenbaresElement):
    """
    Eine Linie die angezeigt werden kann.
    """

    def render(self, pyg_zeichen_flaeche):
        pygame.draw.line(pyg_zeichen_flaeche, self.farbe,
                         (self.x, self.y), self.__verschobenes_ende, self.dicke)

    def aktualisiere_end_punkt(self):
        self.__verschobenes_ende = (self.x + self.__ende[0], self.y + self.__ende[1])

    def __init__(self, start, ende, farbe=(0, 0, 0), dicke=1, eltern_flaeche=None):
        """
        Erstellt eine neue Linie zwischen den beiden gegebenen Punkten.
        :param start
        :type start: tuple[float]
        :param ende
        :type ende: tuple[float]
        :param farbe:
        :type farbe: tuple[int]
        :param dicke:
        :type dicke: int
        :return:
        :rtype:
        """

        # punkte umrechnen, so dass diese bei 0,0 beginnen, und start zu x,y Position wird
        self.__start = start
        self.__ende = (ende[0] - start[0], -(ende[1] - start[1]))
        self.dicke = dicke

        self.__verschobenes_ende = self.__ende
        """
        Internes Tupel für den Endpunkt, der aktualisiert werden muss, wenn die Position geändert wird
        :type: tuple[float]
        """

        super().__init__(start[0], start[1], self.__ende[0], self.__ende[1],
                         farbe, eltern_flaeche, position_geändert=self.aktualisiere_end_punkt)
