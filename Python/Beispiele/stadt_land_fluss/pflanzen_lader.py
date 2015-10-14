__author__ = 'Mark Weinreuter'

# Zum Durchsuchen von HTML-Text.
# ACHTUNG: dieses Python-Paket muss installiert sein!!! Z.B. mittels 'pip install beautifulsoup4' in der Konsole
from bs4 import BeautifulSoup

from webseiten_helfer import *

url = "http://www.bio-gaertner.de/Pflanzen_Liste/"

datei = open("pflanzen.txt", "w")

# Die Webseite erlaubt Aufrufe über einzelne Buchstaben
for buchstabe in 'abcdefghijklmnopqrstuvwxyz':

    text = lade_webseite(url + buchstabe)

    # Text in HTML parsen
    html = BeautifulSoup(text, 'html.parser')

    # Wir lesen alle Einträge aus der Tabelle mit Pflanzenname, Botanischer Name, Kategorie und Pflanzenfamiilie
    # uns interessiert, allerdings nur der Name => jeden vierten Eintrag
    felder = html.select("td.views-field")[::4] 

    for feld in felder:
        # Text auslesen und Sonderzeichen entfernen
        pflanze = feld.text.strip()

        print(pflanze)

        datei.write(pflanze + "\n")



# Datei zum Schluss schließen
datei.close()
