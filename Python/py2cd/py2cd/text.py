__author__ = 'Mark Weinreuter'

import pygame
import pygame.freetype

from py2cd.objekte import ZeichenbaresElement


class Schrift:
    """
    Eine Schrift, die zum Darstellen von Text verwendet werden kann.
    """

    def __init__(self, schrift_groesse, schrift_art=None):
        self.schrift_art = schrift_art
        self.schrift_groesse = schrift_groesse
        self._pyg_schrift = pygame.font.SysFont(schrift_art, schrift_groesse)

    def berechne_groesse(self, text):
        """
        Gibt die Größe des Textes zurück
        :param text:
        :type text:
        :return:
        :rtype:
        """
        return self._pyg_schrift.size(text)

    def render(self, text, aa, farbe, hintergrund):
        return self._pyg_schrift.render(text, aa, farbe, hintergrund)


class Text(ZeichenbaresElement):
    """
    Ein Text, der angezeigt werden kann.
    """

    def setze_text(self, text):
        self.__text = text
        dim = self.schrift.berechne_groesse(self.__text)
        self._aendere_groesse(*dim)

    def render(self, pyg_zeichen_flaeche):
        return pyg_zeichen_flaeche.blit(self.schrift.render(self.__text, True, self.farbe, self.hintergrund),
                                        (self.x, self.y))

    def __init__(self, text, x, y, schrift=Schrift(20), farbe=(0, 0, 0), hintergrund=None, eltern_flaeche=None):
        """
        Ein neuer Text an der angebenen Position
        :param text:
        :type text:str
        :param x:

        :type x: int
        :param y:
        :type y: int
        :param schrift:
        :type schrift:py2cd.text.Schrift
        :param farbe:
        :type farbe:tuple[int]
        :param hintergrund:
        :type hintergrund: tuple[int]
        :return:
        :rtype:
        """
        self.hintergrund = hintergrund
        """
        Die Hintergrundfarbe
        :type: tuple[int]
        """
        self.__text = text
        """
        Der anzuzeigende Text
        :type:str
        """
        self.schrift = schrift
        """
        Die verwendete Schrift
        :type:Schrift
        """

        # berechne Größe
        dim = self.schrift.berechne_groesse(self.__text)

        # Eltern Konstruktor
        super().__init__(x, y, dim[0], dim[1], farbe, eltern_flaeche)
