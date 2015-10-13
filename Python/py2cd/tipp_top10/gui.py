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
    def __init__(self, x, y, wenn_geaendert=lambda wert: None, bilder=("unchecked", "checked")):
        BildWechsler.__init__(self, x, y, bilder)
        Anklickbar.__init__(self, self.punkt_in_rechteck, self.__wenn_geklickt)
        self.gesetzt = False
        self.wenn_geaendert = wenn_geaendert

    def __wenn_geklickt(self, ereignis):
        self.umschalten()

    def umschalten(self, wert=None):
        if wert is not None and self.gesetzt == wert:
            return

        self.gesetzt = not self.gesetzt if wert == None else wert
        self.zeige_bild(self.gesetzt)
        self.wenn_geaendert(self.gesetzt)


class RadioButtonGruppe():
    def __init__(self, anzahl):
        self.buttons = []
        self.welcher = 0

        for i in range(anzahl):
            button = CheckBox(0, i * 40, (lambda a: lambda x: self.geaendert(a))(i))
            self.buttons.append(button)

        self.buttons[0].umschalten()

    def setze_button(self, index, x, y):
        self.buttons[index].aendere_position(x, y)

    def geaendert(self, welcher):
        print(welcher)
        if welcher == self.welcher:
            self.buttons[self.welcher].umschalten(True)
            return

        self.buttons[self.welcher].umschalten(False)
        self.welcher = welcher
        self.buttons[self.welcher].umschalten(True)
