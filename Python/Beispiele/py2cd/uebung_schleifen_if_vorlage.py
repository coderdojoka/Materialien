__author__ = 'Ricarda Trumpf'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *
import random
import time


# So wird das Fenster fuer dein Spiel erstellt:
Spiel.init(400, 400, "Klickspiel")
# Die ersten beiden Zahlen sind für die Breite und Höhe des Fensters,
# der Text in Anfuehrungszeichen ist der Name des Fensters
# und am Ende steht noch, das die "aktualisiere"-Funktion aufgerufen werden soll

# Ab hier gehts mit der Uebung los:

#male mehrere Kreise in einer Reihe:

for spalte in range(8):#Schleife mit 8 Wiederhohlungen
    
    # male hier die Kreise mit Kreis(x,y,Radius,Farbe)
    # wie schaffst du es, das jeder Kreis an einer anderen Stelle ist?

"""
#male mehrere Kreise in mehreren Reihen:
for spalte in range(8):
    for reihe in range(8):
        # male hier die Kreise mit Kreis(x,y,Radius,Farbe)
        # wie schaffst du es, das jeder Kreis an einer anderen Stelle und einer anderen Reihe ist?

#male mehrere Kreise in mehreren Reihen:
#male jeden 3. Kreis andersfarbig (Verwende if und else

for spalte in range(8):
    for reihe in range(8):



#erstelle ein Schachbrettmuster
#Aendere Kreis(x,y,Radius,Farbe) in Rechteck(x,y,Breite,Hoehe,Farbe)

for spalte in range(8):
    for reihe in range(8):


"""



# Dan kannst du das Spiel starten:
Spiel.starten()

# Du hast es geschafft! Probiere aus ob alles Funktioniert!
# rechtsklick und Run "klickspiel_vorlage"
