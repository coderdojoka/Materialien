from pgu.gui.input import Input

__author__ = 'Mark Weinreuter'

import sys

from py2cd import *
from tipp_top10.gui import CheckBox, KlickText, Anklickbar, RadioButtonGruppe
from tipp_top10.konstanten import *
from tipp_top10.tt_tastatur import *
from tipp_top10.spiele.ufos_und_schafe import *

class TTHaupt(Spiel):
    aktuelles_spiel = None
    aktuelles_spiel_index = 0
    start_flaeche = None
    hintergrund_flaeche = None
    geladene_spiele = {}
    punkte = 0

    def __init__(cls):
        super().__init__()

    @classmethod
    def initialisiere(cls):

        super().init(fenster_breite, fenster_hoehe, "TippTop10")
        LektionenUebersicht.lade_lektionen()


        # Die Fläche auf die die Tastatur + Spiel gezeichnet werden
        cls.hintergrund_flaeche = ZeichenFlaeche(0, 0, (fenster_breite, fenster_hoehe, True))

        # Die Tastaturfläche
        tastatur_flaeche = ZeichenFlaeche(0, tastatur_position_y, (788, tastatur_hoehe, True), eltern_flaeche=cls.hintergrund_flaeche)
        tastatur_flaeche.zentriere_horizontal()

        # Tastatur erstellen
        initialisiere_tasten(tastatur_flaeche)

        cls.punkte_stand = Text("0", 10, 5, Schrift(32))
        cls.punkte_stand.nach_vorne()


        def punkte_geaendert(wert):
            cls.punkte += wert
            cls.punkte_stand.setze_text(str(cls.punkte))

        TextUebersicht.punkte_geaendert = punkte_geaendert

        # Rahmen
        cls.rahmen = Rechteck(0, 0, fenster_breite, spiel_hoehe, SCHWARZ, dicke=1, eltern_flaeche=cls.hintergrund_flaeche)

        # Alle Tasten registrieren
        for key in tasten:
            Spiel.registriere_taste_gedrueckt(key, cls.taste_gedrueckt)

        cls._lade_spiele()
        cls._initialisiere_startseite()

    @staticmethod
    def taste_gedrueckt(unten, ereignis):

        if unten:
            tasten[ereignis.key].gedrueckt()
            if ereignis.key == K_BACKSPACE:
                TextUebersicht.buchstabe_loeschen()
            else:
                TextUebersicht.buchstabe_getippt(ereignis.unicode)
        else:
            tasten[ereignis.key].losgelassen()

    @classmethod
    def _lade_spiele(cls):
        sys.path.append("spiele/")

        datei = open("spiele/spiele.json")
        json_text = datei.read()
        datei.close()
        cls.geladene_spiele = json.loads(json_text)["spiele"]
        print(cls.geladene_spiele)

    @classmethod
    def _initialisiere_startseite(cls):

        # Standart Zeichen fläche speichern und ändern
        alte_flaeche = Spiel.standard_flaeche
        cls.start_flaeche = ZeichenFlaeche(0, 0, (fenster_breite, fenster_hoehe), WEISS, eltern_flaeche=cls.gib_zeichen_flaeche())
        Spiel.standard_flaeche = cls.start_flaeche

        BildSpeicher.lade_bild("unchecked", "bilder/unchecked.png")
        BildSpeicher.lade_bild("checked", "bilder/checked.png")
        BildSpeicher.lade_bild("pfeil_r_normal", "bilder/pfeil_r_normal.png")
        BildSpeicher.lade_bild("pfeil_r_aktiv", "bilder/pfeil_r_aktiv.png")
        BildSpeicher.lade_bild("pfeil_r_ueber", "bilder/pfeil_r_maus.png")
        BildSpeicher.lade_bild("ufos_und_schafe", "bilder/ufos_und_schafe.png")

        bilder = []
        for spiel in cls.geladene_spiele:
            BildSpeicher.lade_bild(spiel["bild"], "bilder/" + spiel["bild"])
            bilder.append(spiel["bild"])

        # Titelbild und Name des aktuellen Spiels anzeigen
        cls.aktuelles_spiel = cls.geladene_spiele[cls.aktuelles_spiel_index]
        cls.titel_text = Text(cls.aktuelles_spiel["name"], 0, 20, schrift=Schrift(60), farbe=BLAU)
        cls.titel_text.zentriere_horizontal()
        cls.titel_bild = BildWechsler(0, 80, bilder)
        cls.titel_bild.zentriere_horizontal()

        cls.cbLoeschen = CheckBox(40, 540, lambda gesetzt: TextUebersicht.fehler_muessen_korrigiert_werden(gesetzt))
        cls.cbGross = CheckBox(40, 580, lambda gesetzt: TextUebersicht.soll_woerter_gross_schreiben(gesetzt))


        schrift = Schrift(30, "freesansbold.ttf")
        schriftGross = Schrift(50, "freesansbold.ttf")

        Text("Großschreibung", cls.cbGross.x + 40, cls.cbGross.y + 10, schrift)
        Text("Fehler korrigieren", cls.cbLoeschen.x + 40, cls.cbLoeschen.y + 10, schrift)

        ktStart = KlickText(200, 200, "Start", cls.spiel_starten, schriftGross)
        ktStart.zentriere_horizontal()
        ktStart.abstand_unten = 25

        mitte = cls.titel_bild.mitte
        ktRechts = KlickText(0, mitte[1], " - ", lambda: cls.spiel_wechseln(-1), schriftGross)
        ktLinks = KlickText(0, mitte[1], " + ", lambda: cls.spiel_wechseln(1), schriftGross)
        ktLinks.abstand_rechts = 25
        ktRechts.abstand_links = 25

        cls.naechsteLektion = KlickText(0, mitte[1], " + ", lambda: cls.lektion_wechseln(1), schriftGross)
        cls.vorherigeLektion = KlickText(0, 600, " - ", lambda: cls.lektion_wechseln(-1), schriftGross)

        cls.lektionen_index = 0
        cls.lektionenText = Text("dd", 0, 500, schrift)
        cls.lektion_wechseln(0)

        RadioButtonGruppe(3)


        # b = BildWechsler(100, 40, ["pfeil_r_normal", "pfeil_r_ueber", "pfeil_r_aktiv"])

        Spiel.registriere_maus_gedrueckt(cls.__maus_unten)
        Spiel.registriere_maus_losgelassen(cls.__maus_oben)

        # Alte Standard wieder herstellen
        Spiel.standard_flaeche = alte_flaeche

    @classmethod
    def spiel_wechseln(cls, aenderung):

        cls.aktuelles_spiel_index += aenderung
        if cls.aktuelles_spiel_index == len(cls.geladene_spiele):
            cls.aktuelles_spiel_index = 0
        elif cls.aktuelles_spiel_index == -1:
            cls.aktuelles_spiel_index = len(cls.geladene_spiele) - 1

        cls.aktuelles_spiel = cls.geladene_spiele[cls.aktuelles_spiel_index]

        cls.titel_bild.zeige_bild(cls.aktuelles_spiel_index)
        cls.titel_text.setze_text(cls.aktuelles_spiel["name"])
        cls.titel_text.zentriere_horizontal()

    @classmethod
    def lektion_wechseln(cls, aenderung):

        cls.lektionen_index += aenderung
        cls.lektionen_index = max(0, min(len(LektionenUebersicht.gib_lektionen()) - 1, cls.lektionen_index))
        LektionenUebersicht.setze_lektion(cls.lektionen_index)

        cls.lektionenText.setze_text(LektionenUebersicht.gib_aktuelle_lektion().name)
        cls.lektionenText.zentriere_horizontal()
        cls.vorherigeLektion.setze_position(cls.lektionenText.x - 50, cls.lektionenText.y)
        cls.naechsteLektion.setze_position(cls.lektionenText.x + cls.lektionenText.breite + 18, cls.lektionenText.y)

    @classmethod
    def __maus_unten(cls, ereignis):
        for a in Anklickbar.gib_anklickbare():
            if a.punkt_test(ereignis.pos):
                a.maus_gedrueckt(ereignis)

    @staticmethod
    def __maus_oben(ereignis):
        for a in Anklickbar.gib_anklickbare():
            if a.punkt_test(ereignis.pos):
                a.maus_losgelassen(ereignis)

    @classmethod
    def spiel_starten(cls):
        # Lektion auswählen
        LektionenUebersicht.setze_lektion(cls.lektionen_index)

        _modul = __import__(cls.aktuelles_spiel["modul"], globals(), locals())
        _class = getattr(_modul, cls.aktuelles_spiel["haupt_klasse"])
        spiel_flaeche = ZeichenFlaeche(0, 0, (fenster_breite, spiel_hoehe, True), eltern_flaeche=cls.hintergrund_flaeche)
        spiel = _class(spiel_flaeche)

        # die Startseite entfernen
        cls.start_flaeche.selbst_entfernen()
        Spiel.registriere_maus_losgelassen(lambda e: None)
        Spiel.registriere_maus_gedrueckt(lambda e: None)

        def update(dt):
            spiel.aktualisiere(dt)

        cls.setze_aktualisierung(update)

        # Spielfläache hinzufügen, und spiel starten
        cls.gib_zeichen_flaeche().fuege_hinzu(cls.hintergrund_flaeche)
        cls.rahmen.nach_vorne()
        spiel.aufbauen()



if __name__ == "__main__":
    TTHaupt.initialisiere()
    TTHaupt.starten()
