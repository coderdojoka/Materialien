# Importiert alle wichtigen pyenguin Befehle
from pyenguin import *

__author__ = 'Mark Weinreuter'

# Fenster mit Größe und Titel erstellen
fenster = Fenster(640, 480, "Hallo Formen")

# Rechteck, Mitte bei: 50x25, Größe: 100x50 in Blau
r = Rechteck(50, 25, 100, 50, BLAU)

# Kreis, Mitte bei 100x200 mit Radius 50 in Grün
k = Kreis(100, 200, 50, GRUEN)

# Oval, Mitte bei: 400x100, Radius_breite, Radius_höhe: 60x50
o = Oval(400, 100, 60, 50, BRAUN)

# Ein Form über ihre Eckpunkte angeben (hier ein Dreieck)
punkte = ((200, 50), (300, 50), (250, 100))
d = Vieleck(punkte, ROT)

# Eine Linie von (200,200) nach (450, 350)
l = Linie(200, 200, 450, 350, ROT)

# Ein Form über ihre Eckpunkte angeben (Raute)
punkte = ((200, 350), (300, 250), (400, 350), (300, 450))
r = Vieleck(punkte, GELB)

# Hilfslinien einzeichnen
fenster.zeichne_gitter()

# Das Fenster anzeigen
fenster.starten()
