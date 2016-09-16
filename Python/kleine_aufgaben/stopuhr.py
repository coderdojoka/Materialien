__author__ = 'Rouven'

import time

'''
Deine Aufgabe:

1. Programmiere ein Programm das die Zeit stoppt.
   Zum Starten und Stopen kann man Enter drücken
   und dann gibt es die Zeit aus.

   Tipp: Um die aktuelle Zeit zu erhalten muss man
         aktuelle_zeit = time.time()
         schreiben. Und denke daran time zu importieren.

2. Bau das Programm so um dass es fragt ob man nochmal
   will, wenn ja nochmal von vorne.

3. Verändere das Programm dass es nicht nur die Sekunden
   sondern auch die Minuten anzeigt.
'''

print("Herzlich willkommen zum Zeitstoppen. Drücke return zum Starten und Stoppen")
eingabe = "Ja"
while eingabe == "Ja":
    input("Start: ")
    zeit = time.time()
    input("Stop: ")
    zeit2 = time.time()
    gestoppt_sekunden = zeit2 - zeit
    # eventuell
    gestoppt_minuten = gestoppt_sekunden // 60
    # eventuell
    gestoppt_sekunden = gestoppt_sekunden % 60
    print("Sekunden: " + str(gestoppt_sekunden))
    # eventuell
    print("Minuten: " + str(gestoppt_minuten))
    eingabe = input("Nochmal (Ja/Nein): ")

print("Auf Wiedersehen")
