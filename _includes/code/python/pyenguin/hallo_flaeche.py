# Importiert alle wichtigen pyenguin Befehle
from pyenguin import *

__author__ = 'Mark Weinreuter'

# Fenster mit Größe und Titel erstellen
fenster = Fenster(600, 300, "Hallo Warte")

# eine bemalbare Fläche
f = Flaeche(100, 100)


def zeit_um():
    # global, da wir die Variable von oben in dieser Funktion ändern
    global farbe

    # Zwischen rot und grün umschalten
    if farbe == ROT:
        farbe = GRUEN
    else:
        farbe = ROT

    # Fläche mit neuer Farbe füllen
    f.fuelle(farbe)


# Alle 1000 ms = 1s führe Funktion zeit_um aus
w = Warte(1000, zeit_um, wiederhole=True)

# Das Fenster anzeigen
fenster.starten()
