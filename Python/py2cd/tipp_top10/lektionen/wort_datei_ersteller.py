__author__ = 'Mark Weinreuter'

eingabe_datei = "german.dic"

datei = open(eingabe_datei)
zeilen = []
# Einmal alles einlesen bitte :D
for zeile in datei:
    zeilen.append(zeile.lower().strip())
datei.close()


lektionen = ["asdfjklö", "en", "ri", "th", "cu", "g", "om", "bw", "z", "vp", "üä", "ßq", "yx"]
datei_name = "woerter_lektion_"
datei_ende = ".txt"
bekannt = ""
max_laenge = 11

for zahl, lektion in enumerate(lektionen):

    bekannt += lektion

    schreib_datei = open(datei_name + str(zahl) + datei_ende, "w")

    for zeile in zeilen:

        # Nur Wörter einer maximalen Länge erlauben
        if len(zeile) > max_laenge:
            continue

        # Ein Wort ist geeignet, falls es mindestens einen Buchstaben aus dieser Lektion enthält
        geeignet = False
        for buchstabe in lektion:
            if buchstabe in zeile:
                geeignet = True
                break

        if not geeignet:
            continue

        # Es dürfen auch nur bereits bekannte Buchstaben vorkommen
        geeignet = True
        for buchstabe in zeile:
            if buchstabe not in bekannt:
                geeignet = False
                break

        # Falls alle Kriterien passen, schreiben wir es in die datei
        if geeignet:
            schreib_datei.write(str(zeile) + "\n")

    schreib_datei.close()


# Alle Dateien nochmal öffnen und sortieren
for i in range(len(lektionen)):
    datei = open(datei_name + str(i) + datei_ende, "r")
    zeilen = datei.readlines()
    datei.close()

    datei = open(datei_name + str(i) + datei_ende, "w")
    zeilen = sorted(zeilen, key=len)

    for zeile in zeilen:
        datei.write(zeile)
    datei.close()

