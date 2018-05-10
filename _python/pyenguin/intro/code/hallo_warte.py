# Importiert alle wichtigen pyenguin Befehle
from pyenguin import *

__author__ = 'Mark Weinreuter'

# Fenster mit Größe und Titel erstellen
fenster = Fenster(600, 500, "Hallo Warte")

# eine bemalbare Fläche
f = Flaeche(200, 200)
# Postion setzen
f.links = 100
f.oben = 100

# Auf dieser Fläche können wir nun malen!

# Fläche in dieser Farbe übermalen
f.fuelle(HELL_GRUEN)

# Auf dieser Fläche malen.
# WICHTIG: Koordinaten beziehen sich auf die Fläche
f.rechteck(40, 40, 100, 50, BLAU)

# Was nicht auf die Fläche passt, wird nicht gezeichnet!
# Kreis mit linker oberer Ecke bei 150x150, die Fläche
# ist allerdings nur 200x200 breit => passt nicht ganz drauf
f.kreis(150, 150, 50, HELL_ROT)

f.text("Hallo Text", 40, 150, Schrift(20))

# Das Fenster anzeigen
fenster.starten()
