import random

# Liest die Anzahl der Schleifendurchläufe
durchlaeufe = int(input("Wie viele Durchläufe? "))

# Setze Anzahl Treffer zurück
treffer = 0

for i in range(0, durchlaeufe):
    # Erzeuge zwei Zufallszahlen
    zahl1 = random.random()
    zahl2 = random.random()

    # Ist der Punkt aus zahl1 und zahl2 im Kreis, dann ist es ein Treffer
    if ((zahl1 * zahl1) + (zahl2 * zahl2)) < 1:
        treffer = treffer + 1

# Gebe die Zahl Pi aus
print("Die Zahl Pi ist ungefähr:", 4 * treffer / durchlaeufe)
