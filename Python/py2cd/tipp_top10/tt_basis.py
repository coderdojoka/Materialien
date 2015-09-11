from py2cd.spiel import Spiel
from tipp_top10.tt_text_anzeige import TextUebersicht

__author__ = 'Mark Weinreuter'


class TTBasis:
    def __init__(self, flaeche):
        # Die eigentliche Fläche auf der das Spiel gezeichnet wird
        self.flaeche = flaeche
        Spiel.standard_flaeche = self.flaeche

    @classmethod
    def neues_wort(cls, zeichenbares_objekt, x_offset, y_offset, wenn_komplett):
        ta = TextUebersicht.neuer_text(x_offset, y_offset, wenn_komplett)
        zeichenbares_objekt.position_geaendert = lambda: ta.setze_position(*zeichenbares_objekt.position())
        return ta

    def aufbauen(self):
        raise NotImplementedError("Muss implementiert werden.")

    def abbauen(self):
        raise NotImplementedError("Muss implementiert werden.")

    def aktualisiere(self, delta):
        raise NotImplementedError("Muss implementiert werden.")
