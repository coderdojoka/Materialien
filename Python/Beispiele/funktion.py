# Funktions-Definition
def sageNamen():
	print("Hallo Mark")

# um die Funktion aufzurufen muss man den Funktionsnamen kennen
sageNamen()

print("Vor dem Funktionsaufruf")
# -> springt zu dieser Funktion und führt deren Code aus
sageNamen() 
print("Nach dem Funktionsaufruf")

# Die obige Funktion ist das Gleiche wie wie:
print("Vor dem Funktionsaufruf")
print("Hallo Mark")
print("Nach dem Funktionsaufruf")

def berechneSumme():
	return 5 + 4

# Die Funktion aufrufen und den Rückgabewert in wert schreiben
wert = berechneSumme()
print(wert)

# Diese Funktion fordert den Nutzer auf eine Zahl einzugeben
def leseZahl()
	eingabeText = input("Gib eine Zahl ein: ") 
	zahl = int(eingabeText) # Eingelesenen Text umwandeln
	return zahl # die Zahl zurückgeben

# Eine Zahl mit unserer Funktion einlesen
zahl1 = leseZahl()
zahl2 = leseZahl()
print("Zahl1: ", zahl1, "Zahl2: ", zahl2)
