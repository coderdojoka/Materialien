import math

__author__ = 'Mark Weinreuter'


class Planet:
    # Spezialfunktion: Wird beim Erstellen aufgerufen
    def __init__(self, name, radius_in_km):
        # ALLLE VARIABLEN HIER ANLEGEN
        self.name = name
        self.radius = radius_in_km
        self.monde = []

    def berechne_volumen(self):
        # VARIABLEN INTERN MIT SELF.XY verwenden

        # Annahme: Planet ist eine Kugel
        return 4 / 3 * math.pi * self.radius * self.radius * self.radius

    def fuege_mond_hinzu(self, mond):
        # Falls neuer Mond, füge hinzu
        if mond not in self.monde:
            self.monde.append(mond)

        # Verweis auf den Planet setzen
        mond.planet = self

    def gib_monde_aus(self):
        print("Alle Monde: ")
        for mond in self.monde:
            print(mond)
        else:  # Wird ausgeführt, falls die for-Schleife nie ausgeführt wird
            print("Keine")

        # Leerzeile
        print()

    # Spezialfunktion: Wird u.a. bei print(planet) aufgerufen
    def __str__(self):
        return "Planet: %s hat %d Mond(e)" % (self.name, len(self.monde))
