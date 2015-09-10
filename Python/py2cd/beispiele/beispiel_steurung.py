__author__ = 'Mark Weinreuter'

from py2cd.spiel import *
from py2cd.kreis import Kreis
from py2cd.text import Schrift, Text
from py2cd.rechteck import Rechteck
from py2cd.farben import *

links_down = False
rechts_down = False
oben_down = False
unten_down = False
speed = 3.1
ball_x = speed - 1
ball_y = speed


def aktualisiere(dt):
    global ball_x, ball_y

    # Überprüfen ob der Ball die Kanten berührt
    if ball.beruehrt_linken_oder_rechten_rand():
        ball_x *= -1

    if ball.beruehrt_oberen_oder_unteren_rand():
        ball_y *= -1

    # Ball bewegen
    ball.aendere_position(ball_x * dt, ball_y * dt)


    # Welche Tasten sind gedrückt?
    if links_down:
        rechteck.aendere_position(-speed * dt, 0)

    if rechts_down:
        rechteck.aendere_position(speed * dt, 0)

    if oben_down:
        rechteck.aendere_position(0, -speed * dt)

    if unten_down:
        rechteck.aendere_position(0, speed * dt)


    # Kollision der zwei Rechtecke überprüfen
    beruehrt = rechteck.beruehrt_umgebendes_rechteck(kollision)
    if beruehrt:
        kollision.farbe = ROT
    else:
        kollision.farbe = GELB


# Diese Funktionen werden aufgerufen, wenn die entsprechende Taste gedrückt wird
def links(gedrueckt, e):
    global links_down
    links_down = gedrueckt


def rechts(gedrueckt, e):
    global rechts_down
    rechts_down = gedrueckt


def oben(gedrueckt, e):
    global oben_down
    oben_down = gedrueckt


def unten(gedrueckt, e):
    global unten_down
    unten_down = gedrueckt

# Initialisiert das Fenster
Spiel.init(400, 400, "Steuere das Rechteck!", aktualisiere)

# Zwei Rechtecke erstellen
rechteck = Rechteck(40, 160, 40, 40, BLAU)
kollision = Rechteck(50, 40, 60, 40, ROT)

# Einen Text anzeigen
schrift = Schrift(20)
t = Text("wasd zum bewegen", 0, 10, schrift, GRAU)

# 5 Pixel vom rechten Rand plazieren
t.abstand_rechts = 5

ball = Kreis(10, 10, 20, GRUEN)

# Tastendrücke-Funktionen registrien. Wird die Taste K_a = 'a' gedrückt, so wird die
# Funktion mit dem Namen links aufgerufen
Spiel.registriere_taste_gedrueckt(K_a, links)
Spiel.registriere_taste_gedrueckt(K_w, oben)
Spiel.registriere_taste_gedrueckt(K_s, unten)
Spiel.registriere_taste_gedrueckt(K_d, rechts)


# Das Spiel starten
Spiel.starten()