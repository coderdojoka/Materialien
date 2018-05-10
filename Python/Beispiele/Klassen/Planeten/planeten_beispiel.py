__author__ = 'Mark Weinreuter'

# Wichtig! Die Klassen importieren
from mond import Mond
from planet import Planet

# Eine Instanz unserer Klasse anlegen
erde = Planet("Erde", 6378.15)
mars = Planet("Mars", 3397)

# Instanzen unsere Mond-Klasse
erdmond = Mond("ErdMond")
phobos = Mond("Phobos")
deimos = Mond("Deimos")

print(erde)
erde.gib_monde_aus()

# Monde hinzufügen
erde.fuege_mond_hinzu(erdmond)
mars.fuege_mond_hinzu(phobos)
mars.fuege_mond_hinzu(deimos)

print(erde)
erde.gib_monde_aus()

volMars = mars.berechne_volumen()
print("Mars hat ein errechnetes Volumen von:    %d" % volMars)
print("Laut Wikipedia hat Mars ein Volumen von: %d" % 1631400000000)  # Da ist eine 0 zu viel?? :)

# Zu Welchem Planet gehört der Mond?
print("Phobos gehört zu: ", phobos.planet.name)
# Mit dem Punkt-Operator kann man die Variablen eines Objektes abfragen
# Diese Variablen können selbst wieder Objekte sein!
# Man kann den Punkt-Operator auf diese Objekte weiter anwenden

ersterMond = mars.monde[0]

# Wir können Objekte ganz normal vergleichen
if ersterMond == phobos:
    print(phobos.name, "ist der erste Mond von", mars.name)
