__author__ = "Mark Weinreuter"

from py2cd import *
from py2cd.farben import *

# Der erste Schritt um ein Spiel zu starten ist immer, der Initialisierungsfunktion init()
Spiel.init(640, 480, "Mein Spiel")
# Erstellt ein neues Fenster mit der gegebenen Größe von 640x480 und dem Titel "Mein Spiel"

Spiel.fps = 30  # Setzt die Neuzeichnungsrate auf 30mal pro Sekunde. (Diese Anweisung ist optional, da 30 der Standartwert ist)

"""
Ein Spiel (Programme im Allgemeinen) zeichnen wiederholt "Bilder" auf den Bildschirm. Je nach Anwendung wird der
Bildschirm unterschiedlich oft aktualisiert.
Die Aktualisierungsrate wird als oftmals als "Frames per second", kurz "fps" bezeichnet.
Übersetzt bedeutet dies einfach "Neuzeichnung pro Sekunde".
Folglich hat die Anweisung: 'Spiel.fps = 60', die Bedeutung, dass das Spiel 60mal pro Sekunde neugezeichnet wird.
Bei Spielen ist als grobe Grenze gesetzt, dass es gut mit 60 Fps läuft.
Für das menschliche Auge reicht es allerdings auch aus sicherzustellen, das ein Spiel zumindest noch mit 30 Fps läuft,
da ab diesen Wert die einzelnen Bilder nicht mehr unterscheiden werden können.
"""


# Diese Funktion wird aufgerufen wenn die Maus bewegt wurde
def maus_bewegt(evt):
    if reckt.punkt_in_rechteck(evt.pos):
        reckt.farbe = GRUEN
    else:
        reckt.farbe = GELB


bewegung_x = 4
bewegung_y = 4


# Diese Funktion wird aufgerufen, wenn das Spiel aktualisiert wird
def aktualisiere_spiel(delta):
    global bewegung_x, bewegung_y

    if box.x <= 0:
        bewegung_x *= -1

    elif box.breite + box.x >= Spiel.breite:
        bewegung_x *= -1

    if box.y <= 0:
        bewegung_y *= -1

    elif box.hoehe + box.y >= Spiel.hoehe:
        bewegung_y *= -1

    # bewege die Box
    box.aendere_position(bewegung_x, bewegung_y)

reckt = Rechteck(270, 200, 100, 100,  GELB)

dreieck = Polygon([(270, 300), (320, 340), (370, 300)],  ROT)

box = Rechteck(10, 10, 50, 50,  GRUEN)

# Funktion die aufgerufen wird, wenn die Maus bewegt wurde
Spiel.registriere_maus_bewegt(maus_bewegt)

# Funktion die aufgerufen wird, wenn das Spiel aktualisiert wird (fps mal)
Spiel.setze_aktualisierung(aktualisiere_spiel)

Spiel.starten()
"""
Um das Spiel zu starten, muss Spiel.start() aufgerufen werden. Dies sollte immer die letzte Anweisung sein.
"""
