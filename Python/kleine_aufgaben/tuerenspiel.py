from random import randint

anzahl_tueren = 2
weitermachen = "j"
zaehler = 1

while weitermachen == "j":
    tuer_richtig = "Ja"
    while tuer_richtig == "Ja":
        tuer = randint(1, anzahl_tueren)
        eingabe = input("Raten Sie welche von " + str(anzahl_tueren) + " Türen die richtige ist.")
        eingabe = int(eingabe)
        if tuer == eingabe:
            print("Richtig!!!")
        else:
            print("Leider falsch!!!")
            tuer_richtig = "Nein"
            zaehler = 0
        if zaehler == 3:
            tuer_richtig = "Nein"
            print("Super Sie haben es geschaft!!!")
        zaehler = zaehler + 1
    weitermachen = input("Weitermachen?(j/n): ")
