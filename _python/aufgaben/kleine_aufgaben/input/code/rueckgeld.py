print("Gib einen Betrag und das was du bezahlt hast ein!")
betrag = int(input("Betrag(in €): "))
bezahlt = int(input("Bezahlt(in ct): "))
zurueck = (bezahlt / 100) - betrag
print("Das Rückgeld ist " + str(zurueck) + " €")
