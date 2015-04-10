__author__ = 'Mark Weinreuter'

import pygame
import py2cd
from py2cd.objekte import *
from py2cd.box import *


class Schrift():
    """
    Eine Schrift, die zum Darstellen von Text verwendet werden kann.
    """

    def __init__(self, schrift_groesse, schrift_art='freesansbold.ttf'):
        self.schrift_art = schrift_art
        self.schrift_groesse = schrift_groesse
        self._pyg_schrift = pygame.font.Font(schrift_art, schrift_groesse)

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


class Text(ZeichenbaresObjekt):
    """
    Ein Text, der angezeigt werden kann.
    """

    def render(self, pyg_zeichen_flaeche):
        return pyg_zeichen_flaeche.blit(self.schrift.render(self.text, True, self.farbe, self.hintergrund),
                                        (self.x_intern, self.y_intern))

    def __init__(self, text, x, y, schrift, farbe=(0, 0, 0), hintergrund=None):
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
        self.text = text
        self.schrift = schrift
        super().__init__(farbe, py2cd.spiel.Spiel.haupt_flaeche)
        # nach init!
        self.setze_position(x, y)

    def berechne_groesse(self):
        dim = self.schrift.berechne_groesse(self.text)
        return Box(0, 0, dim[0], dim[1])
