import logging
from threading import Lock

__author__ = 'Mark Weinreuter'

LIMIT_ZUEGE = 10000
SPIELFELD_BREITE = 100
SPIELFELD_HOEHE = 100
BOX_GROESSE = 6

FREI = 1
RAND = 2
BELEGT = 3
BESUCHT = 4


class Arena:
    def __init__(self, algo1_modul, algo1_name, algo2_modul, algo2_name):
        """

        :param algo1_modul: Der Name des Moduls (python Datei), z.B. zufall
        :type algo1_modul: str
        :param algo1_name: Der Name der Klasse, z.B. Zufall1
        :type algo1_name: str
        :param algo2_modul: Der Name des Moduls (python Datei), z.B. zufall
        :type algo2_modul: str
        :param algo2_name: Der Name der Klasse, z.B. Zufall1
        :type algo2_name: str
        :return:
        :rtype:
        """

        # zurücksetzen, für den nächsten Durchlauf
        self.felder = bytearray(SPIELFELD_BREITE * SPIELFELD_HOEHE)
        self.felder_sperre = Lock()
        self.zuege_sperre = Lock()

        self.zuege_uebersicht = [0, 0, 0]
        """
        Hier werden die Gesamtanzahl an Zuegen und die Anzahl der Züge der einzelnen Algorithmen gesammelt.
        :type: [int]
        """
        self.punkte = [0, 0]
        """
        Hier werden die Punkte(eroberten Felder dier beiden Algos gespeichert
        """

        _modul1 = __import__(algo1_modul, globals(), locals())
        _modul2 = __import__(algo2_modul, globals(), locals())

        self.algo1 = getattr(_modul1, algo1_name)()
        """
        :type: algorithmus.Algorithmus
        """
        self.algo2 = getattr(_modul2, algo2_name)()
        """
        :type: algorithmus.Algorithmus
        """

        self.algo1.init(self, 1, 2)
        self.algo2.init(self, 2, 1)

        # Logging Ausgabe anpassen
        logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s', )

    def start(self):
        self.algo1.start()
        self.algo2.start()

    def aktualisiere(self):

        # Die neuen Punkte der beiden Algos abfragen (thread-sicher)
        punkte1 = self.algo1.gib_eroberte_punkte()
        punkte2 = self.algo2.gib_eroberte_punkte()

        anz_punkte1 = len(punkte1)
        anz_punkte2 = len(punkte2)

        # logging.debug("Neue Punkte1: %d, Neue Punkte2: %d" % (anz_punkte1, anz_punkte2))

        self.punkte[0] += anz_punkte1
        self.punkte[1] += anz_punkte2

        if not self.laueft_noch():
            self.beenden()

        return punkte1, punkte2

    def beenden(self):
        # Um die Schleife abzubrechen
        with self.zuege_sperre:
            self.gesamt_zuege = LIMIT_ZUEGE + 1

        # Auf beide Algos warten
        if self.algo2.is_alive():
            self.algo2.join()

        if self.algo1.is_alive():
            self.algo1.join()

        return True

    def versuche_bewegung(self, x, y, algo_index):
        with self.zuege_sperre:
            self.zuege_uebersicht[0] += 1
            self.zuege_uebersicht[algo_index] += 1

        if x < 0 or x >= SPIELFELD_BREITE or y < 0 or y >= SPIELFELD_HOEHE:
            return RAND

        # Nur ein Thread einlassen, für andere Threads sperren:
        # Felder Info aktualisieren
        with self.felder_sperre:
            farbe = self.felder[x + y * SPIELFELD_HOEHE]

            if farbe == 0:
                # Daten aktualisieren
                self.felder[y * SPIELFELD_HOEHE + x] = algo_index

                return FREI

            if farbe == algo_index:
                return BESUCHT
            else:
                return BELEGT

    def laueft_noch(self):
        with self.zuege_sperre:
            return self.zuege_uebersicht[0] < LIMIT_ZUEGE
