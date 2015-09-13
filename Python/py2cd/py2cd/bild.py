__author__ = 'Mark Weinreuter'

import pygame

from py2cd.objekte import ZeichenbaresElement


class Bild(ZeichenbaresElement):
    def render(self, pyg_zeichen_flaeche):
        pyg_zeichen_flaeche.blit(self.__pygame_bild, (self.x, self.y))

    def __init__(self, x, y, bild, eltern_flaeche=None, position_geaendert=lambda: None):
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
            self.__pygame_bild = BildSpeicher.gib_pygame_flaeche(bild)
        elif isinstance(bild, pygame.Surface):
            self.__pygame_bild = bild
        else:
            raise ValueError("Bitte Schlüssel des Bildes im Bildspeicher angeben.")

        super().__init__(x, y, self.__pygame_bild.get_width(), self.__pygame_bild.get_height(), farbe=None,
                         eltern_flaeche=eltern_flaeche,
                         position_geaendert=position_geaendert)


class BildWechsler(ZeichenbaresElement):
    def __init__(self, x, y, bilder_namen_liste, eltern_flaeche=None, position_geaendert=lambda: None):
        self.__pygame_bilder = []
        self.aktuelles_bild = 0
        self.zeige_erstes_bild = lambda: self.zeige_bild(0)
        self.zeige_letztes_bild = lambda: self.zeige_bild(-1)

        if len(bilder_namen_liste) == 0:
            raise ValueError("Bilder Liste darf nicht leer sein!")

        groesse = (0, 0)
        # alle Bilder laden und Größe ermittlen
        for name in bilder_namen_liste:
            pg_bild = BildSpeicher.gib_pygame_flaeche(name)
            groesse = max(groesse[0], pg_bild.get_width()), max(groesse[1], pg_bild.get_height())

            self.__pygame_bilder.append(pg_bild)


        self.anzahl_bilder = len(self.__pygame_bilder)

        super().__init__(x, y, *groesse, farbe=None, eltern_flaeche=eltern_flaeche,
                         position_geaendert=position_geaendert)

    def zeige_bild(self, index):
        if index < 0:
            index = 0
        elif index >= self.anzahl_bilder:
            index = self.anzahl_bilder - 1

        self.aktuelles_bild = index

    def naechstes_bild(self):
        if self.aktuelles_bild == self.anzahl_bilder - 1:
            self.aktuelles_bild = 0
        else:
            self.aktuelles_bild += 1

    def vorheriges_bild(self):
        if self.aktuelles_bild == 0:
            self.aktuelles_bild = self.anzahl_bilder - 1
        else:
            self.aktuelles_bild -= 1

    def render(self, pyg_zeichen_flaeche):
        bild = self.__pygame_bilder[self.aktuelles_bild]
        # Bild zentriert zeichnen
        pyg_zeichen_flaeche.blit(bild, (self.x +(self.breite-bild.get_width())/2, self.y+(self.hoehe-bild.get_height())/2))


class BildSpeicher:
    __alle_bilder = {}

    @classmethod
    def ist_bild_vorhanden(cls, schluessel):
        return schluessel in cls.__alle_bilder

    @staticmethod
    def lade_bild_aus_datei(pfad, alpha=True):
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

    @classmethod
    def lade_bild(cls, schluessel, pfad, alpha=True):
        bild = cls.lade_bild_aus_datei(pfad, alpha)
        cls.__alle_bilder[schluessel] = bild
        return bild

    @classmethod
    def gib_bild(cls, schluessel, x=0, y=0):
        if schluessel not in cls.__alle_bilder:
            raise ValueError("Bild %s nicht im BildSpeicher vorhanden. Füge es zuerst hinzu!" % schluessel)

        return Bild(x, y, cls.__alle_bilder[schluessel])

    @classmethod
    def gib_pygame_flaeche(cls, schluessel):
        if schluessel not in cls.__alle_bilder:
            raise ValueError("%s ist nicht im BildSpeicher vorhanden. Füge es zuerst hinzu!" % schluessel)

        return cls.__alle_bilder[schluessel]
