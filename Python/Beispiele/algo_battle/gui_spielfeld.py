from pyenguin import *

from arena import *

__author__ = 'Mark Weinreuter'

FARBEN = [TUERKIS, ORANGE]
SPIELER_1 = -1
SPIELER_2 = -2


class SpielFeld(Arena):
    def __init__(self, algo1_modul, algo1_name, algo2_modul, algo2_name):
        super().__init__(algo1_modul, algo1_name, algo2_modul, algo2_name)
        self.flaeche = Flaeche(SPIELFELD_BREITE * BOX_GROESSE, SPIELFELD_HOEHE * BOX_GROESSE)
        self.flaeche.zentriere()
        self.flaeche.fuelle(WEISS)

    def aktualisiere(self):

        # Die neuen Punkte der beiden Spieler abfragen (thread-sicher)
        punkte1, punkte2 = super().aktualisiere()

        for x, y in punkte1:
            # Rechteck zeichnen
            self.flaeche.rechteck(x * BOX_GROESSE, y * BOX_GROESSE, BOX_GROESSE, BOX_GROESSE, FARBEN[0])

        for x, y in punkte2:
            # Rechteck zeichnen
            self.flaeche.rechteck(x * BOX_GROESSE, y * BOX_GROESSE, BOX_GROESSE, BOX_GROESSE, FARBEN[1])
