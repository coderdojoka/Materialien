print("Gib ein wieviel Zeit du gebraucht hast und für welche Strecke.")
zeit = int(input("Zeit(in min.): "))
strecke = int(input("Strecke(in km): "))
print("Du hatest eine Durchschnittsgeschwindichkeit von " + str((60 / zeit) * strecke) + " km/h")
