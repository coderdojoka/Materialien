__author__ = 'Mark Weinreuter'

# Zum Laden von Webseite
import urllib.request

# Zum Durchsuchen von HTML-Text.
# ACHTUNG: dieses Python-Paket muss installiert sein!!! Z.B. mittels 'pip install beautifulsoup4' in der Konsole
from bs4 import BeautifulSoup


# Lädt den HTML-Text einer Webseite
def lade_webseite(url):
    html = ""

    # Alle Fehler abfangen bei ungültigen Urls
    try:

        with urllib.request.urlopen(url) as response:
            html = response.read()

    except Exception as e:
        print("Fehler beim Laden:", e)

    return html


def lade_fluesse():

    # Wikipedia hat eine Liste von Flüssen gesammelt
    url = "https://de.wikipedia.org/w/index.php?title=Liste_von_Fl%C3%BCssen_in_Deutschland&oldid=145628822"

    text = lade_webseite(url)
    html = BeautifulSoup(text, 'html.parser')

    # Es gibt viel ul-Tags auf der Webseite durch Ausprobieren ermittelt, dass 8-11 die wichtigen sind :)
    eintraege = html.find_all("ul")[8:11]

    alle_fluesse = []

    for e in eintraege:

        # Alle li-Tags filtern
        liste = e.find_all("li")

        # Text aus allen li-Tags lesen
        for li in liste:
            text = li.text

            # Die Flüsse sind kodiert in Länge - Name - Extras
            # Der Name ist als der 1 Eintrage nach Split am Trennstrich
            name = text.split("–")[1]
            alle_fluesse.append(name.strip())

    print("%d Flüsse gefunden" % len(alle_fluesse))

    # Flüsse speichern
    datei = open("deutsche_fluesse.txt", "w")

    for fluss in alle_fluesse:
        datei.write(fluss + "\r\n") # Namen und Zeilenumbruch speichern

    datei.close()


def lade_staedte():

    # Hier finden wir freundlicherweise deutsche Städte nach Buchstaben sortiert
    url = "http://home.meinestadt.de/deutschland/staedteliste/"

    alle_staedte = []

    # Alle Buchstaben durchgehen und einzeln die Städte-Liste von der Webseite abfragen
    for buchstabe in "abcdefghijklmnopqrstuvwxyz":

        # Alle Städte mit buchstabe beginnen
        text = lade_webseite(url + buchstabe)
        html = BeautifulSoup(text, 'html.parser')

        # im HTML-Text der Webseite sind die Städte so kodiert:
        # < li class ="ms-citylist-item" > < a href="http://home.meinestadt.de/aach-trier" > Aachen < / a > < / li >
        # Also brauchen wir alle li-Tags mit der Klasse ms-citylist-item und darin die a-Tags
        liste = html.select("li.ms-citylist-item a")

        print(len(liste), "Städte gefunden mit: " + buchstabe)

        # Alle Eintrage durchgehen und den Text auslesen
        for e in liste:
            stadt = e.text.strip()
            alle_staedte.append(stadt)

    print("%d Städte gefunden" % len(alle_staedte))

    # Städte speichern
    datei = open("deutsche_staedte.txt", "w")

    for stadt in alle_staedte:
        datei.write(stadt + "\r\n")

    datei.close()


# Fluesse und Städte laden
lade_fluesse()
lade_staedte()