import random
# generiert eine Zufallszahl zwischen 1 und 100
zufallsZahl = random.randint(1,100)

# Variable in der die geratente Zahl gespeichert wird
# input(..) liest einen Text ein. Dieser Text wird mit int(..) in eine Zahl konvertiert
print("Willkommen beim Zahlenraten.")
gerateneZahl = int(input("Bitte gib deinen ersten Tipp ab: "))

# Variable in der die Anzahl der Versuche gespeichert werden
versuche = 1

# solange die geratene Zahl nicht übereinstimmt
while gerateneZahl != zufallsZahl:

    # Hinweis, wie groß die Zahl ist    
    if gerateneZahl < zufallsZahl:
        print("Zu klein!")

    else:
        print("Zu groß!")

    # Neuer Versuch
    gerateneZahl = int(input("Rate die Zahl: "))

    # Versuche hochzählen
    versuche += 1

    
# Anzahl der Versuche ausgeben (außerhalb der while-Schleife)
print("Du hast", versuche, " Versuche gebraucht.")

