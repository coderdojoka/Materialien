__author__ = 'Mark Weinreuter'

from collections import defaultdict
import random
import json

from py2cd.farben import TRANSPARENT, ROT
from py2cd.text import Text, Schrift


class TextUebersicht:
    max_buchstaben = 3
    __max_buchstaben_grenze = 16
    __alle_texte = []
    aktueller_text = None
    fehler_anzahl = 0
    richtig_anzahl = 0
    fehler_korrigieren = False
    __woerter_komplett = 0
    __gross_schreiben = False
    __fehler_muss_korrigiert_werden = False
    punkte_geaendert = lambda x: None
    """
    :type:TextAnzeige
    """

    @classmethod
    def fehler_muessen_korrigiert_werden(cls, wert):
        cls.__fehler_muss_korrigiert_werden = wert

    @classmethod
    def soll_woerter_gross_schreiben(cls, wert):
        cls.__gross_schreiben = wert

    @classmethod
    def woerter_gross_schreiben(cls):
        return cls.__gross_schreiben

    @staticmethod
    def neuer_text(x_offset, y_offset, wenn_komplett):
        wort = LektionenUebersicht.gib_aktuelle_lektion().gib_wort()
        ta = TextAnzeige(wort, x_offset, y_offset, wenn_komplett)
        TextUebersicht.__alle_texte.append(ta)

        return ta

    @staticmethod
    def buchstabe_getippt(buchstabe):

        # Falls wir einen Fehler gemacht haben muss er korrigiert werden
        if TextUebersicht.__fehler_muss_korrigiert_werden:
            return

            # aktuellen Text ermitteln
        if TextUebersicht.aktueller_text is None:
            for ta in TextUebersicht.__alle_texte:
                if ta.text[0] == buchstabe:
                    TextUebersicht.aktueller_text = ta
                    ta.nach_vorne()
                    break

        # Falls kein Text vorhanden Tippfehler
        if TextUebersicht.aktueller_text is None:
            TextUebersicht.fehler_anzahl += 1
            return

        # Überprüfen ob der Buchstabe der richtige war
        ergebnis = TextUebersicht.aktueller_text.buchstabe_getippt(buchstabe)

        if ergebnis == 0:
            TextUebersicht.punkte_geaendert(len(TextUebersicht.aktueller_text.text))
            TextUebersicht.aktueller_text.entfernen()
            TextUebersicht.__alle_texte.remove(TextUebersicht.aktueller_text)
            TextUebersicht.aktueller_text = None
            TextUebersicht.__woerter_komplett += 1
            if TextUebersicht.__woerter_komplett > TextUebersicht.__max_buchstaben_grenze:
                TextUebersicht.max_buchstaben += 1
                TextUebersicht.__max_buchstaben_grenze *= 2

        elif ergebnis == -1:
            TextUebersicht.fehler_anzahl += 1
            TextUebersicht.__fehler_muss_korrigiert_werden = TextUebersicht.fehler_korrigieren
        else:
            TextUebersicht.richtig_anzahl += 1

    @staticmethod
    def buchstabe_loeschen():
        if TextUebersicht.__fehler_muss_korrigiert_werden:
            TextUebersicht.__fehler_muss_korrigiert_werden = False
            if TextUebersicht.aktueller_text is not None:
                TextUebersicht.aktueller_text.normale_auswahl_farbe()

    @staticmethod
    def text_nicht_geschafft(ta):
        TextUebersicht.__alle_texte.remove(ta)
        if TextUebersicht.aktueller_text == ta:
            TextUebersicht.aktueller_text = None

        ta.aufraeumen()


class TextAnzeige:
    standard_schrift = Schrift(40)
    zeichen_laenge = 8
    zeichen_auswahl_farbe = (255, 170, 0, 80),
    zeichen_fehler_farbe = (255, 120, 120, 80)
    hintergrund_farbe = TRANSPARENT

    def __init__(self, text, x_offset=0, y_offset=0, wenn_komplett=lambda: None):
        self.text = text
        self.__x = 0
        self.__y = 0
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.position = 0
        self.wenn_komplett = wenn_komplett
        self.auswahl_text = Text(text[self.position], 0, 0, TextAnzeige.standard_schrift)
        laenge = min(len(text[self.position:]), TextAnzeige.zeichen_laenge)

        self.text_feld = Text(text[self.position + 1:self.position + laenge], 0, 0,
                              TextAnzeige.standard_schrift, ROT)

        # self.hintergrund = Rechteck(0, 0, self.text_feld.breite + self.auswahl_text.breite,
        # self.text_feld.hoehe, farbe=TextAnzeige.hintergrund_farbe)

        # self.hintergrund.entferne()
        self.text_feld.nach_vorne()
        self.auswahl_text.nach_vorne()
        self.setze_position(self.__x, self.__y)

    def normale_auswahl_farbe(self):
        self.auswahl_text.hintergrund = TextAnzeige.zeichen_auswahl_farbe

    def buchstabe_getippt(self, buchstabe):
        if self.text[self.position] != buchstabe:
            self.auswahl_text.hintergrund = TextAnzeige.zeichen_fehler_farbe
            return -1

        self.position += 1
        if self.position == len(self.text):
            return 0

        self.auswahl_text.hintergrund = TextAnzeige.zeichen_auswahl_farbe

        self.auswahl_text.setze_text(self.text[self.position])
        laenge = min(len(self.text[self.position:]), TextAnzeige.zeichen_laenge)
        self.text_feld.setze_text(self.text[self.position + 1:self.position + laenge])
        #  self.hintergrund._aendere_groesse(self.text_feld.breite + self.auswahl_text.breite, self.text_feld.hoehe)
        self.text_feld.setze_position(self.__x + self.auswahl_text.breite, self.__y)
        return 1

    def setze_position(self, x, y):
        self.__x = x + self.x_offset
        self.__y = y + self.y_offset
        #  self.hintergrund.setze_position(self.__x, self.__y)
        self.auswahl_text.setze_position(self.__x, self.__y)
        self.text_feld.setze_position(self.__x + self.auswahl_text.breite, self.__y)

    def aufraeumen(self):
        #   self.hintergrund.entferne()
        self.text_feld.selbst_entfernen()
        self.auswahl_text.selbst_entfernen()

    def nach_vorne(self):
        #   self.hintergrund.nach_vorne()
        self.text_feld.nach_vorne()
        self.auswahl_text.nach_vorne()

    def entfernen(self):
        self.aufraeumen()
        self.wenn_komplett()


class LektionenUebersicht:
    __lektionen = []
    __aktuelle_lektion = None

    @classmethod
    def gib_lektionen(cls):
        return cls.__lektionen

    @classmethod
    def setze_lektion(cls, index):
        cls.__aktuelle_lektion = cls.__lektionen[index]

    @staticmethod
    def lade_lektionen():
        with  open("lektionen.json") as datei:
            text = datei.read()

        lektionen_json = json.loads(text)
        lektionen_info = lektionen_json["lektionen"]
        datei_name = lektionen_json["datei_name"]

        anzahl_lektionen = len(lektionen_info)

        LektionenUebersicht.__lektionen = []

        for i in range(anzahl_lektionen):
            datei = open(datei_name % i)

            woerter = defaultdict(list)
            for zeile in datei:
                zeile = zeile.strip()
                woerter[len(zeile)].append(zeile)
            datei.close()

            for key in woerter:
                woerter[key] = sorted(woerter[key])

            woerter[1] = list(lektionen_info[i]["buchstaben"])
            LektionenUebersicht.__lektionen.append(
                Lektion(lektionen_info[i]["name"], woerter, lektionen_info[i]["sonderzeichen"]))

        LektionenUebersicht.__aktuelle_lektion = LektionenUebersicht.__lektionen[0]

    @classmethod
    def gib_aktuelle_lektion(cls):
        return cls.__aktuelle_lektion


class Lektion:
    def __init__(self, name, woerter, sonderzeichen):
        self.name = name
        self.woerter = woerter
        self.sonderzeichen = sonderzeichen
        self.anzahl_sonderzeichen = len(sonderzeichen) - 1

    def gib_wort(self, laenge=-1):
        if laenge == -1:
            laenge = random.randint(1, min(TextUebersicht.max_buchstaben, len(self.woerter) - 1))

        # Ein Wort auswählen
        woerter = self.woerter[laenge]
        index = random.randint(0, len(woerter) - 1)
        wort = woerter[index]

        if self.anzahl_sonderzeichen > 0 and random.randint(0, 4) == 1:
            wort += self.sonderzeichen[random.randint(0, self.anzahl_sonderzeichen)]

        if TextUebersicht.woerter_gross_schreiben() and random.randint(0, 2) == 1:
            wort = wort.capitalize()

        return wort
