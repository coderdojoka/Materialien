__author__ = 'Mark Weinreuter'


class Mond:
    def __init__(self, name):
        # ALLLE VARIABLEN HIER ANLEGEN
        self.name = name
        self.planet = None  # Noch nicht bekannt

    # Spezialfunktion: Wird u.a. bei print(planet) aufgerufen
    def __str__(self):
        return "Mond: " + self.name
