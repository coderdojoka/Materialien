__author__ = 'Mark Weinreuter'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *

# Der erste Schritt, um ein Spiel zu starten ist immer, init() aufzurufen
Spiel.init(640, 480, "Mein Spiel")
# Erstellt ein neues Fenster mit der gegebenen Größe von 640x480
# und dem Titel 'Mein Spiel'

# ein neues Rechteckt mit Position 270x200 und Größe 100x100 in gelb
haus = Rechteck(270, 200, 100, 100, GELB)

# ein Polygon mit den Ecken aus der Liste und der Farbe Rot
dach = Polygon([(270, 200), (320, 160), (370, 200)], ROT)

# ein neues Rechteck mit Position 320x200 und Größe: 30x50 in grün
tuer = Rechteck(320, 250, 30, 50, GRUEN)

# Eine Linie zwischen den gegeben Punkten in Rot und 2 Pixel dick
boden = Linie((100, 300), (550, 300), ROT, 2)

# Hilfsgitter anzeigen
Spiel.zeichne_gitter()

# Startet das Spiel. Dies muss immer die letze Zeile sein
Spiel.starten()
