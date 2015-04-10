import py2cd

__author__ = 'Mark Weinreuter'

import pygame
from py2cd.box import Box
from py2cd.objekte import ZeichenbaresObjekt


class ZeichenFlaeche(ZeichenbaresObjekt):
    """
    Eine Fläche auf der gezeichnet werden kann. Es können z.B. Rechtecke oder Bilder gezeichnet werden.
    """

    def berechne_groesse(self):
        return Box(0, 0, self.breite, self.hoehe)

    def __init__(self, pygame_flaeche, farbe=None):
        self._zeichenbareObjekte = []
        self._pyg_flaeche = pygame_flaeche
        self.breite = pygame_flaeche.get_width()  # dürfen nicht nachträglich geändert werden
        self.hoehe = pygame_flaeche.get_height()
        """:type:pygame.Surface """

        super().__init__(farbe, None)

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
            img = pygame.image.load(pfad)
        except pygame.error:
            raise AttributeError("Das bild: %s konnte nicht geladen werden!" % pfad)

        # laut Doku soll convert() aufgerufen werden?!
        if alpha:
            img = img.convert_alpha()
        else:
            img = img.convert()

        return ZeichenFlaeche(img, py2cd.spiel.Spiel.haupt_flaeche)

    @staticmethod
    def neue_pygame_flaeche(breite, hoehe, alpha=False):
        """
        Erstellt einen neues pygame.Surface Objekt, das intern zum Zeichnen verwendet wird.
        :param breite:
        :type breite:
        :param hoehe:
        :type hoehe:
        :param alpha:
        :type alpha:
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

    def fuege_hinzu(self, objekt):
        """
        Fügt ein zeichenbares Objekt zur Liste hinzu, d.h. es wird in jedem Update gezeichnet.
        :param objekt: das zeichenbare Objekt
        :type objekt:ZeichenbaresObjekt
        :return:
        :rtype:
        """
        if not issubclass(objekt.__class__, ZeichenbaresObjekt):
            raise AttributeError("Objekt muss von ZeichenbaresObjekt erben!")

        # falls das objekt bereits registeriert ist, entferne es
        if objekt._eltern_flaeche is not None:
            objekt._eltern_flaeche.entferne(objekt)

        self._zeichenbareObjekte.append(objekt)
        objekt.setze_eltern_flaeche(self)

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
            objekt.setze_eltern_flaeche(None)

    def zeichne_alles(self):

        if self.farbe is not None:
            self._pyg_flaeche.fill(self.farbe)

        # zeichne alle
        for zb in self._zeichenbareObjekte:
            zb.render(self._pyg_flaeche)

    def render(self, pyg_zeichen_flaeche):
        self.zeichne_alles()
        blubb = self.y_intern
        return pyg_zeichen_flaeche.blit(self._pyg_flaeche, (self.x_intern, self.y_intern))

    def setze_farbmaske(self, farbe):
        self._pyg_flaeche.set_colorkey(farbe)

    def lese_farbmaske(self):
        return self._pyg_flaeche.get_colorkey()