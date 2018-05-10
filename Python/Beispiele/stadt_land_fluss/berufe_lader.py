__author__ = 'Mark Weinreuter'

from bs4 import BeautifulSoup
from webseiten_helfer import lade_webseite

# Zum Laden von Webseite
import http.cookiejar



def extrahiere_berufe(html):
    #  nach folgenden Tags suhen
    werte = html.select("td.daten a")

    zaehler = 0

    for wert in werte:
        # den Text des a-Tags
        beruf = wert.text.strip()

        # Nicht alle Tags enthalten auch Berufsnamen
        if len(beruf) > 0:

            # Beruf + Zeilenumbruch
            datei.write(beruf + "\n")
            zaehler += 1

    return zaehler


def lade_berufe():

    # Da die Webseite Cookies verwendet, benutzen wir unser CookieJar
    cj = http.cookiejar.CookieJar()

    # Die Webseite zuerst laden, um unser Cookie zu bekommen :D
    url_start = "http://berufenet.arbeitsagentur.de/berufe/"
    lade_webseite(url_start, cj)

    # Alle Buchstaben durchgehen
    for buchstabe in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':

        url = "http://berufenet.arbeitsagentur.de/berufe/alphaSearch.do?alphaCaps=" + buchstabe
        text = lade_webseite(url, cj)

        # Text in HTML parsen
        html = BeautifulSoup(text, 'html.parser')

        links = html.select("td.linksa1")[-1]
        seiten = links.find_all('a', )[:-1]
        print("Seiten: ", len(seiten) + 1)

        # Erste pagination seite lesen
        zaehler = extrahiere_berufe(html)

        # Alle anderen seiten laden
        for i in range(1, 1 + len(seiten)):
            text = lade_webseite("http://berufenet.arbeitsagentur.de/berufe/resultList.do?_pgnt_act=goToAnyPage&_pgnt_pn=%d&_pgnt_id=resultList" % i,
                                 cj)

            html = BeautifulSoup(text, 'html.parser')
            zaehler += extrahiere_berufe(html)

        print("%d Berufe mit: %s" % (zaehler, buchstabe))

# Datei zum Schreiben öffnen
datei = open("berufe.txt", "w")

lade_berufe()

# Alle Buchstaben gecheckt => Datei schließen
datei.close()
