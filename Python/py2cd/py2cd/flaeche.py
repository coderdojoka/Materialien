__author__ = 'Mark Weinreuter'

import pygame

from py2cd.objekte import Zeichenbar


def neue_pygame_flaeche(breite, hoehe, alpha=False):
    """
    Erstellt einen neues pygame.Surface Objekt, das intern zum Zeichnen verwendet wird.
    :param breite:
    :type breite: int
    :param hoehe:
    :type hoehe: int
    :param alpha:
    :type alpha: bool
    :return:
    :rtype:pygame.Surface
    """
    if alpha:
        flaeche = pygame.Surface([breite, hoehe], pygame.SRCALPHA, 32)
        """:type:pygame.Surface"""
        flaeche.convert_alpha()
    else:
        flaeche = pygame.Surface([breite, hoehe])

    return flaeche


class ZeichenFlaeche(Zeichenbar):
    """
    Eine Fläche auf der gezeichnet werden kann. Es können z.B. Rechtecke oder Bilder gezeichnet werden.
    """

    def __init__(self, x, y, pygame_flaeche, farbe=(0, 0, 0, 0), eltern_flaeche=None):
        """
        Eine neue Zeichenfläche
        :param x:
        :type x: float
        :param y:
        :type y: float
        :param pygame_flaeche:
        :type pygame_flaeche: pygame.Surface
        :param eltern_flaeche:
        :type eltern_flaeche:
        :param farbe:
        :type farbe: tuple[int]
        :return:
        :rtype:
        """

        self._zeichenbareObjekte = []
        """
        Liste aller ZeichenbarenObjekte, die auf dieser Fläche gezeichnet werden
        :type: list[ZeichenbaresObjekt]
        """

        self.pyg_flaeche = pygame_flaeche
        """
        Die eigentliche pygame Zeichenfläche auf der gezeichnet wird.
        :type:pygame.Surface
        """

        super().__init__(x, y, pygame_flaeche.get_width(),
                         pygame_flaeche.get_height(), farbe, eltern_flaeche=eltern_flaeche)

    def fuege_hinzu(self, objekt):
        """
        Fügt ein zeichenbares Objekt zur Liste hinzu, d.h. es wird in jedem Update gezeichnet.
        :param objekt: das zeichenbare Objekt
        :type objekt:Zeichenbar
        :return:
        :rtype:
        """
        if not issubclass(objekt.__class__, Zeichenbar):
            raise AttributeError("Objekt muss von ZeichenbaresObjekt erben!")

        # falls das Objekt bereits registeriert ist, entferne es
        if objekt._eltern_flaeche is not None:
            objekt._eltern_flaeche.entferne(objekt)

        # setzt die neue Elternfläche
        objekt._eltern_flaeche = self
        # Zur Liste von Objekten hinzufügen
        self._zeichenbareObjekte.append(objekt)

    def entferne(self, objekt):
        """
        Löscht das übergebene Objekt von dieser Zeichenfläche, falls es vorhanden ist
        :param objekt:
        :type objekt:
        :return:
        :rtype:
        """
        if objekt in self._zeichenbareObjekte:
            self._zeichenbareObjekte.remove(objekt)
            objekt._eltern_flaeche = None

    def zeichne_alles(self):

        if self.farbe is not None:
            self.pyg_flaeche.fill(self.farbe)

        # zeichne alle
        for zb in self._zeichenbareObjekte:
            zb.zeichne()

    def render(self, pyg_zeichen_flaeche):
        self.zeichne_alles()
        return pyg_zeichen_flaeche.blit(self.pyg_flaeche, (self.x, self.y))

    def setze_farbmaske(self, farbe):
        self.pyg_flaeche.set_colorkey(farbe)

    def lese_farbmaske(self):
        return self.pyg_flaeche.get_colorkey()
