from py2cd.rechteck import Rechteck
from py2cd.text import Text, Schrift

__author__ = 'Mark Weinreuter'


class TextUebersicht:
    texte = []
    aktueller_text = None
    fehler_anzahl = 0
    richtig_anzahl = 0

    """
    :type:TextAnzeige
    """

    @staticmethod
    def neuer_text():
        ta = TextAnzeige("bubber")
        TextUebersicht.texte.append(ta)

    @staticmethod
    def buchstabe_getippt(buchstabe):
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
            TextUebersicht.neuer_text()
        elif ergebnis == -1:
            TextUebersicht.fehler_anzahl += 1
        else:
            TextUebersicht.richtig_anzahl += 1

    @classmethod
    def buchstabe_loeschen(cls):
        pass


class TextAnzeige:
    standard_schrift = Schrift(40)
    zeichen_laenge = 8
    zeichen_auswahl_farbe = (255, 170, 0, 80),
    zeichen_fehler_farbe = (255, 120, 120, 80)

    def __init__(self, text, x_offset=0, y_offset=0):
        self.text = text
        self.position = 0
        self.auswahl_text = Text(text[self.position], 0, 0, TextAnzeige.standard_schrift,
                                 hintergrund=TextAnzeige.zeichen_auswahl_farbe)
        laenge = min(len(text[self.position:]), TextAnzeige.zeichen_laenge)
        self.text_feld = Text(text[self.position + 1:self.position + laenge], self.auswahl_text.breite, 0,
                              TextAnzeige.standard_schrift)

        self.hintergrund = Rechteck(0, 0, self.text_feld.breite + self.auswahl_text.breite,
                                    self.text_feld.hoehe, farbe=(230, 230, 230, 80))
        self.text_feld.nach_vorne()
        self.auswahl_text.nach_vorne()
        self.position_geaendert(50, 200)

    def buchstabe_getippt(self, buchstabe):
        if self.text[self.position] != buchstabe:
            return -1

        self.position += 1
        if self.position == len(self.text):
            return 0

        self.auswahl_text.setze_text(self.text[self.position])
        laenge = min(len(self.text[self.position:]), TextAnzeige.zeichen_laenge)
        self.text_feld.setze_text(self.text[self.position + 1:self.position + laenge])
        self.hintergrund._aendere_groesse(self.text_feld.breite + self.auswahl_text.breite, self.text_feld.hoehe)
        return 1

    def position_geaendert(self, x, y):
        self.hintergrund.setze_position(x, y)
        self.auswahl_text.setze_position(x, y)
        self.text_feld.setze_position(x + self.auswahl_text.breite, y)

    def entfernen(self):
        self.hintergrund.entferne()
        self.text_feld.entferne()
        self.auswahl_text.entferne()
