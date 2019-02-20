
# eine Variable mit dem Wert 'Hallo Welt'
meinText = "Hallo Welt"
print(meinText)

name = "Mark"
meinText = "Hallo " + name  # Textstücke zusammenkleben
print(meinText)

# Kombinierte Ausgabe
print("Hallo", name)

meinText = "Hallo" * 2
print(meinText)  # gibt 'HalloHallo' aus

laenge = len(meinText)  # Länge des Textes ermitteln
print(laenge)

meinText = 'Hallo'
buchstabe = meinText[2]  # dritter Buchstabe! Die erste Stelle ist 0!
print(buchstabe)  # Gibt 'l' aus

# Dies erzeugt einen Fehler! Texte sind nicht veränderlich
meinText[3] = 'b'
