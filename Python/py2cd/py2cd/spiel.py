__author__ = 'Mark Weinreuter'

import sys

import pygame
import pygame.freetype

from pygame.constants import *

class Spiel:
    """
    Die Hauptklasse des Spiels.
    Es muss Spiel.init() und Spiel.starten() aufgerufen werden.
    """

    _ist_aktiv = True
    breite = 640
    """
    Die Breite des Spiels (Fensters)
    :type: int"""
    hoehe = 480
    """
    Die Höhe des Spiels (Fensters)
    :type: int"""
    fps = 30
    """
    Die Anzahl der Aktualisierungen pro Sekunde ("Frames per second)
    :type: float """

    __haupt_flaeche = None
    """
    Die ZeichenFlaeche des Spiels (Fensters)
    :type: py2cd.zeichen_flaeche.ZeichenFlaeche """

    standard_flaeche = None
    """
    Die Fläche zu der Objekte standartmäßig hinzugefügt werden, falls die Elternfläche nicht explizit angegben ist.
    :type: py2cd.zeichen_flaeche.ZeichenFlaeche
    """

    _tasten = {}
    """
    Tastendruck-Funktionen werden hier gespeichert
    :type: dict[int, callable] """

    _clock = pygame.time.Clock()
    """
    Taktgeber für das Spiel um die Fps einzustellen
    :type: pygame.time.Clock"""

    __aktualisiere = None
    """
    Die Funktion, die aufgerufen wird, wenn das Spiel aktualisiert wird (fps mal).
    :type: (float) -> None
    """

    zeit_unterschied_ms = 0
    """:type: float """

    _mausBewegt = None
    """ :type: callable|None """

    _maus_taste_gedrueckt = None
    """
    Funktion die aufgerufen wird, wenn eine Taste gedrückt wurde
    :type: (object) -> None
    """

    _maus_taste_losgelassen = None
    """ :type: callable|None """

    @classmethod
    def init(cls,breite=640, hoehe=480, titel="Python Spiel", aktualisierungs_funktion=lambda zeit: None):
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

        # Versions Info
        print("Python: ", sys.version)
        print("Pygame: ", pygame.version.ver)

        # die spiel schleife
        Spiel.__aktualisiere = aktualisierungs_funktion

        # Dimension des Fensters
        Spiel.breite = breite
        Spiel.hoehe = hoehe

        # wird hier erst importiert, da sonst ein Fehler auftritt (wegen cyclischen Imports?)
        from py2cd.flaeche import ZeichenFlaeche

        # die Hauptzeichenfläche des Spiels!
        Spiel.__haupt_flaeche = ZeichenFlaeche(0, 0, pygame.display.set_mode((breite, hoehe)),
                                               (255, 255, 255))

        Spiel.standard_flaeche = Spiel.__haupt_flaeche

        # Fenstertitel
        Spiel.setze_fenster_titel(titel)

        # setze ESC handler um das Fenster zu schließen
        Spiel.registriere_taste_gedrueckt(K_ESCAPE, lambda down, y: Spiel.beenden())

    @staticmethod
    def beenden():
        """
        Beendet das Spiel und schließt das Fenster
        :return:
        :rtype:
        """
        pygame.quit()
        sys.exit()

    @staticmethod
    def starten():
        """
        Startet das Spiel. Hinweis, diese Funktion blockiert und kehrt nie zurück!
        :return:
        :rtype:
        """
        # erster tick für zeit_unterschied_ms
        Spiel._clock.tick(Spiel.fps)

        while Spiel._ist_aktiv:  # spiel schleife

            # wir gehen alle events durch
            for ereignis in pygame.event.get():

                # Fenster schließen
                if ereignis.type == QUIT:
                    Spiel.beenden()

                # Maus bewegt
                elif ereignis.type == MOUSEMOTION:
                    if Spiel._mausBewegt:
                        Spiel._mausBewegt(ereignis)

                # Maustaste gedrückt
                elif ereignis.type == MOUSEBUTTONDOWN:
                    if Spiel._maus_taste_gedrueckt:
                        Spiel._maus_taste_gedrueckt(ereignis)

                # Maustaste losgelassen
                elif ereignis.type == MOUSEBUTTONUP:
                    if Spiel._maus_taste_losgelassen:
                        Spiel._maus_taste_losgelassen(ereignis)

                # Taste losgelassen
                elif ereignis.type == KEYUP:
                    if ereignis.key in Spiel._tasten:
                        Spiel._tasten[ereignis.key](False, ereignis)

                # Taste gedrückt
                elif ereignis.type == KEYDOWN:
                    if ereignis.key in Spiel._tasten:
                        Spiel._tasten[ereignis.key](True, ereignis)

            Spiel.zeit_unterschied_ms = Spiel._clock.get_time()
            Spiel.__aktualisiere(Spiel.zeit_unterschied_ms / Spiel.fps)

            # zeichne alles!!!
            Spiel.__haupt_flaeche.zeichne_alles()

            # muss aufgerufen werden um Änderungen anzuzeigen
            pygame.display.update()

            # lässt das Spiel mit ca. dieser fps laufen
            Spiel._clock.tick(Spiel.fps)

    @staticmethod
    def setze_fenster_titel(titel):
        """
        Setzt den Titel für das Fenster
        :param titel:
        :type titel: str
        :return:
        :rtype:
        """
        pygame.display.set_caption(titel)

    @staticmethod
    def registriere_taste_gedrueckt(taste, funktion):
        """
        Registriert eine Funktion, die ausgeführt wird, wenn die angegebene Taste gedrückt wird.
        :param taste: die Taste z.B. die a-Taste ist 97. Alle Tasten sind vordefiniert, so entspricht K_a der 'a'-Taste
        :type taste: int
        :param funktion: Die Funktion die aufgerufen wird. Sie muss 2 Parameter akzeptieren, der
        Erste gibt an, ob die Taste gedrückt oder losgelassen ist und der Zweite ist das Event Objekt
        :type funktion: (bool, object) -> None
        :return:
        :rtype:
        """
        Spiel._tasten[taste] = funktion
        pass

    @staticmethod
    def registriere_maus_bewegt(funktion):
        """
        Registriert eine Funktion, die ausgeführt wird, wenn eine Maus-Taste gedrückt wird.
        Wenn die Funktion aufgerufen wird, wird ihr ein Objekt übergeben, das so aufgebaut ist:
        {
            button: 1-3 # welche Taste: 1 = Links, ...
            pos: (x,y) # Tupel mit der Position
        }
        :param funktion: Die Funktion die aufgerufen werden soll, wenn eine Taste gedrückt wurde
        :type funktion: (object) -> None
        :return:
        :rtype:
        """
        Spiel._mausBewegt = funktion

    @staticmethod
    def registriere_maus_losgelassen(funktion):
        """
        Registriert eine Funktion, die aufgerufen wird, wenn eine Maustaste losgelassen wird.
        :param funktion: Die Funktion
        :type funktion: (object)->None
        :return:
        :rtype:
        """
        Spiel._maus_taste_losgelassen = funktion

    @staticmethod
    def registriere_maus_gedrueckt(funktion):
        """
        Registriert eine Funktion, die aufgerufen wird, wenn eine Maustaste gedrückt wird.
        :param funktion:
        :type funktion: (object)->None
        :return:
        :rtype:
        """
        Spiel._maus_taste_gedrueckt = funktion

    @staticmethod
    def gib_zeichen_flaeche():
        """
        Gibt die Hauptzeichenfläche des Spiels zurück. Darauf kann (muss) gezeichnet werden.
        :return: Die Zeichenfläche
        :rtype:py2cd.flaeche.ZeichenFlaeche
        """
        return Spiel.__haupt_flaeche

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
        Spiel.__aktualisiere = funktion

    @staticmethod
    def entferne_aktualisierung():
        """
        Entfernt die Aktualisierugsfuntion
        :return:
        :rtype:
        """
        Spiel.__aktualisiere = lambda dt: None
