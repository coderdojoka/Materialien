import os
import sys

from pyenguin import *

from algorithmus import Algorithmus
from gui_spielfeld import SpielFeld, FARBEN

sys.path.append(os.path.join(os.path.dirname(__file__), "algos"))

__author__ = "Mark Weinreuter"

if len(sys.argv) < 3:
    a1 = input("Algo1 (z.B. liner.Liner): ")
    a2 = input("Algo2 (z.B. zufall.Zufall1): ")
else:
    a1 = sys.argv[1]
    a2 = sys.argv[2]

if len(a1) < 3:
    a1 = "liner.Liner"
if len(a2) < 3:
    a2 = "d3stRoy3r.D3strRoy3r"

m1, n1 = a1.split(".")
m2, n2 = a2.split(".")


W = 900
H = 900
fenster = Fenster(W, H, "dotWars")
Algorithmus.SCHLAF_ZEIT = .001
delta = 0

INTRO_ENDE = 20
spielfeld = None


def intro_ende():
    entferne_aktualisiere(hintergrund)
    introSzene.verstecke()
    spielSzene.zeige()
    txt_start.zeige()

def init_runde(x,y,e):
    global spielfeld
    txt_start.verstecke()
    spielfeld = SpielFeld(m1, n1, m2, n2)
    spielfeld.flaeche.zeige()
    registriere_aktualisiere(spiel_aktualisiere)
    spielfeld.flaeche.wechsle_szene(spielSzene)
    fenster.darf_beendet_werden = spielfeld.beenden

    spielfeld.start()


def hintergrund(dt):
    global delta
    delta += dt

    if delta > INTRO_ENDE:
        intro_ende()

    if ((delta * .5) % 200) < 100:
        introSzene.farbe = ORANGE
        text.setze_farbe(WEISS)
        text2.setze_farbe(SCHWARZ)
    else:
        introSzene.farbe = MATT_BLAU
        text.setze_farbe(SCHWARZ)
        text2.setze_farbe(WEISS)


MAX_RUNDEN = 5
runde = 1
punkte1 = 0
punkte2 = 0


def beenden():
    global punkte1, punkte2
    zeige_neue_punkte()

    if spielfeld.punkte[0] > spielfeld.punkte[1]:
        txt_runde.setze_text(n1 + " gewinnt!")
    else:
        txt_runde.setze_text(n2 + " gewinnt!")


def naechste_runde():
    global runde, punkte1, punkte2
    entferne_aktualisiere(spiel_aktualisiere)

    if spielfeld.punkte[0] > spielfeld.punkte[1]:
        punkte1 += 1
    else:
        punkte2 += 1

    if runde == MAX_RUNDEN:
        beenden()
    else:
        runde += 1
        zeige_neue_punkte()
        txt_start.zeige()
        txt_start.nach_vorne()


def spiel_aktualisiere(delta):
    spielfeld.aktualisiere()

    # Texte aktualisieren
    txt_runde.setze_text("Runde: " + str(runde))
    txt_spieler1.setze_text(spielfeld.algo1.name + ":  " + str(spielfeld.punkte[0]))
    txt_spieler2.setze_text(spielfeld.algo2.name + ":  " + str(spielfeld.punkte[1]))

    txt_spieler1.abstand_links = 20
    txt_spieler1.abstand_unten = 70
    txt_spieler2.abstand_unten = 20
    txt_spieler2.abstand_links = 20

    if not spielfeld.laueft_noch():
        naechste_runde()


def zeige_neue_punkte():
    txt_runde.setze_text("Runde " + str(runde))
    txt_runde.zentriere_breite()
    txt_runde.oben = 20
    txt_punkte1.setze_text(str(punkte1))
    txt_punkte2.setze_text(str(punkte2))
    txt_punkte1.abstand_rechts = 20
    txt_punkte1.abstand_unten = 70
    txt_punkte2.abstand_unten = 20
    txt_punkte2.abstand_rechts = 20


# Intro Texte, etc
introSzene = Szene(W, H)
schrift = Schrift(50)
text = Text("Willkommen zur epischen", schrift)
text2 = Text("Schlacht zwischen rot und blau!", schrift)
text.zentriere()
text2.zentriere_breite()
text2.oben = text.unten
text.wechsle_szene(introSzene)
text2.wechsle_szene(introSzene)

# Spieltexte
schrift = Schrift(30)
spielSzene = Szene(W, H, farbe=MATT_GRUEN)
txt_runde = Text("Runde " + str(runde), Schrift(90), farbe=WEISS)
txt_spieler1 = Text("", schrift, farbe=FARBEN[0])
txt_spieler2 = Text("", schrift, farbe=FARBEN[1])
txt_punkte1 = Text("0", schrift, farbe=FARBEN[0])
txt_punkte2 = Text("0", schrift, farbe=FARBEN[1])
txt_start = Text("Start", Schrift(60), farbe=WEISS, hintergrund=MATT_GRUEN)


txt_spieler1.wechsle_szene(spielSzene)
txt_spieler2.wechsle_szene(spielSzene)
txt_runde.wechsle_szene(spielSzene)
txt_punkte1.wechsle_szene(spielSzene)
txt_punkte2.wechsle_szene(spielSzene)
txt_start.wechsle_szene(spielSzene)
txt_start.zentriere()
txt_start.setze_bei_maus_klick(init_runde)


zeige_neue_punkte()

spielSzene.verstecke()

registriere_aktualisiere(hintergrund)

fenster.starten()
