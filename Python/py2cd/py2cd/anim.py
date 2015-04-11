__author__ = 'Mark Weinreuter'

import py2cd

from py2cd.spiel import Spiel
from py2cd.flaeche import ZeichenFlaeche
from py2cd.objekte import ZeichenbaresObjekt

GESTOPPT = 0
GESTARTET = 1
PAUSIERT = 2


class Animation(ZeichenbaresObjekt):
    """
    Zeigt einen Animation an, indem eine Liste von Bildern(ZeichenFlaechen) in angegeben Zeitabschnitten
    durch gewechselt werden.
    """

    def __init__(self, flaechen_und_zeiten, wiederhole=False, alpha=True):
        """
        Erstellt einen neue Instanz aus den Flächen.
        :param flaechen_und_zeiten:
        :type flaechen_und_zeiten:list[(str|ZeichenFlaeche, int)]
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

        for zf in flaechen_und_zeiten:

            flaeche = zf[0]

            # Die Fläche kann entweder aus einer Datei geladen werden
            if isinstance(flaeche, str):
                flaeche = ZeichenFlaeche.lade_bild_aus_datei(zf[0], alpha)

            # oder schon eine Zeichenfläche sein
            elif not isinstance(flaeche, ZeichenFlaeche):
                raise AttributeError("Entweder ZeichenFlaeche oder Strings übergeben.")

            # die größten werte ermitteln
            if flaeche.breite > breite:
                breite = flaeche.breite
            if flaeche.hoehe > hoehe:
                hoehe = flaeche.hoehe

            # Zur List hinzufügen und Zeit addieren
            self._flaechen_zeiten.append((flaeche, zf[1]))
            self._gesamt_zeit += zf[1]

        self._anzahl_flaechen = len(self._flaechen_zeiten)

        super().__init__(0, 0, breite, hoehe, py2cd.spiel.Spiel.haupt_flaeche, None)

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
            pyg_zeichen_flaeche.blit(self._flaechen_zeiten[self._aktuelle_flaeche][0].pyg_flaeche,
                                     (self.x, self.y))

        elif self._zustand == PAUSIERT:
            # das aktuelle bild wird immer noch gezeichnet
            return pyg_zeichen_flaeche.blit(self._flaechen_zeiten[self._aktuelle_flaeche][0].pyg_flaeche,
                                            (self.x, self.y))

    def setze_wiederhole(self, wiederhole=True):
        self._wiederhole_animation = wiederhole

    def stop(self):
        self._zustand = GESTOPPT

    def pause(self):
        self._zustand = PAUSIERT
