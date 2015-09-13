from py2cd import *
from py2cd.farben import *

__author__ = 'Mark Weinreuter'


class Anklickbar():
    __anklickbare = []

    @classmethod
    def gib_anklickbare(cls):
        return cls.__anklickbare

    @classmethod
    def entferne_anklickbar(cls, was):
        cls.__anklickbare.remove(was)

    def __init__(self, punkt_test, maus_unten, maus_oben=lambda e: None, maus_ueber=lambda e: None,
                 maus_verlassen=lambda e: None):
        self.punkt_test = punkt_test
        self.maus_gedrueckt = maus_unten
        self.maus_losgelassen = maus_oben
        self.maus_betreten = maus_ueber
        self.maus_verlassen = maus_verlassen

        Anklickbar.__anklickbare.append(self)


class KlickText(Text, Anklickbar):
    hintergrund_farbe = HELL_GRAU
    klick_farbe = BLAU

    def __init__(self, x, y, text, wenn_geklickt, schrift):
        Text.__init__(self, text, x, y, schrift, hintergrund=KlickText.hintergrund_farbe)
        Anklickbar.__init__(self, self.punkt_in_rechteck, self.__maus_unten, self.__maus_oben)

        self.wenn_geklickt = wenn_geklickt

    def __maus_unten(self, ereignis):
        self.hintergrund = KlickText.klick_farbe

    def __maus_oben(self, ereignis):
        self.hintergrund = KlickText.hintergrund_farbe
        self.wenn_geklickt()


class CheckBox(BildWechsler, Anklickbar):
    def __init__(self, x, y, wenn_geaendert=lambda wert: None):
        BildWechsler.__init__(self, x, y, ["unchecked", "checked"])
        Anklickbar.__init__(self, self.punkt_in_rechteck, self.__maus_unten)
        self.gesetzt = False
        self.wenn_geaendert = wenn_geaendert

    def __maus_unten(self, ereignis):
        self.gesetzt = not self.gesetzt
        self.zeige_bild(self.gesetzt)
        self.wenn_geaendert(self.gesetzt)
