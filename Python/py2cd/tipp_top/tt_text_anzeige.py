from py2cd.rechteck import Rechteck
from py2cd.text import Text, Schrift
from tipp_top.tt_lektionen import LektionenUebersicht

__author__ = 'Mark Weinreuter'


class TextUebersicht:
    texte = []
    aktueller_text = None
    fehler_anzahl = 0
    richtig_anzahl = 0
    fehler_korrigieren = True
    fehler_muss_korrigiert_werden = False
    """
    :type:TextAnzeige
    """

    @staticmethod
    def neuer_text(x_offset, y_offset, wenn_komplett):
        wort = LektionenUebersicht.aktuelle_lektion.gib_wort()
        ta = TextAnzeige(wort, x_offset, y_offset, wenn_komplett)
        TextUebersicht.texte.append(ta)

        return ta

    @staticmethod
    def buchstabe_getippt(buchstabe):

        # Falls wir einen Fehler gemacht haben muss er korrigiert werden
        if TextUebersicht.fehler_muss_korrigiert_werden:
            return

            # aktuellen Text ermitteln
        if TextUebersicht.aktueller_text is None:
            for ta in TextUebersicht.texte:
                if ta.text[0] == buchstabe:
                    TextUebersicht.aktueller_text = ta
                    break

        # Falls kein Text vorhanden Tippfehler
        if TextUebersicht.aktueller_text is None:
            TextUebersicht.fehler_anzahl += 1
            return

        # Überprüfen ob der Buchstabe der richtige war
        ergebnis = TextUebersicht.aktueller_text.buchstabe_getippt(buchstabe)

        if ergebnis == 0:
            TextUebersicht.aktueller_text.entfernen()
            TextUebersicht.texte.remove(TextUebersicht.aktueller_text)
            TextUebersicht.aktueller_text = None
        elif ergebnis == -1:
            TextUebersicht.fehler_anzahl += 1
            TextUebersicht.fehler_muss_korrigiert_werden = TextUebersicht.fehler_korrigieren
        else:
            TextUebersicht.richtig_anzahl += 1

    @staticmethod
    def buchstabe_loeschen():
        if TextUebersicht.fehler_muss_korrigiert_werden:
            TextUebersicht.fehler_muss_korrigiert_werden = False
            TextUebersicht.aktueller_text.normale_auswahl_farbe()
        pass

    @staticmethod
    def text_nicht_geschafft(ta):
        TextUebersicht.texte.remove(ta)
        if TextUebersicht.aktueller_text == ta:
            TextUebersicht.aktueller_text = None

        ta.aufraeumen()


class TextAnzeige:
    standard_schrift = Schrift(40)
    zeichen_laenge = 8
    zeichen_auswahl_farbe = (255, 170, 0, 80),
    zeichen_fehler_farbe = (255, 120, 120, 80)
    hintergrund_farbe = (230, 230, 230, 80)

    def __init__(self, text, x_offset=0, y_offset=0, wenn_komplett=lambda: None):
        self.text = text
        self.__x = 0
        self.__y = 0
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.position = 0
        self.wenn_komplett = wenn_komplett
        self.auswahl_text = Text(text[self.position], 0, 0, TextAnzeige.standard_schrift,
                                 hintergrund=TextAnzeige.hintergrund_farbe)
        laenge = min(len(text[self.position:]), TextAnzeige.zeichen_laenge)
        self.text_feld = Text(text[self.position + 1:self.position + laenge], self.auswahl_text.breite, 0,
                              TextAnzeige.standard_schrift)

        self.hintergrund = Rechteck(0, 0, self.text_feld.breite + self.auswahl_text.breite,
                                    self.text_feld.hoehe, farbe=TextAnzeige.hintergrund_farbe)
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
        self.hintergrund._aendere_groesse(self.text_feld.breite + self.auswahl_text.breite, self.text_feld.hoehe)
        self.text_feld.setze_position(self.__x + self.auswahl_text.breite, self.__y)
        return 1

    def setze_position(self, x, y):
        self.__x = x + self.x_offset
        self.__y = y + self.y_offset
        self.hintergrund.setze_position(self.__x, self.__y)
        self.auswahl_text.setze_position(self.__x, self.__y)
        self.text_feld.setze_position(self.__x + self.auswahl_text.breite, self.__y)

    def aufraeumen(self):
        self.hintergrund.entferne()
        self.text_feld.entferne()
        self.auswahl_text.entferne()

    def entfernen(self):
        self.aufraeumen()
        self.wenn_komplett()
