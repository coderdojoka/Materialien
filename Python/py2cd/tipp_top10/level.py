__author__ = 'Mark Weinreuter'


class Schwierigkeit():

    def __init__(self, max_buchstaben, naechstes_level, anzahl_ufos):
        self.max_buchstaben = max_buchstaben
        self.naechstes_level = naechstes_level
        self.anzahl_ufos = anzahl_ufos

LEICHT = lambda : Schwierigkeit(2, 32, 2)
MITTEL = lambda : Schwierigkeit(4, 16, 3)
SCHWER = lambda : Schwierigkeit(6, 8, 5)

schwierigkeit = LEICHT()