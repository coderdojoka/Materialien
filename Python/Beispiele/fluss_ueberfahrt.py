__author__ = 'Mark Weinreuter'

duLinks = True
ziegeLinks = True
wolfLinks = True
futterLinks = True

print()
print("Du, deine Ziege, ein Wolf und ein Sack Futter stehen an der linken Seite eines Flusses.")
print("Du hast ein kleines Ruderboot, indem du nur eine Sache auf die andere Seite bringen kannst.")
print("Allderdings darf der Wolf nicht mit der Ziege oder die Ziege mit Futter alleine auf einer Seite sein,")
print("da sonst die Ziege oder das Futter gefressen wird!")
print("Wie kannst du alles auf die rechts Seite bringen?")
print()

while True:

    # 1.) Situation darstellen
    text = "-~~~~~~<=/=>~~~~~~-"

    if duLinks:
        text = "-Du" + text
    else:
        text = text + "Du-"

    if ziegeLinks:
        text = "-Z" + text
    else:
        text = text + "Z-"

    if wolfLinks:
        text = "-W" + text
    else:
        text = text + "W-"

    if futterLinks:
        text = "-F" + text
    else:
        text = text + "F-"

    print(text)
    print()

    # 2.) Eingabe einlesen
    eingabe = input("Was willst du mit auf die andere Seite nehmen: nichts, wolf, ziege, futter?\n")

    if eingabe == "ende":
        print("Spiel beendet.")
        break

    # Was wird mitgenommen, ist das überhaupt möglich?
    if eingabe == "nichts":
        pass

    elif eingabe == "wolf" and wolfLinks == duLinks:
        wolfLinks = not wolfLinks

    elif eingabe == "ziege" and ziegeLinks == duLinks:
        ziegeLinks = not ziegeLinks

    elif eingabe == "futter" and futterLinks == duLinks:
        futterLinks = not futterLinks
    else:
        print("Ungültige Eingabe")
        continue

    # Du wechselst immer die Seite
    duLinks = not duLinks

    # 3.) Situation überprüfen
    if ziegeLinks == wolfLinks and ziegeLinks != duLinks:
        print("Der Wolf hat die Ziege gefressen!")
        break

    if ziegeLinks == futterLinks and ziegeLinks != duLinks:
        print("Die Ziege hat das Futter gefressen!")
        break

    if ziegeLinks == futterLinks == wolfLinks == duLinks == False:
        print("Geschafft! Du hast alles auf die rechte Seite gebracht")
        break
