__author__ = 'Rouven'

'''
Deine Aufgabe:

1. Schreibe ein Programm das dich
   1x1-Aufgaben abfragt.

2. Mache am Ende eine Abfrage ob man
   nochmal möchte, wenn ja von vorne
   wenn nein beenden.

3. Lass den Benutzer denn Zahlenraum festlegen.
'''

from random import randint

print("Herzlich willkommen zum 1x1-Lerner. Bitte gib den Zahlenraum an.")
von = input("von: ")
bis = input("bis: ")
von = int(von)
bis = int(bis)
weiter = "Ja"

while weiter == "Ja":
    zahl = randint(von, bis)
    zahl2 = randint(von, bis)
    print(str(zahl) + " x " + str(zahl2))

    eingabe = int(input("= "))
    if eingabe == zahl * zahl2:
        print("Richtig")
    else:
        print("Leider falsch!!! Das richtige Ergebnis ist " + str(zahl * zahl2))

    weiter = input("Weiter (Ja/Nein): ")

print("Auf Wiedersehen")
