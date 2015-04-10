import py2cd

__author__ = 'Mark Weinreuter'

import pygame
from pygame.locals import *
from py2cd.flaeche import ZeichenFlaeche
import sys


class Spiel:
    breite = 640
    """:type: int"""
    hoehe = 480
    """:type: int"""
    fps = 30
    """:type: float """

    haupt_flaeche = None
    """:type: None|py2cd.zeichen_flaeche.ZeichenFlaeche """

    _tasten = {}
    """:type: dict[int, callable] """

    _clock = pygame.time.Clock()
    """:type: pygame.time.Clock"""

    _aktualisiere = None
    """ :type: None|(float) -> None"""

    zeit_unterschied_ms = 0
    """:type: float """

    _mausBewegt = None
    """ :type: callable|None """

    _mausTasteGedrueckt = None
    """ :type: callable|None """

    _mausTasteLosgelassen = None
    """ :type: callable|None """

    @staticmethod
    def init(breite=640, hoehe=480, titel="Python FTW", aktualisierungs_funktion=lambda zeit: None):
        """
        Initialisiert das Spiel.
        HINWEIS: Das Spiel muss! als Erstes initialisiert werden
        :param breite: die Fensterbreite
        :type breite: int
        :param hoehe: die Fensterhöhe
        :type hoehe: int
        :param titel: Der Fenstertitel
        :type titel: str
        :param aktualisierungs_funktion: die Aktualisierungsfunktion, die bei jedem Neuzeichnen aufgerufen wird (fps mal pro sekunde)
        :type aktualisierungs_funktion: (float) ->None
        :return:
        :rtype:
        """
        pygame.init()  # init pygame und so :D

        # die spiel schleife
        Spiel._aktualisiere = aktualisierungs_funktion
        Spiel.breite = breite
        Spiel.hoehe = hoehe

        # die Hauptzeichenfläche des Spiels!
        Spiel.haupt_flaeche = ZeichenFlaeche(pygame.display.set_mode((breite, hoehe)), (255, 255, 255))

        # Fenstertitel
        Spiel.setze_fenster_titel(titel)

        # setze ESC handler um das Fenster zu schließen
        Spiel.registriere_taste_gedrueckt(K_ESCAPE, lambda down, y: Spiel.beenden())

    @staticmethod
    def beenden():
        pygame.quit()
        sys.exit()

    @staticmethod
    def starten():
        """
        Startet das Spiel. Hinweis, diese Funktion blockiert und kehrt nie zurück!
        :return:
        :rtype:
        """
        Spiel._clock.tick(Spiel.fps)  # erster tick für _zeitUnterschiedMs

        while True:  # spiel schleife

            for event in pygame.event.get():  # wir gehen alle events durch
                if event.type == QUIT:
                    Spiel.beenden()

                elif event.type == MOUSEMOTION:
                    if Spiel._mausBewegt:
                        Spiel._mausBewegt(event)

                elif event.type == MOUSEBUTTONDOWN:
                    if Spiel._mausTasteGedrueckt:
                        Spiel._mausTasteGedrueckt(event)

                elif event.type == MOUSEBUTTONUP:
                    if Spiel._mausTasteLosgelassen:
                        Spiel._mausTasteLosgelassen(event)

                elif event.type == KEYUP:
                    if event.key in Spiel._tasten:
                        Spiel._tasten[event.key](False, event)

                elif event.type == KEYDOWN:
                    if event.key in Spiel._tasten:
                        Spiel._tasten[event.key](True, event)

            Spiel.zeit_unterschied_ms = Spiel._clock.get_time()
            Spiel._aktualisiere(Spiel.zeit_unterschied_ms / Spiel.fps)

            # zeichne alles!!!
            Spiel.haupt_flaeche.zeichne_alles()

            # muss aufgerufen werden um Änderungen anzuzeigen
            pygame.display.update()

            # lässt das Spiel mit ca. dieser fps laufen
            Spiel._clock.tick(Spiel.fps)

    @staticmethod
    def setze_fenster_titel(titel):
        # titel für das Fenster
        pygame.display.set_caption(titel)

    @staticmethod
    def registriere_taste_gedrueckt(taste, funktion):
        """
        Registriert eine Funktion, die ausgeführt wird, wenn die angegebene Taste gedrückt wird.
        :param taste: die Taste z.B. die a-Taste ist 97. Alle Tasten sind auch vordefiniert, so entspricht K_a der 'a'-Taste
        :type taste: int
        :param funktion: die Funktion
        :type funktion: (bool, object) -> None
        :return:
        :rtype:
        """
        Spiel._tasten[taste] = funktion
        pass

    @staticmethod
    def registriere_maus_bewegt(funktion):
        Spiel._mausBewegt = funktion

    @staticmethod
    def registriere_maus_losgelassen(funktion):
        Spiel._mausTasteLosgelassen = funktion

    @staticmethod
    def registriere_maus_gedrueckt(funktion):
        """
        Registriert eine Funktion, die aufgerufen wird, wenn eine Maustaste gedrückt wird.
        :param funktion:
        :type funktion: (object)->None
        :return:
        :rtype:
        """
        Spiel._mausTasteGedrueckt = funktion

    @staticmethod
    def lese_zeichen_flaeche():
        """
        Gibt die Hauptzeichenfläche des Spiels zurück. Darauf kann (muss) gezeichnet werden.
        :return:
        :rtype:py2cd.zeichen_flaeche.ZeichenFlaeche
        """
        return Spiel.haupt_flaeche

    @staticmethod
    def setze_aktualisierung(funktion):
        """
        Setzt die Funktion, die einmal pro Spiel Update-Durchlauf aufgerufen wird, in der Spiel-Objekte
        aktualisiert werden können.
        :param funktion:
        :type funktion: (float) -> None
        :return:
        :rtype:
        """
        Spiel._aktualisiere = funktion
