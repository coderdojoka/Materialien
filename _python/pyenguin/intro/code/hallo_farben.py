# Importiert alle wichtigen pyenguin Befehle
from pyenguin import *

__author__ = 'Mark Weinreuter'

# Fenster mit Größe und Titel erstellen
fenster = Fenster(500, 900, "Hallo Farben")


# WAS SIND FARBEN? WIE WERDEN SIE DARGESTELLT?
# Farben besten aus 3 Farbwerten: Rot, Grün, Blau
# Mit einer 3er Kombinatation kann einen neue Farbe definiert werden

# Eine eigene Farbe anlegen!
meine_farbe = (234, 66, 234)


# ACHTUNG DER FOLGENDE CODE DIENT NUR ZUR AUSGABE DER VORHANDEN FARBEN
# ER IST ZUR VERWENDUNG VON FARBEN NICHT WICHTIG
FARBEN_NAMEN.append("meine_farbe")
schrift = Schrift(20)
y = 5

for name in sorted(FARBEN_NAMEN):

    # Für meine Farbe etwas abstand schaffen
    if name == "meine_farbe":
        y += 25

    # Farb name schreiben
    t = Text(name, schrift)
    t.oben = y
    t.links = 50

    # Farbe anzeigen
    r = Rechteck(240, y, 20, 20, globals()[name])

    # Farbe als Zahlen
    t2 = Text(str(globals()[name]), schrift)
    t2.oben = y
    t2.links = 270

    # Nächste Reihe berechnen
    y += 25

# Das Fenster anzeigen
fenster.starten()
