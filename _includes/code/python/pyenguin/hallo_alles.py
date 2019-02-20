__author__ = 'Mark Weinreuter'

# Importiert alle wichtigen pyenguin Befehle
from pyenguin import *

# Fenster mit Größe und Titel erstellen
fenster = Fenster(400, 400, "Hallo Position")

meineFarbe = (255, 0, 0)
k1 = Kreis(390, 110, 100, MATT_GRUEN)

k1.setze_position(200, 200)
r1 = Rechteck(20, 20, 200, 200, SCHWARZ, dicke=3)
r1.setze_position(200, 200)

l1 = Rechteck(185, 199, 30, 3, ROT)
l2 = Rechteck(199, 185, 3, 30, ROT)

f = Flaeche(100, 100)
f.fuelle(BLAU)
f.rechteck(10, 10, 50, 50, ROT)
f.kreis(10, 10, 25, GELB)
f.text("Hallo", 10, 70, Schrift(20), HELL_GRUEN)
f.linie(75, 10, 75, 90, ROT)
f.oval(15, 20, 20, 10, HELL_GRUEN)
f.vieleck([(80, 80), (90, 80), (85, 90)], HELL_ROT)
f.zentriere()

fenster.zeichne_gitter()


# fenster.setze_fenster_titel("Mein Fenster")


# Diese Funtion wird wiederholt aufgerufen
def aktualisiere(dt):
    print("aktualisiere")


def leer_gedrueckt(taste):
    print("Leertaste gedrückt.")


# Leertaste 'T_LEER', an die Rückruffunktion binden
registriere_taste_unten(T_LEER, leer_gedrueckt)


def leer_losgelassen(taste):
    print("Leertaste losgelassen.")


# Leertaste 'T_LEER', an die Rückruffunktion binden
registriere_taste_oben(T_LEER, leer_losgelassen)

# Aktualisierungsfunktion bekannt machen
registriere_aktualisiere(aktualisiere)
entferne_aktualisiere(aktualisiere)
# Das Fenster anzeigen
fenster.starten()
