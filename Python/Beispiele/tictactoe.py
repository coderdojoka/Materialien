__author__ = 'Mark Weinreuter'

s1 = input("Spieler 1, wie heißt du? ")
s2 = input("Spieler 1, wie heißt du? ")

z1 = input("Spieler 1, gib bitte dein Zeichen (ein Buchstabe) ein? ")
z2 = input("Spieler 1, gib bitte dein Zeichen (ein Buchstabe) ein? ")

print("Es spielen ", s1, "und", s2)

felder = [0, 0, 0,
          0, 0, 0,
          0, 0, 0]


def spielfeld_anzeigen():
    for zahl in range(0, 9):
        # Das Zeichen kann 0, z1 oder z2 sein
        zeichen = felder[zahl]

        # Entweder die Feldnummer, oder das Zeichen ausgeben
        if zeichen == 0:
            print(zahl, end=" ")
        else:
            print(zeichen, end=" ")

        # print erzeugt normalerweise einen Zeilenumbruch
        # mit , separator=" " haben wir dies verhindert.
        # Wir wollen nur nach jedem dritten Zeichen einen Umbruch
        if zahl % 3 == 2:
            print("")


def hat_gewonnen():
    for i in range(0, 3):
        # erste Reihe überprüfen
        if felder[i * 3 + 0] == aktives_zeichen and felder[i * 3 + 1] == aktives_zeichen and felder[i * 3 + 2] == aktives_zeichen:
            return True

        # Erste Spalte überprüfen
        if felder[i + 0] == aktives_zeichen and felder[i + 3] == aktives_zeichen and felder[i + 6] == aktives_zeichen:
            return True

    # Erste Diagonale überprüfen
    if felder[0] == aktives_zeichen and felder[4] == aktives_zeichen and felder[8] == aktives_zeichen:
        return True

    if felder[2] == aktives_zeichen and felder[4] == aktives_zeichen and felder[6] == aktives_zeichen:
        return True

    # Weitere Diagonalen ...

    # Falls nicht gewonnen => False
    return False


spielfeld_anzeigen()

# Spieler 1 beginnt
aktiver_spieler = s1
aktives_zeichen = z1

zuege = 0
while zuege < 9:
    print("Du bist dran", aktiver_spieler)
    eingabe = input("Welches Feld möchtest du besetzen?")
    # In eingabe steht ein Text => in eine Zahl umwandeln
    feld_nummer = int(eingabe)

    # Ist die Eingabe korrekt?
    if feld_nummer < 0 or feld_nummer > 8:
        continue

    # Ist das Feld schon besetzt?
    if felder[feld_nummer] != 0:
        continue

    felder[feld_nummer] = aktives_zeichen
    spielfeld_anzeigen()

    # Hat der aktive Spieler gewonnen
    if hat_gewonnen():
        print(aktiver_spieler, "hat gewonnen!")
        break  # Die Schleife verlassen

    # Spieler wechseln
    if aktiver_spieler == s1:
        aktiver_spieler = s2
        aktives_zeichen = z2
    else:
        aktiver_spieler = s1
        aktives_zeichen = z1

    # Ein Zug erfolgreich abgeschlossen
    zuege = zuege + 1

if zuege == 9:
    print("Unentschieden!")
