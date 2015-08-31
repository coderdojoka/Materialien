import random

from py2cd.anim import Animation
from py2cd.bild import Bild
from py2cd.spiel import Spiel
from tipp_top.tt_text_anzeige import TextUebersicht

__author__ = 'Mark Weinreuter'

alle_ufos = []
alle_schafe = []


def neues_ufo():
    u = Ufo()
    alle_ufos.append(u)
    return u


def neues_schaf():
    s = Schaf()
    alle_schafe.append(s)
    return s


class Schaf(Animation):
    schaf1_bild = None
    schaf2_bild = None
    MODUS_GRASSEND = 1
    MODUS_HOCHFLIEGEN = 2
    MODUS_FALLSCHIRM = 3
    MODUS_ENTFUERT = 4
    schaf_hoehe = 300

    def __init__(self):
        self.bewegungs_richtung = 1
        self.timer = 0
        self.timer_grenze = 400
        self.modus = Schaf.MODUS_GRASSEND
        self.entfuerendes_ufo = None

        if Schaf.schaf1_bild is None:
            Schaf.fallschirm_bild = Bild.lade_bild_aus_datei("bilder/fallschirm.png", True)
            Schaf.schaf1_bild = Bild.lade_bild_aus_datei("bilder/schaf_1.png", True)
            Schaf.schaf2_bild = Bild.lade_bild_aus_datei("bilder/schaf_2.png", True)


        # Fallschirm bild hinzufügen und zunächst verstecken
        self.fallschirm = Bild(0, 0, Schaf.fallschirm_bild, True)
        self.fallschirm.verstecke()

        # Animation initialsieren
        super().__init__([(Schaf.schaf1_bild, 500), (Schaf.schaf2_bild, 500)])

        self.setze_position(random.randint(0, Spiel.breite), Schaf.schaf_hoehe)
        self.start()
        self.setze_wiederhole(True)

    def aktualisiere(self, delta):

        if self.modus == Schaf.MODUS_HOCHFLIEGEN:
            self._hochfliegen(delta)
        elif self.modus == Schaf.MODUS_FALLSCHIRM:
            self._fallschirm_springen(delta)
        else:
            self._grasen(delta)

    def _grasen(self, delta):
        x = random.randint(0, 3)

        self.timer += delta
        if self.timer > self.timer_grenze:
            self.bewegungs_richtung *= -1
            self.timer = 0
            self.timer_grenze = random.randint(200, 1000)

        self.aendere_position(x * self.bewegungs_richtung, 0)

        if self.bewegungs_richtung == 1 and self.x + self.breite > Spiel.breite:
            self.bewegungs_richtung = -1
        elif self.bewegungs_richtung == -1 and self.x < 0:
            self.bewegungs_richtung = 1

    def _fallschirm_springen(self, delta):
        if self.y < Schaf.schaf_hoehe:
            x = random.randint(0, 2)
            self.aendere_position(x, 1)
            self.fallschirm.setze_position(self.x - 25, self.y - 110)
        else:
            self.fallschirm.verstecke()
            self.modus = Schaf.MODUS_GRASSEND

    def wird_entfuehrt(self, ufo):
        self.modus = Schaf.MODUS_HOCHFLIEGEN
        self.entfuerendes_ufo = ufo

    def fallschirm_rettung(self, x, y):
        self.modus = Schaf.MODUS_FALLSCHIRM
        self.entfuerendes_ufo = None
        self.setze_position(x, y)
        self.zeige()
        self.fallschirm.zeige()

    def _hochfliegen(self, delta):
        if self.y > Ufo.schaf_sammel_hoehe - 50:
            self.aendere_position(0, -3)
        else:
            self.verstecke()
            self.modus = Schaf.MODUS_ENTFUERT


class Ufo(Bild):
    ufo_bild = None
    such_strahl_bild1 = None
    such_strahl_bild2 = None
    such_strahl_bild3 = None
    schaf_sammel_hoehe = 270

    MODUS_RUNTERFLIEGEN = 1
    MODUS_ENTFUEHREN = 2
    MODUS_SCHAF_SAUGEN = 3
    MODUS_WEG_FLIEGEN = 4
    MODUS_EXPLODIEREN = 5

    def __init__(self):
        if Ufo.ufo_bild is None:
            Ufo.ufo_bild = Bild.lade_bild_aus_datei("bilder/ufo.png", True)
            Ufo.such_strahl_bild1 = Bild.lade_bild_aus_datei("bilder/such_strahl_trans0.png", True)
            Ufo.such_strahl_bild2 = Bild.lade_bild_aus_datei("bilder/such_strahl_trans1.png", True)
            Ufo.such_strahl_bild3 = Bild.lade_bild_aus_datei("bilder/such_strahl_trans2.png", True)

        self.text = TextUebersicht.neuer_text(0, Ufo.ufo_bild.get_height(), self.zerstoert)
        self.such_strahl = Animation(
            [(Ufo.such_strahl_bild1, 100), (Ufo.such_strahl_bild2, 300), (Ufo.such_strahl_bild3, 1000)], True, True)
        self.such_strahl.start()
        self.such_strahl.setze_wiederhole()
        self.such_strahl.verstecke()
        self.timer = 20
        self.bewegungs_richtung = 1 if random.randint(0,1) == 1 else -1
        self.enfuertes_schaf = None
        self.modus = Ufo.MODUS_RUNTERFLIEGEN

        def bewegt():
            self.such_strahl.zentriere_in_objekt(self)
            self.such_strahl.aendere_position(0, 80)
            self.text.setze_position(self.x, self.y - 110)

        x = random.randint(0, Spiel.breite - Ufo.ufo_bild.get_width())
        super().__init__(x, 0, Ufo.ufo_bild, position_geaendert=bewegt)

        self.nach_vorne()

    def aktualisiere(self, delta):

        self.timer += delta
        if self.timer > 100:
            self.bewegungs_richtung *= -1
            self.timer = 0

        if self.x <= 0:
            self.bewegungs_richtung = 1
        elif self.x >= Spiel.breite:
            self.bewegungs_richtung = -1

        if self.modus == Ufo.MODUS_RUNTERFLIEGEN:
            self._runter_fliegen()
        elif self.modus == Ufo.MODUS_ENTFUEHREN:
            self._entfuehren()
        elif self.modus == Ufo.MODUS_WEG_FLIEGEN:
            self._weg_fliegen()

    def _weg_fliegen(self):
        y = -random.randint(0, 4)
        x = random.randint(0, 1) * self.bewegungs_richtung
        self.aendere_position(x, y)

        if self.y + self.hoehe < 0:
            print("Entkommen...")
            # Wir sind entkommen
            alle_ufos.remove(self)
            self.entferne()
            self.such_strahl.entferne()

            # Das Schaf entfernen
            alle_schafe.remove(self.enfuertes_schaf)
            self.enfuertes_schaf.entferne()
            TextUebersicht.text_nicht_geschafft(self.text)

    def _runter_fliegen(self):

        if self.y + self.hoehe > Ufo.schaf_sammel_hoehe:
            self.such_strahl.zeige()
            self.modus = Ufo.MODUS_ENTFUEHREN

        y = random.randint(0, 2)
        self.aendere_position(random.randint(0, 1) * self.bewegungs_richtung, y)

    def _entfuehren(self):
        if self.enfuertes_schaf is None:
            for schaf in alle_schafe:
                if schaf.entfuerendes_ufo is None and abs(schaf.mitte[0] - self.mitte[0]) < 10:
                    # Wir haben ein Schaf gefunden (yummi :D)
                    self.enfuertes_schaf = schaf
                    schaf.wird_entfuehrt(self)
                    break
        else:
            # wir haben das Schaf eingesaugt!!!
            if self.enfuertes_schaf.y <= Ufo.schaf_sammel_hoehe - 50:
                self.modus = Ufo.MODUS_WEG_FLIEGEN
                self.such_strahl.verstecke()

        self.aendere_position(0, 0.5 * random.randint(0, 1) * self.bewegungs_richtung)

    def zerstoert(self):
        self.such_strahl.entferne()
        self.entferne()
        alle_ufos.remove(self)
        if self.enfuertes_schaf is not None:
            self.enfuertes_schaf.fallschirm_rettung(*self.position())
        neues_ufo()
