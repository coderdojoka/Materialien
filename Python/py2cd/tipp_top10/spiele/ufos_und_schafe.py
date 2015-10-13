__author__ = 'Mark Weinreuter'

from py2cd.anim import Animation, AnimationSpeicher
from py2cd.bild import Bild, BildSpeicher
from py2cd.spiel import Spiel
from tipp_top10.tt_basis import TTBasis
from tipp_top10.tt_text_anzeige import *
from tipp_top10.level import schwierigkeit


class UfoUndSchafeSpiel(TTBasis):
    alle_ufos = []
    alle_schafe = []

    def __init__(self, flaeche):
        super().__init__(flaeche)

    def aufbauen(self):
        BildSpeicher.lade_bild("ufo", "bilder/ufo.png", True)
        BildSpeicher.lade_bild("such_strahl1", "bilder/such_strahl_trans0.png", True)
        BildSpeicher.lade_bild("such_strahl2", "bilder/such_strahl_trans1.png", True)
        BildSpeicher.lade_bild("such_strahl3", "bilder/such_strahl_trans1.png", True)

        BildSpeicher.lade_bild("grass_1", "bilder/grass_1.png", True)
        BildSpeicher.lade_bild("grass_2", "bilder/grass_2.png", True)
        BildSpeicher.lade_bild("grass_3", "bilder/grass_3.png", True)
        BildSpeicher.lade_bild("grass_4", "bilder/grass_4.png", True)
        BildSpeicher.lade_bild("grass_5", "bilder/grass_5.png", True)

        BildSpeicher.lade_bild("fallschirm", "bilder/fallschirm.png", True)
        BildSpeicher.lade_bild("schaf_1", "bilder/schaf_1.png", True)
        BildSpeicher.lade_bild("schaf_2", "bilder/schaf_2.png", True)

        BildSpeicher.lade_bild("sonne", "bilder/sonne.png", True)

        zeit = 1000 / 6
        bilder_zeiten = []
        for i in range(1, 6):
            BildSpeicher.lade_bild("rauch_%d" % i, "../beispiele/testimages/smoke_puff_000%d.png" % i, True)
            bilder_zeiten.append(("rauch_%d" % i, zeit))

        AnimationSpeicher.registriere_animation("rauch", bilder_zeiten)
        AnimationSpeicher.registriere_animation("such_strahl",
                                                [("such_strahl1", 300), ("such_strahl2", 500), ("such_strahl3", 300)])

        sonne = BildSpeicher.gib_bild("sonne")
        sonne.aendere_position(Spiel.breite - 150, 25)

        self.neues_schaf()
        self.neues_schaf()
        s = self.neues_schaf()
        s.fallschirm_rettung(300, 200)

        for i in range(schwierigkeit.anzahl_ufos):
            self.neues_ufo()

        anzahl = 60
        b = Spiel.breite / anzahl

        for i in range(1, anzahl):
            g1 = BildSpeicher.gib_bild("grass_" + str(random.randint(1, 5)))
            y_offset = random.randint(0, 10) - 5
            x_offset = random.randint(0, 10) - 5

            g1.aendere_position(i * b + x_offset, 360 + y_offset)

    def aktualisiere(self, delta):
        for ufo in self.alle_ufos:
            ufo.aktualisiere(delta)

        for schaf in self.alle_schafe:
            schaf.aktualisiere(delta)

    @classmethod
    def neues_ufo(cls):
        u = Ufo()
        cls.alle_ufos.append(u)
        return u

    @classmethod
    def neues_schaf(cls):
        s = Schaf()
        cls.alle_schafe.append(s)
        return s


class Schaf(Animation):
    MODUS_GRASSEND = 1
    MODUS_HOCHFLIEGEN = 2
    MODUS_FALLSCHIRM = 3
    MODUS_ENTFUERT = 4

    schaf_hoehe = 315

    def __init__(self):
        self.bewegungs_richtung = 1
        self.timer = 0
        self.timer_grenze = 400
        self.modus = Schaf.MODUS_GRASSEND
        self.entfuerendes_ufo = None

        # Fallschirm bild hinzufügen und zunächst verstecken
        self.fallschirm = BildSpeicher.gib_bild("fallschirm")
        self.fallschirm.verstecke()

        # Animation initialsieren
        super().__init__(
            [(BildSpeicher.gib_pygame_flaeche("schaf_1"), 500), (BildSpeicher.gib_pygame_flaeche("schaf_2"), 500)])

        self.setze_position(random.randint(0, Spiel.breite), Schaf.schaf_hoehe)
        self.start()
        self.setze_wiederhole(True)

    def aktualisiere(self, delta):

        self.timer += delta
        if self.timer > self.timer_grenze:
            self.bewegungs_richtung *= -1
            self.timer = 0
            self.timer_grenze = random.randint(200, 1000)


        if self.modus == Schaf.MODUS_HOCHFLIEGEN:
            self._hochfliegen(delta)
        elif self.modus == Schaf.MODUS_FALLSCHIRM:
            self._fallschirm_springen(delta)
        else:
            self._grasen(delta)

    def _grasen(self, delta):
        x = random.randint(0, 3)

        # Sicher stellen, dass wir immer im Spielfeld laufen
        if self.x + self.breite > Spiel.breite:
            self.bewegungs_richtung = -1
        elif self.x < 0:
            self.bewegungs_richtung = 1

        self.aendere_position(x * self.bewegungs_richtung * delta, 0)

    def _fallschirm_springen(self, delta):
        if self.y < Schaf.schaf_hoehe:
            x = random.randint(0, 2)
            self.aendere_position(self.bewegungs_richtung * delta, 1.5 * delta)
            self.fallschirm.setze_position(self.x - 25, self.y - 70)
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
    schaf_sammel_hoehe = 270

    MODUS_RUNTERFLIEGEN = 1
    MODUS_ENTFUEHREN = 2
    MODUS_SCHAF_SAUGEN = 3
    MODUS_WEG_FLIEGEN = 4
    MODUS_EXPLODIEREN = 5

    def __init__(self):

        pygame_ufo = BildSpeicher.gib_pygame_flaeche("ufo")
        x = random.randint(0, Spiel.breite - pygame_ufo.get_width())

        super().__init__(x, 0, pygame_ufo)
        self.text = UfoUndSchafeSpiel.neues_wort(self, 0, -30, self.zerstoert)
        self.such_strahl = AnimationSpeicher.gib_animation("such_strahl")
        self.such_strahl.start()
        self.such_strahl.setze_wiederhole()
        self.such_strahl.verstecke()
        self.timer = 20
        self.bewegungs_richtung = 1 if random.randint(0, 1) == 1 else -1
        self.entfuertes_schaf = None
        self.modus = Ufo.MODUS_RUNTERFLIEGEN

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
            self._runter_fliegen(delta)
        elif self.modus == Ufo.MODUS_ENTFUEHREN:
            self._entfuehren(delta)
        elif self.modus == Ufo.MODUS_WEG_FLIEGEN:
            self._weg_fliegen(delta)

    def _weg_fliegen(self, delta):
        y = -random.randint(0, 4) * delta
        x = random.randint(0, 1) * self.bewegungs_richtung * delta
        self.aendere_position(x, y)

        if self.y + self.hoehe < 0:
            print("Entkommen...")
            # Wir sind entkommen
            UfoUndSchafeSpiel.alle_ufos.remove(self)
            self.selbst_entfernen()
            self.such_strahl.selbst_entfernen()

            # Das Schaf entfernen
            UfoUndSchafeSpiel.alle_schafe.remove(self.entfuertes_schaf)
            self.entfuertes_schaf.selbst_entfernen()
            TextUebersicht.text_nicht_geschafft(self.text)

            # neues UFo erzeugen
            UfoUndSchafeSpiel.neues_ufo()

    def _runter_fliegen(self, delta):

        if self.y + self.hoehe > Ufo.schaf_sammel_hoehe:
            self.such_strahl.zeige()
            self.such_strahl.start()
            self.such_strahl.setze_wiederhole(True)
            self.such_strahl.setze_position(self.x + (self.breite - self.such_strahl.breite) / 2, self.y + 80)
            self.modus = Ufo.MODUS_ENTFUEHREN

        y = random.randint(0, 2)
        self.aendere_position(random.randint(0, 1) * self.bewegungs_richtung * delta, y * delta)

    def _entfuehren(self, delta):
        if self.entfuertes_schaf is None:
            for schaf in UfoUndSchafeSpiel.alle_schafe:
                if schaf.entfuerendes_ufo is None and schaf.modus == Schaf.MODUS_GRASSEND and abs(
                                schaf.mitte[0] - self.mitte[0]) < 10:
                    # Wir haben ein Schaf gefunden (yummi :D)
                    self.entfuertes_schaf = schaf
                    schaf.wird_entfuehrt(self)
                    break
        else:
            # wir haben das Schaf eingesaugt!!!
            if self.entfuertes_schaf.y <= Ufo.schaf_sammel_hoehe - 50:
                self.modus = Ufo.MODUS_WEG_FLIEGEN
                self.such_strahl.verstecke()

        self.aendere_position(0.5 * random.randint(0, 1) * self.bewegungs_richtung * delta,
                              0.5 * random.randint(0, 1) * self.bewegungs_richtung * delta)
        self.such_strahl.setze_position(self.x + (self.breite - self.such_strahl.breite) / 2, self.y + 50)

    def zerstoert(self):
        self.such_strahl.selbst_entfernen()
        self.selbst_entfernen()
        UfoUndSchafeSpiel.alle_ufos.remove(self)

        # Falls das Ufo zerstört wird, während es ein schaf entführt
        if self.entfuertes_schaf is not None:
            self.entfuertes_schaf.fallschirm_rettung(*self.position())

        rauch_animation = AnimationSpeicher.gib_animation("rauch")
        rauch_animation.aendere_position(*self.position())
        rauch_animation.start()
        UfoUndSchafeSpiel.neues_ufo()
