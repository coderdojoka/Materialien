__author__ = 'Mark Weinreuter'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *

# Initialisiert das Fenster
Spiel.init(400, 400, "Bewegung")

# 1.) Am Anfang die linken obere Ecke angeben: 10, 10
box = Rechteck(10, 10, 50, 50, ROT)

# 2.) Mit links, rechts, oben, unten kann der Abstand zum jeweiligen Rand
# festgelegt werden, z.B. platziert:
# box.unten = 5 die Box-Unterkante 5 Pixel vom Boden entfernt

# 20 Pixel vom rechten Rand entfernt (ändert die x-Koordinate)
box.rechts = 20
# 20 Pixel vom linken Rand entfernt (ändert die x-Koordinate)
box.links = 20
# 20 Pixel vom oberen Rand entfernt (ändert die y-Koordinate) 
box.oben = 20 
# 20 Pixel vom unteren Rand entfernt (ändert die y-Koordinate)
box.unten = 20 

# den Mittelpunkt des Objekts auf 20,30 setzen
box.mitte = (20, 30)

kreis = Kreis(10, 100, 100, BLAU)

# Zentriert das Objekt horizontal (ändert die x-Koordinate)
kreis.zentriere_horizontal()

# Zentriert das Objekt vertikal (ändert die y-Koordinate)
kreis.zentriere_horizontal()

# Zentriert das Objekt mittig  (ändert die x- und y-Koordinate)
kreis.zentriere()

box = Rechteck(10, 10, 100, 100, GELB)

# Abstand zum linken Rand
abstand = box.links
print(abstand)

# Abstand zum rechten Rand
abstand = box.rechts
print(abstand)

# Abstand zum oberen Rand
abstand = box.oben
print(abstand)

# Abstand zum unteren Rand
abstand = box.unten
print(abstand)

# Mittelpunkt abfragen, ein Tupel mit (mitte_x, mitte_y)
mitte = box.mitte
print(mitte)

# Breite des umgebenden Rechtecks abfragen
breite = box.breite
print(breite)

# Höhe des umgebenden Rechtecks abfragen
hoehe = box.hoehe
print(hoehe)


# Das Spiel starten
Spiel.starten()
