__author__ = 'Mark Weinreuter'
import random

from pyenguin import *


# Diese Funktion wird aufgeruft, ca 30 mal pro Sekunde, um das Spiel zu aktualisieren
def aktualisiere(dt):
    # 1.) BALL UND BODEN

    # Ball berührt Boden => GameOver
    if ball.ist_unten_raus():
        gameOver()
        return

    # 2.) BALL UND BRETT

    if ball.ist_linksrechts_raus():
        ball.bewegung_x *= -1
        return

    if ball.ist_obenunten_raus():
        ball.bewegung_y *= -1
        return

    # Ball berührt Brett => abprallen
    # Wir wollen nur abprallen wenn wir von oben kommen => bewegung > 0
    # Ansonsten treten komische mehrfach abprall-effekte auf
    if ball.box_beruehrt(brett) and ball.bewegung_y > 0:
        ball.bewegung_y *= -1

        # Zufällige Änderung  im Bereich von -1 bis 1, um es ein wenig spannender zu gestalten
        aenderung = random.randint(0, 1) - .5
        ball.bewegung_x = aenderung

    # 2.) BALL UND BLOCK

    beruehrter_block = None
    for block in alle_bloecke:

        if ball.box_beruehrt(block):
            # ACHTUNG: es ist keine gute idee Element aus einer Liste innerhalb eine for-Schleife zu löschen!
            beruehrter_block = block
            break

    # Überprüfen ob ein Block getroffen wurde => entfernen, Ball abprallen lassen
    if beruehrter_block is not None:
        # Bewegungs richtung oben-unten umkehren
        ball.bewegung_y *= -1

        # Block löschen
        alle_bloecke.remove(beruehrter_block)
        # Vom Spiel entfernen
        beruehrter_block.entferne()

        # Alle Blöcke entfernt?
        if len(alle_bloecke) == 0:
            gewonnen()


def gameOver():
    text.setze_text("GameOver")
    text.zentriere()
    text.zeige()
    entferne_aktualisiere(aktualisiere)


def gewonnen():
    text.setze_text("Gewonnen")
    text.zentriere()
    text.zeige()
    entferne_aktualisiere(aktualisiere)


def links_gedrueckt(e):
    brett.bewegung_x = -brett_geschwindigkeit


def links_losgelassen(e):
    brett.bewegung_x = 0


def rechts_gedrueckt(e):
    brett.bewegung_x = brett_geschwindigkeit


def rechts_losgelassen(e):
    brett.bewegung_x = 0


def brett_bewegen(ges):
    # Brett mit gegebener Geschwindigkeit bewegen
    brett.aendere_position(ges, 0)

    # Fall der linke oder rechte Rand berührt wird setzen wir die Position
    # fest, damit wir nicht darüber hinaus fahren
    if brett.raus_links():
        brett.links = 0
    elif brett.ist_rechts_raus():
        brett.rechts = 0


# Spiel initialisierne mit Größe, Titel und Aktualisierungs-Funktion
fenster = Fenster(640, 480, "Blocks")
registriere_aktualisiere(aktualisiere)

brett_geschwindigkeit = .5
links_unten = False
rechts_unten = False

anzahl_breite = 6
anzahl_hoehe = 5
abstand = 5
block_breite = (fenster.breite - (anzahl_breite + 1) * abstand) / anzahl_breite
block_hoehe = 40

farben = [BLAU, LILA, ROT, GRUEN, GELB, ORANGE]
alle_bloecke = []

# Wir wollen anzahl_breite x anzahl_hoehe viele Blöcke erstellen
for reihe in range(0, anzahl_hoehe):
    for spalte in range(0, anzahl_breite):
        # Zufällige Farbe auswählen
        farb_index = random.randint(0, len(farben) - 1)
        zufalls_farbe = farben[farb_index]

        # Position des aktuellen Blocks berechnen... Eine Skizze hilft um die Berechnung zu verstehen :)
        x = abstand + spalte * (block_breite + abstand)
        y = abstand + reihe * (block_hoehe + abstand)

        # Neuen Block erstellen und in die Liste einfügen
        block = Rechteck(x, y, block_breite, block_hoehe, zufalls_farbe)
        alle_bloecke.append(block)

# Das Brett, dass wir bewegen
brett = Rechteck(270, 450, 60, 10, GRAU)

# Der Ball, Geschwindigkeit festlegen und automatisch vom Rand abprallen
ball = Kreis(250, 300, 12, ROT)
ball.bewegung_x = .1
ball.bewegung_y = .1

# Text für GameOver/Gewonnen erzeugen, aber noch verstecken
s = Schrift(60, "freesansbold")
text = Text("", s)
text.links = 2
text.oben = 2
text.verstecke()

# Tasten registrieren
registriere_taste_unten(T_LINKS, links_gedrueckt)
registriere_taste_unten(T_RECHTS, rechts_gedrueckt)
registriere_taste_unten(T_b, links_gedrueckt)
registriere_taste_unten(T_d, rechts_gedrueckt)
registriere_taste_oben(T_LINKS, links_losgelassen)
registriere_taste_oben(T_RECHTS, rechts_losgelassen)
fenster.starten()
