__author__ = 'Mark Weinreuter'
import random

from py2cd import *
from py2cd.farben import *
# Wird benötigt, um die Tasten Konstanten: K_LEFT, ... zu importieren
from pygame.constants import *


# Diese Funktion wird aufgeruft, ca 30 mal pro Sekunde, um das Spiel zu aktualisieren
def aktualisiere(dt):
    # Tastendrücke untersuchen
    if links_unten:
        brett_bewegen(-brett_geschwindigkeit * dt)
    elif rechts_unten:
        brett_bewegen(brett_geschwindigkeit * dt)

    # 1.) BALL UND BODEN

    # Ball berührt Boden => GameOver
    if ball.beruehrt_unteren_rand():
        gameOver()
        return


    # 2.) BALL UND BRETT

    # Ball berührt Brett => abprallen
    # Wir wollen nur abprallen wenn wir von oben kommen => bewegung > 0
    # Ansonsten tretten komische mehrfach abprall-effekte auf
    if ball.beruehrt_objekt(brett) and ball.y_geschwindigkeit > 0:
        ball.y_bewegung_umkehren()

        # Zufällige Änderung  im Bereich von -1 bis 1, um es ein wenig spannender zu gestalten
        aenderung = random.randint(0, 2) - 1
        ball.aendere_geschwindigkeit(aenderung, 0)


    # 2.) BALL UND BLOCK

    beruehrter_block = None
    for block in alle_bloecke:

        if ball.beruehrt_objekt(block):
            # ACHTUNG: es ist keine gute idee Element aus einer Liste innerhalb eine for-Schleife zu löschen!
            beruehrter_block = block
            break

    # Überprüfen ob ein Block getroffen wurde => entfernen, Ball abprallen lassen
    if beruehrter_block is not None:
        # Bewegungs richtung oben-unten umkehren
        ball.y_bewegung_umkehren()

        # Block löschen
        alle_bloecke.remove(beruehrter_block)
        # Vom Spiel entfernen
        beruehrter_block.selbst_entfernen()

        # Alle Blöcke entfernt?
        if len(alle_bloecke) == 0:
            gewonnen()


    # Den Ball einen Schritt weiter bewegen
    ball.bewege()


def gameOver():
    text.setze_text("GameOver")
    text.zentriere()
    text.zeige()
    Spiel.entferne_aktualisierung()


def gewonnen():
    text.setze_text("Gewonnen")
    text.zentriere()
    text.zeige()
    Spiel.entferne_aktualisierung()


def links_gedrueckt(unten, e):
    global links_unten
    links_unten = unten


def rechts_gedrueckt(unten, e):
    global rechts_unten
    rechts_unten = unten


def brett_bewegen(ges):
    # Brett mit gegebener Geschwindigkeit bewegen
    brett.aendere_position(ges, 0)

    # Fall der linke oder rechte Rand berührt wird setzen wir die Position
    # fest, damit wir nicht darüber hinaus fahren
    if brett.beruehrt_linken_rand():
        brett.links = 0
    elif brett.beruehrt_rechten_rand():
        brett.rechts = 0


# Spiel initialisierne mit Größe, Titel und Aktualisierungs-Funktion
Spiel.init(640, 480, "Blocks", aktualisiere)

brett_geschwindigkeit = 12
links_unten = False
rechts_unten = False

anzahl_breite = 6
anzahl_hoehe = 5
abstand = 5
block_breite = (Spiel.breite - (anzahl_breite + 1) * abstand) / anzahl_breite
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
ball = Kreis(250, 400, 12)
ball.setze_geschwindigkeit(8, 8)
ball.pralle_vom_rand_ab(True)

# Text für GameOver/Gewonnen erzeugen, aber noch verstecken
s = Schrift(60, "freesansbold")
text = Text("", 0, 0, s)
text.verstecke()

# Tasten registrieren
Spiel.registriere_taste_gedrueckt(K_LEFT, links_gedrueckt)
Spiel.registriere_taste_gedrueckt(K_RIGHT, rechts_gedrueckt)
Spiel.registriere_taste_gedrueckt(K_a, links_gedrueckt)
Spiel.registriere_taste_gedrueckt(K_d, rechts_gedrueckt)

Spiel.starten()
