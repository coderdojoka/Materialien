# Importiert alle wichtigen pyenguin Befehle
from pyenguin import *

__author__ = 'Mark Weinreuter'

# Fenster mit Größe und Titel erstellen
fenster = Fenster(460, 460, "Hallo Fenster")

# Ein blaues Rechteck. Mitte bei: 200x200, Größe: 60x60
r = Rechteck(200, 200, 60, 60, BLAU)

# Das Fenster anzeigen
fenster.starten()
