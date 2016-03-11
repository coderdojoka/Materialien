__author__ = 'Ricarda Trumpf'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *
import random
import time

farbe = [WEISS,SCHWARZ,ROT,GRUEN,GELB,BLAU,HELL_GELB,HELL_GRUEN,ORANGE]
# So wird das Fenster fuer dein Spiel erstellt:
Spiel.init(400, 400, "Klickspiel")
# Die ersten beiden Zahlen sind für die Breite und Höhe des Fensters,
# der Text in Anfuehrungszeichen ist der Name des Fensters
# und am Ende steht noch, das die "aktualisiere"-Funktion aufgerufen werden soll

# Ab hier gehts mit der Uebung los:

for i in range(1000):
    Kreis(random.randint(0,400), random.randint(0,400), random.randint(5,30), farbe[random.randint(0,8)])
"""
#male mehrere Kreise in einer Reihe:

for i in range(8):
    Kreis(i*50,50,10,ROT)

#male mehrere Kreise in mehreren Reihen:

for i in range(8):
    for j in range(8):
        Kreis(i*50,j*50,10,ROT)


#male mehrere Kreise in mehreren Reihen:
#male jeden 3. Kreis andersfarbig

for i in range(8):
    for j in range(8):

        if (i+j)%3 == 0:
             Kreis(i*50,j*50,10,GRUEN)
        else:
            Kreis(i*50,j*50,10,ROT)


#erstelle ein Schachbrettmuster


for i in range(8):
    for j in range(8):
        g = (i+j)%2
        Rechteck(i*50,j*50,50,50,farbe[g])



"""

# Dan kannst du das Spiel starten:
Spiel.starten()

# Du hast es geschafft! Probiere aus ob alles Funktioniert!
# rechtsklick und Run "klickspiel_vorlage"
