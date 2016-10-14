import random
import threading
import time

from arena import *

__author__ = 'Mark Weinreuter'

# Fake-Enums
OBEN = 1
UNTEN = 2
LINKS = 3
RECHTS = 4


class Algorithmus(threading.Thread):
    SCHLAF_ZEIT = .00001

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.richtung = LINKS


        # For some more randomness :)
        time.sleep(.2)
        random.seed()
        self.x = random.randint(0, SPIELFELD_BREITE-1)

        time.sleep(.2)
        random.seed()
        self.y = SPIELFELD_HOEHE - random.randint(0, SPIELFELD_HOEHE-1)

        self.arena = None
        self.gegner_index = -1
        self.index = -1
        self._letzter_zustand = FREI
        self.__fertig_sperre = threading.Lock()
        self.__punkte_sperre = threading.Lock()
        self.__zug_fertig = True
        self.__neu_eroberte_punkte = []
        """
        Liste mit allen neu eroberten Punkten.
        :type: [(int, int)]
        """

        # Logging Ausgabe anpassen
        # logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s', )
        # logging.debug("Starte %s in %d, %d" % (self.name, self.x, self.y))


    def richtung_hor(self, richtung):
        return richtung == LINKS or richtung == RECHTS

    def richtung_horizontal(self):
        return self.richtung == LINKS or self.richtung == RECHTS

    def richtung_vertikal(self):
        return self.richtung == OBEN or self.richtung == UNTEN

    def richtung_ver(self, richtung):
        return richtung == OBEN or richtung == UNTEN

    def drehe_horizontal(self):
        if self.richtung == LINKS:
            self.richtung = RECHTS
        else:
            self.richtung = LINKS

    def drehe_vertikal(self):
        if self.richtung == OBEN:
            self.richtung = UNTEN
        else:
            self.richtung = OBEN

    def drehe_ver(self, richtung):
        if richtung == OBEN:
            return UNTEN
        else:
            return OBEN

    def drehe_hor(self, richtung):
        if richtung == LINKS:
            return RECHTS
        else:
            return LINKS

    def __str__(self):
        return "%s: %d, %d" % (self.name, self.x, self.y)

    def run(self):

        while self.arena.laueft_noch():
            # 'with' übernimmt das anfordern und freigeben der sperre für uns:
            # Flag setzen, dass wir am Arbeiten sind
            with self.__fertig_sperre:
                self.__zug_fertig = False

            # in Richtung bewegen, bzw. versuchen
            richtung = self.gib_richtung(self._letzter_zustand)
            self._letzter_zustand = self.__bewege(richtung)

            # Flag zurück setzen
            with self.__fertig_sperre:
                self.__zug_fertig = True

            # damit nicht alles sofort vorbei ist :D
            time.sleep(self.SCHLAF_ZEIT)

    def init(self, arena, index, gegner_index):
        self.arena = arena
        self.gegner_index = gegner_index
        self.index = index

        self.setName(self.name)

    def abstand_links(self):
        return self.x

    def abstand_rechts(self):
        return SPIELFELD_BREITE - self.x

    def abstand_oben(self):
        return self.y

    def abstand_unten(self):
        return SPIELFELD_HOEHE - self.y

    def ist_bereit(self):

        with self.__fertig_sperre:
            bereit = self.__zug_fertig

        return bereit

    def gib_eroberte_punkte(self):
        with self.__punkte_sperre:
            # Liste kopieren und leeren
            punkte = self.__neu_eroberte_punkte.copy()
            self.__neu_eroberte_punkte.clear()

        return punkte

    def gib_richtung(self, letzter_zustand):
        """
        Gibt die Bewegungsrichtung an.

        :param letzter_zustand: Der Zustand der letzen Bewegung
        :type letzter_zustand: FREI, BESUCHT, BELEGT, RAND
        :return: Eine Bewegungsrichtung
        :rtype: UNTEN, OBEN, LINKS, RECHTS
        """
        raise NotImplementedError("Diese Methode muss überschrieben werden und OBEN, UNTEN, RECHTS oder LINKS zurückgeben.")

    def __bewege(self, richtung):

        x = self.x
        y = self.y

        if richtung == UNTEN:
            y += 1
        elif richtung == OBEN:
            y -= 1
        elif richtung == LINKS:
            x -= 1
        elif richtung == RECHTS:
            x += 1
        else:
            raise AttributeError("Richtung muss entweder OBEN(1), UNTEN(2), LINKS(3) oder RECHTS(4) sein!")

        info = self.arena.versuche_bewegung(x, y, self.index)
        if info == BESUCHT or info == FREI:

            # Position ändern
            self.x = x
            self.y = y
            if info == FREI:
                with self.__punkte_sperre:
                    self.__neu_eroberte_punkte.append((x, y))

        return info
