import pygame

from py2cd.bild import BildSpeicher

__author__ = 'Mark Weinreuter'

# Inspired by Al Sweigarts pyganim: http://inventwithpython.com/pyganim/

from py2cd.spiel import Spiel
from py2cd.flaeche import ZeichenFlaeche
from py2cd.objekte import ZeichenbaresElement

GESTOPPT = 0
GESTARTET = 1
PAUSIERT = 2


class Animation(ZeichenbaresElement):
    """
    Zeigt einen Animation an, indem eine Liste von Bildern(ZeichenFlaechen) in angegeben Zeitabschnitten
    durch gewechselt werden.
    """

    def __init__(self, pygame_flaechen_und_zeiten, wiederhole=False, alpha=True):
        """
        Erstellt einen neue Instanz aus den Flächen.
        :param pygame_flaechen_und_zeiten:
        :type pygame_flaechen_und_zeiten:list[(str|ZeichenFlaeche, int)]
        :param wiederhole:
        :type wiederhole: bool
        :param alpha:
        :type alpha:bool
        :return:
        :rtype:
        """

        self._wiederhole_animation = wiederhole
        """
        Gibt an ob die Animation wiederholt wird oder nicht
        """
        self._flaechen_zeiten = []
        """
        :type: list[(ZeichenFlaeche, int)]
        """

        self._gesamt_zeit = 0
        self._aktuelle_flaeche = 0
        self._zustand = GESTOPPT
        self._vergangen = 0
        self._gesamt_zeit = 0

        # zur Ermittlung der Dimension
        breite = 0
        hoehe = 0

        for zf in pygame_flaechen_und_zeiten:

            animations_bild = zf[0]

            # Die Fläche kann entweder aus einer Datei/ dem Bildspeicher geladen werden
            if isinstance(animations_bild, str):
                # Falls im Speicher, nehmen wir dieses Bild
                if BildSpeicher.ist_bild_vorhanden(animations_bild):
                    animations_bild = BildSpeicher.gib_pygame_flaeche(animations_bild)
                else:
                    # Ansonsten laden wir es
                    animations_bild = BildSpeicher.lade_bild_aus_datei(animations_bild, alpha)

            # oder schon eine pygame surface sein
            elif not isinstance(animations_bild, pygame.Surface):
                raise AttributeError("Entweder Surface oder Strings übergeben.")

            # die größten werte ermitteln
            if animations_bild.get_width() > breite:
                breite = animations_bild.get_width()
            if animations_bild.get_height() > hoehe:
                hoehe = animations_bild.get_height()

            # Zur List hinzufügen und Zeit addieren
            self._flaechen_zeiten.append((animations_bild, zf[1]))
            self._gesamt_zeit += zf[1]

        self._anzahl_flaechen = len(self._flaechen_zeiten)

        super().__init__(0, 0, breite, hoehe, None)

    def start(self):
        if self._zustand == GESTOPPT:
            self._vergangen = 0
            self._aktuelle_flaeche = 0

        self._zustand = GESTARTET

    def render(self, pyg_zeichen_flaeche):
        """
        Zeichnet das aktuelle Bild dieser Animation
        :param pyg_zeichen_flaeche:
        :type pyg_zeichen_flaeche:
        :return:
        :rtype:
        """
        if self._zustand == GESTARTET:
            self._vergangen += Spiel.zeit_unterschied_ms

            # falls die Zeit für das aktuelle Bild abgelaufen ist, gehe zum nächsetn bild
            while self._vergangen > self._flaechen_zeiten[self._aktuelle_flaeche][1]:
                self._vergangen -= self._flaechen_zeiten[self._aktuelle_flaeche][1]
                self._aktuelle_flaeche += 1  # nächste fläche

                # alle Flächen gezeichnet?
                if self._aktuelle_flaeche == self._anzahl_flaechen:

                    # aktuelle Fläche zurücksetzen
                    self._aktuelle_flaeche = 0

                    if not self._wiederhole_animation:
                        # animation anhalten
                        self._zustand = GESTOPPT
                        # Nichts zeichnen
                        return

            # Zeichne das aktuelle bild
            pyg_zeichen_flaeche.blit(self._flaechen_zeiten[self._aktuelle_flaeche][0],
                                     (self.x, self.y))

        elif self._zustand == PAUSIERT:
            # das aktuelle bild wird immer noch gezeichnet
            return pyg_zeichen_flaeche.blit(self._flaechen_zeiten[self._aktuelle_flaeche][0],
                                            (self.x, self.y))

    def zeige_bild(self, index):
        if index < 0 or index > len(self._flaechen_zeiten):
            raise ValueError("Index muss größer 0 und kleiner als die Anzahl an Bildern sein")

        self._aktuelle_flaeche = index

    def setze_wiederhole(self, wiederhole=True):
        self._wiederhole_animation = wiederhole

    def stop(self):
        self._zustand = GESTOPPT

    def pause(self):
        self._zustand = PAUSIERT


class AnimationSpeicher:
    __alle_animationen = {}

    @classmethod
    def ist_animation_vorhanden(cls, schluessel):
        return schluessel in cls.__alle_animationen

    @classmethod
    def registriere_animation(cls, schluessel, bilder_und_zeiten, wiederhole=False, alpha=True):
        cls.__alle_animationen[schluessel] = (bilder_und_zeiten, wiederhole, alpha)

        return Animation(*cls.__alle_animationen[schluessel])

    @classmethod
    def gib_animation(cls, schluessel):
        if schluessel not in cls.__alle_animationen:
            raise ValueError("Animation nicht im Speicher vorhanden.")

        return Animation(*cls.__alle_animationen[schluessel])
