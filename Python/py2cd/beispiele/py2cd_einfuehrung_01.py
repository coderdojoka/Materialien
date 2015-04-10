# Hack um py2cd im PythonPfad bekannt zu machen
import sys
from py2cd.linie import Linie
from py2cd.poly import Polygon

sys.path.append('..')

from py2cd.spiel import Spiel
from py2cd.farben import *
from py2cd.text import Schrift, Text
from py2cd.rechteck import Rechteck


"""
             ____         _
 _ __  _   _|___ \ ___ __| |
| '_ \| | | | __) / __/ _` |
| |_) | |_| |/ __/ (_| (_| |
| .__/ \__, |_____\___\__,_|
|_|    |___/


py2cd ist ein (hoffentlich) einfach zu verwendendes "2D-Framework".

Es können graphische Objekte, wie Rechtecke, Linien, Kreise, Polygone gezeichnet werden.
Außerdem wird das Anzeigen von Bilder und Animationen, als schnelle Abfolge von Bilder angeboten.


"""


# Der erste Schritt um ein Spiel zu starten ist immer, der Initialisierungsfunktion init()
Spiel.init(640, 480, "Mein Spiel")
"""Erstellt ein neues Fenster mit der gegebenen Größe von 640x480 und dem Titel "Mein Spiel"
"""

# ein neues Rechteckt mit Position 270x200 und Größe 100x100 mit Farbe Gelb
haus = Rechteck(270, 200, 100, 100, GELB)

linie = Linie((100, 200), (540, 200), ROT, 2)  # Eine Linie zwischen den gegeben Punkten in Rot und 2 Pixel dick


# ein Polygon mit den Ecken aus der Liste und der Farbe Rot
dach = Polygon([(270, 300), (320, 340), (370, 300)],ROT)

# ein neues Rechteck mit Position 320x200 und Größe: 30x50 in grün
tuer = Rechteck(320, 200, 30, 50, GRUEN)

text = Text("Hallo Welt", 0, 0, Schrift(20))  # Text an der Stelle 0x0 mit einer Schrift in der Größe: 20

# setzt die Position an die gegebene Stelle: oben mittig mit Abstand 10 pixel vom Rand
text.setze_position((Spiel.breite - text.dimension.breite)/2, Spiel.hoehe - text.dimension.hoehe - 10)

Spiel.starten()
"""
Um das Spiel zu starten, muss Spiel.start() aufgerufen werden. Dies sollte immer die letzte Anweisung sein!
"""