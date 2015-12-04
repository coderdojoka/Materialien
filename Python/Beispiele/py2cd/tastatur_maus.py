__author__ = 'Mark Weinreuter'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *

# Der erste Schritt, um ein Spiel zu starten ist immer, init() aufzurufen
Spiel.init(640, 480, "Mein Spiel")

# Für die Tasten benötigen wir diesen 'import'
from pygame.constants import *

# ein gelbes Rechteckt
box = Rechteck(270, 200, 100, 100, GELB)

# Diese Funktion wird aufgerufen, wenn die linke Pfeiltaste gedrückt wird
def links_gedrueckt(unten, event):

    if unten:
        print("Links gedrückt.")
        box.aendere_position(-5, 0)
    else:
        print("Links losgelassen.")


Spiel.registriere_taste_gedrueckt(K_LEFT, links_gedrueckt)






# Hilfsgitter anzeigen
Spiel.zeichne_gitter()

# Startet das Spiel. Dies muss immer die letze Zeile sein
Spiel.starten()
