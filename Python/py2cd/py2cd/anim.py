import py2cd

__author__ = 'Mark Weinreuter'

import pygame

from py2cd.spiel import Spiel
from py2cd.flaeche import ZeichenFlaeche
from py2cd.objekte import ZeichenbaresObjekt
from py2cd.box import Box

GESTOPPT = 0
GESTARTET = 1
PAUSIERT = 2


class Animation(ZeichenbaresObjekt):
    """
    Zeigt einen Animation an, indem eine Liste von Bildern(ZeichenFlaechen) in angegeben Zeitabschnitten durchgewechselt werden.
    """

    def berechne_groesse(self):
        return Box(0, 0, self.breite, self.hoehe)

    def __init__(self, flaechen, alpha=True):
        """

        :param flaechen:
        :type flaechen:list[(str|ZeichenFlaeche, int)]
        :param alpha:
        :type alpha:bool
        :return:
        :rtype:
        """

        self._wiederhole_animation = False
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
        self.breite = 0
        self.hoehe = 0

        for zf in flaechen:

            flaeche = zf[0]
            # Die Fläche kann entweder aus einer Datei geladen werden
            if isinstance(flaeche, str):
                flaeche = ZeichenFlaeche.lade_bild_aus_datei(zf[0], alpha)

            # oder schon eine Zeichenfläche sein
            elif not isinstance(flaeche, ZeichenFlaeche):
                raise AttributeError("Entweder ZeichenFlaeche oder Strings übergeben.")

            # die größten werte ermitteln
            if flaeche.breite > self.breite:
                self.breite = flaeche.breite
            if flaeche.hoehe > self.hoehe:
                self.hoehe = flaeche.hoehe

            # Zur List hinzufügen und Zeit addieren
            self._flaechen_zeiten.append((flaeche, zf[1]))
            self._gesamt_zeit += zf[1]

        flaeche = ZeichenFlaeche.neue_pygame_flaeche(self.breite, self.hoehe, alpha)
        self._anzahl_flaechen = len(self._flaechen_zeiten)

        super().__init__(flaeche, py2cd.spiel.Spiel.haupt_flaeche)

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

                if self._aktuelle_flaeche == self._anzahl_flaechen:  # alle Flächen gezeichnet?
                    self._aktuelle_flaeche = 0

                    if not self._wiederhole_animation:  # animation anhalten
                        self._zustand = GESTOPPT
                        return self.dimension

            return pyg_zeichen_flaeche.blit(self._flaechen_zeiten[self._aktuelle_flaeche][0]._pyg_flaeche,
                                            (self.x_intern, self.y_intern))
        elif self._zustand == PAUSIERT:
            return pyg_zeichen_flaeche.blit(self._flaechen_zeiten[self._aktuelle_flaeche][0]._pyg_flaeche,
                                            (self.x_intern, self.y_intern))  # das aktuelle bild wird immernoch gezeichnet

        # das Dimensionsrechteck wird immer zurück gegeben, auch wenn nichts gezeichnet wird
        return Box(self.x_intern, self.y_intern, self.breite, self.hoehe)

    def setze_wiederhole(self, wiederhole=True):
        self._wiederhole_animation = wiederhole

    def stop(self):
        self._zustand = GESTOPPT

    def pause(self):
        self._zustand = PAUSIERT