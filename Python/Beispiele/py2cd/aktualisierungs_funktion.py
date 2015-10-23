__author__ = 'Mark Weinreuter'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *

def aktualisiere(delta):
    print("Wird ca. 30 mal pro Sekunde ausgeführt.")
    # Die Box um 1 pixel verschieben
    box.aendere_position(1, 1)


# Initialisiert das Fenster
Spiel.init(400, 400, "Steuere das Rechteck!", aktualisiere)

# So kann man die Aktualisierungsfunktion ändern
Spiel.setze_aktualisierung(aktualisiere)

box = Rechteck(10, 10, 50, 50, ROT)
print(box.x, box.y)

# Das Spiel starten
Spiel.starten()
