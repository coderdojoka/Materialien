__author__ = 'Mark Weinreuter'

from py2cd.flaeche import ZeichenFlaeche, neue_pygame_flaeche
from py2cd.rechteck import Rechteck
from py2cd.spiel import *
from tipp_top.wort_sammlung import TextAnzeige, TextUebersicht

from tipp_top.tt_tastatur import *


def aktualisiere(dt):
    pass


fenster_breite = 800
fenster_hoehe = 670
tastatur_hoehe = 270

Spiel.init(fenster_breite, fenster_hoehe, "TippTop10", aktualisiere)
zf = Spiel.gib_zeichen_flaeche()

tastatur_flaeche = ZeichenFlaeche(0, fenster_hoehe - tastatur_hoehe,
                                  neue_pygame_flaeche(788, tastatur_hoehe, True), eltern_flaeche=zf)

spiel_flaeche = ZeichenFlaeche(0, 0, neue_pygame_flaeche(fenster_breite, fenster_hoehe-tastatur_hoehe, True), eltern_flaeche=zf)
tastatur_flaeche.zentriere_horizontal()

# Tastatur erstellen
initialisiere_tasten(tastatur_flaeche)

# Nur auf dieser Fläche zeichnen
Spiel.standard_flaeche = spiel_flaeche

Rechteck(0, 0, spiel_flaeche.breite, spiel_flaeche.hoehe, SCHWARZ,dicke=1)

TextUebersicht.neuer_text()


def taste_gedrueckt(unten, ereignis):
    global text
    if unten:
        tasten[ereignis.key].gedrueckt()
        if ereignis.key == K_BACKSPACE:
            TextUebersicht.buchstabe_loeschen()
        else:
            TextUebersicht.buchstabe_getippt(ereignis.unicode)
    else:
        tasten[ereignis.key].losgelassen()


for key in tasten:
    Spiel.registriere_taste_gedrueckt(key, taste_gedrueckt)

Spiel.starten()
