text = input("Gib eine Zahl größer 9 und kleiner 100 ein: ")
zahl = int(text)

if zahl < 10:
    print("Die Zahl ist zu klein")
elif zahl > 99:
    print("Die Zahl ist zu groß")
else:
    z = zahl // 10
    e = zahl % 10
    ergebnis = z + e
    print("Ergebnis: ", ergebnis)



