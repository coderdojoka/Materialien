__author__ = 'Mark Weinreuter'

import random

from py2cd import *
from py2cd.farben import *

# Der erste Schritt, um ein Spiel zu starten ist immer, init() aufzurufen
Spiel.init(640, 480, "Mein Spiel")


def aktualisiere(dt):
    # alle Kreise durchgehen, bei Randberührung löschen -> in einer Liste speichern,
    # da aus einer for-Schleife nicht gelöscht werden darf!
    kreise_zu_loeschen = []

    # alle Blöcke bewegen
    for block in bloecke:
        block.bewege(dt)

        # Falls ein Block unsere Box berührt, ist das Spiel vorbei
        if block.beruehrt_objekt(box):
            # Spiel vorbei
            t = Text("Game Over", schrift=Schrift(50))
            t.zentriere()
            Spiel.entferne_aktualisierung()

        # Blöcke werden am unteren Rand zurücksetzen
        if block.beruehrt_unteren_rand():
            block.setze_position(random.randint(0, Spiel.breite - 20), 0)

    # alle Kreise bewegen und auf Kollisionen überprüfen
    for kreis in kreise:

        kreis.bewege(dt)
        for block in bloecke:
            if kreis.beruehrt_objekt(block):
                # Block zurücksetzen
                block.setze_position(random.randint(0, Spiel.breite - 20), 0)

        if kreis.beruehrt_oberen_rand():
            kreise_zu_loeschen.append(kreis)

    # Jetzt alle zu löschen gemerkten Kreise löschen
    for kreis in kreise_zu_loeschen:
        kreise.remove(kreis)
        kreis.selbst_entfernen()


# Diese Funktion wird aufgerufen, wenn die Leertaste gedrückt wird
def leer_gedrueckt(unten, pyg_ereignis):
    if unten:
        print("Leertaste gedrückt.")
        # Neuer Kreis. Setze dessen Mitte auf die Box-Mitte
        k = Kreis(0, 0, 10, BLAU)
        k.setze_geschwindigkeit(0, -8)
        k.mitte = box.mitte
        kreise.append(k)
    else:
        print("Leertaste losgelassen.")


# Aufgerufen solange die linke Pfeiltaste gedrückt ist
def solange_links(dt):
    box.aendere_position(-7 * dt, 0)


# Aufgerufen solange die rechte Pfeiltaste gedrückt ist
def solage_rechts(dt):
    box.aendere_position(7 * dt, 0)


def neuer_block():
    # Die x-Position und Fallgeschwindikeit zufällig wählen
    x = random.randint(0, Spiel.breite - 20)
    y_ges = random.randint(2, 4)

    block = Rechteck(x, 0, 20, 20, GRUEN)
    block.setze_geschwindigkeit(0, y_ges)
    bloecke.append(block)


bloecke = []
kreise = []

# ein gelbes Rechteckt, die Spielfigur
box = Rechteck(270, 200, 40, 40, ROT)
box.zentriere_horizontal()
box.unten = 25

for i in range(10):  # Zehn Blöcke generieren
    neuer_block()

# Tastendruck-Funktion registrieren
Spiel.registriere_taste_gedrueckt(T_LEER, leer_gedrueckt)
# Taste-Unten-Funktionen registrieren
Spiel.registriere_solange_taste_unten(T_RECHTS, solage_rechts)
Spiel.registriere_solange_taste_unten(T_LINKS, solange_links)

Spiel.zeichne_gitter()  # Hilfsgitter anzeigen
Spiel.setze_aktualisierung(aktualisiere)
Spiel.starten()
