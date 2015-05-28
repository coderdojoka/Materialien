__author__ = 'Mark Weinreuter'

import pygame

from py2cd.objekte import ZeichenbaresElement


class Bild(ZeichenbaresElement):
    def render(self, pyg_zeichen_flaeche):
        pyg_zeichen_flaeche.blit(self._bild, (self.x, self.y))

    def __init__(self, x, y, bild, alpha=False):
        """

        :param x:
        :type x:
        :param y:
        :type y:
        :param bild:
        :type bild:str|pygame.Surface
        :param alpha:
        :type alpha:
        :return:
        :rtype:
        """
        if isinstance(bild, str):
            bild = Bild.lade_bild_aus_datei(bild, alpha)

        super().__init__(x, y, bild.get_width(), bild.get_height(), None)
        self._bild = bild

    @staticmethod
    def lade_bild_aus_datei(pfad, alpha=False):
        """
        Lädt das Bild aus der beschrieben Datei.
        ACHTUNG: Kann das Bild nicht geladen werden, wird ein Fehler geworfen!
        :param pfad:
        :type pfad:str
        :param alpha: Falls das Bild Transparenz unterstüzten soll
        :type alpha:bool
        :return:
        :rtype:
        """
        try:
            bild = pygame.image.load(pfad)
        except pygame.error:
            raise AttributeError("Das Bild: %s konnte nicht geladen werden!" % pfad)

        # laut Doku soll convert() aufgerufen werden?!
        if alpha:
            bild = bild.convert_alpha()
        else:
            bild = bild.convert()

        return bild
