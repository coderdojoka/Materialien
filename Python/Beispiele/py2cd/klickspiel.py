__author__ = 'Mark Weinreuter'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *
import random
import time


def aktualisiere(delta):
    text_time.setze_text("Zeit in s: " + str(round(time.time() - stime,2)))


def neuer_kreis():
    kreis.setze_position(random.randint(0, 360), random.randint(0, 360))


def auf_kreis(a):
    global punkte
    if kreis.punkt_in_rechteck(a.pos):
        neuer_kreis()
        punkte += 1
        text.setze_text("Punkte: " + str(punkte))


# Initialisiert das Fenster
Spiel.init(400, 400, "Bewegung", aktualisiere)

kreis = Kreis(random.randint(0, 360), random.randint(0, 360), 20, ROT)
punkte = 0
stime = time.time()
text = Text("Punkte: " + str(punkte), 0, 0)
text_time = Text("Zeit in s: " + str(time.time() - stime), 300, 0)
Spiel.registriere_maus_gedrueckt(auf_kreis)

# Das Spiel starten
Spiel.starten()
