__author__ = 'Mark Weinreuter'

import random
import json


class LektionenUebersicht:
    lektionen = []
    aktuelle_lektion = None

    @staticmethod
    def lade_lektionen():
        with  open("lektionen.json") as datei:
            text = datei.read()

        lektionen_json = json.loads(text)
        lektionen_info = lektionen_json["lektionen"]
        datei_name = lektionen_json["datei_name"]

        anzahl_lektionen = len(lektionen_info)

        LektionenUebersicht.lektionen = []

        for i in range(anzahl_lektionen):
            datei = open(datei_name % i)

            woerter  = []
            for zeile in datei:
                woerter.append(zeile.strip())

            datei.close()
            LektionenUebersicht.lektionen.append(Lektion(lektionen_info[i]["buchstaben"], lektionen_info[i]["sonderzeichen"], woerter=woerter))

        LektionenUebersicht.aktuelle_lektion = LektionenUebersicht.lektionen[0]


class Lektion:
    def __init__(self, buchstaben, sonderzeichen, woerter):
        self.buchstaben = buchstaben
        self.sonderzeichen = sonderzeichen
        self.woerter = woerter
        self.anzahl_woerter = len(self.woerter) -1

    def gib_wort(self):
        return self.woerter[random.randint(0, self.anzahl_woerter)]
