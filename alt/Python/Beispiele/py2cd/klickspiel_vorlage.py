__author__ = 'Ricarda Trumpf'

# Diese zwei Zeilen werden immer benötigt, um py2cd zu importieren
from py2cd import *
from py2cd.farben import *
import random
import time


def aktualisiere(delta):
    #Text zum Zeit anzeigen
    ...
    #
    pass


def neuer_kreis():
    #male den Kreis an eine zufällige Stelle
    ...
    #Tipps:
    # mit kreis.setze_position(x,y) wird der Kreis "kreis" an die Stelle (x,y) verschoben
    # um den Kreis an eine zufällige Stelle zu malen muessen zwei Zufallszahlen
    # mit random.randint(0,max) erstellt werden


def auf_kreis(a):
    # ueberpruefe ob Mausklick auf Kreis

    #Tipps:
    # es gibt dazu eine Funktion, die das ueberprueft:
    # so wird sie aufgerufen: kreis.punkt_in_rechteck(a.pos)

    #Tipps:
    # du brauchst eine if-Abfrage
    # wenn der Kreis getroffen ist muessen drei Dinge passieren:
    # 1. es muss ein neuer Kreis gezeichnet werden
    # 2. die Punkte muessen um eins erhoeht werden
    # 3. der Text, der die Punkte anzeigt, muss geaendert werden


# So wird das Fenster fuer dein Spiel erstellt:
Spiel.init(400, 400, "Klickspiel", aktualisiere)
# Die ersten beiden Zahlen sind für die Breite und Höhe des Fensters,
# der Text in Anfuehrungszeichen ist der Name des Fensters
# und am Ende steht noch, das die "aktualisiere"-Funktion aufgerufen werden soll

# Ab hier gehts mit dem Spiel los:

#erstelle als erstes einen Kreis, mit einer x- und einer y- Koordinate, einem Radius und einer Farbe:
#ein Kreis wird mit Kreis(x,y,radius,farbe) erstellt
kreis =
#erstelle eine Variable zum zaehlen der Punkte (setzte sie auf 0)
...
#erstelle mit Text("text",x,y) einen Text in deinem Spiel an der Stelle (x,y)
#als Text soll dort stehen Punkte: 0
text =
#um die Zeit zu stoppen koennen wir noch eine Uhr einbauen
#die Funktion time.time() gibt uns die Anzahl an Sekunden seit dem 01.01.1971
#hier muss die Startzeit ermittel und in eine Variable geschrieben werden:

#Wie für die Punkte brauchen wir dann wieder einen Text:
text_time =

#damit das Spiel auch spielbar wird brauchen wir etwas das
#ueberprueft ob wir die Maustaste gedrueckt haben
Spiel.registriere_maus_gedrueckt(auf_kreis)#diese Funktion macht das fuer uns!
#ihr muss als Argument, also in die Klammern, eine Funktion uebergeben werden
#in unserem Fall heißt diese auf_kreis

#jetzt musst du nur noch oben die drei Funktionen
# aktualisiere
# auf_kreis
# neuer_kreis
#ausfuellen

# Dan kannst du das Spiel starten:
Spiel.starten()

# Du hast es geschafft! Probiere aus ob alles Funktioniert!
# rechtsklick und Run "klickspiel_vorlage"
