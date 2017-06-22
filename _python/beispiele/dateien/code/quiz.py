import os
from random import randint

from datei_helfer import *

__author__ = 'Mark Weinreuter'

datei_name = "quiz_1.txt"
besten_liste_name = "bestenliste.txt"

# Zeilen aus der Fragen-Datei einlesen als Liste
zeilen = lese_datei_zeilen(datei_name)

# Pro Frage 3 Antwormöglichkeiten + 1 richtige Antwort
anzahl_fragen = len(zeilen) // 5

besten_liste = []

# Bestenliste einlesen, falls schon eine Datei vorhanden
if os.path.exists(besten_liste_name):
    besten_liste = lese_datei_zeilen(besten_liste_name)

richtig = 0
while anzahl_fragen > 0:

    # Frage auswählen
    frage_index = randint(0, anzahl_fragen - 1) * 5
    # Frage + Antwortmöglichkeiten ausgeben
    for i in range(0, 4):
        print(zeilen[frage_index + i])

    # richtige Antwort laden und Benutzer-Antwort einlesen
    richtige_antwort = zeilen[frage_index + 4]
    antwort = input("Deine Antwort? ")

    if richtige_antwort == antwort:
        print("Richtig!!!")
        richtig += 1
    else:
        print("Das ist leider falsch :(")

    # Leerzeile
    print()

    # Frage löschen. Genauer Teil der Liste entfernen
    zeilen[frage_index:frage_index + 5] = []
    anzahl_fragen -= 1

# In Bestenliste eintragen
name = input("Wie heißt du? ")
eintrag = str(richtig) + " Punkte: " + name
besten_liste.append(eintrag)

# Bestenliste sortieren. ACHTUNG: Schwarze Python-Magie...
besten_liste = sorted(besten_liste, reverse=True, key=lambda z: int(z.split(" Punkte: ")[0]))

# 10 besten ausgeben
for zeile in besten_liste[0:10]:
    print(zeile)

# Bestenliste speichern
schreibe_datei_zeilen(besten_liste_name, besten_liste)
