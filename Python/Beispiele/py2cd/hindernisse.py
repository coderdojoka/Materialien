__author__ = 'Mark Weinreuter'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd.farben import *

from py2cd import *


# Der erste Schritt, um ein Spiel zu starten ist immer, init() aufzurufen
Spiel.init(640, 480, "Hindernislauf")
# Erstellt ein neues Fenster mit der gegebenen Größe von 640x480
# und dem Titel 'Mein Spiel'

punkte = [(50, 70), (150, 100), (250, 175), (150, 275)]
h1 = Polygon(punkte, BLAU)

punkte = [(350, 70), (275, 100), (300, 175), (350, 275)]
h2 = Polygon(punkte, BLAU)

r1 = Rechteck(425, 125, 50, 125, BLAU)

punkte = [(500, 50), (550, 400), (575, 400), (520, 50)]
h3 = Polygon(punkte, BLAU)

start = Kreis(40, 190, 10, ROT)
ziel = Kreis(590, 140, 10, GRUEN)

Spiel.zeichne_gitter()


# Startet das Spiel. Dies muss immer die letze Zeile sein
Spiel.starten()
