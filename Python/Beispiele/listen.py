# eine Liste erstellen
liste = [1, 2, 3, 4, 5]

# Hilfsfunktion für das Ausgeben einer Liste
def liste_ausgeben(liste):
	print("Liste mit", len(liste), "Einträgen")
	# die Elemente ausgeben
	for element in liste:
		print(element)

liste_ausgeben(liste)

# einen Eintrag anfügen
liste.append(6)
liste_ausgeben(liste)

# Liste mit einer anderen Liste kombinieren
liste = liste + [7, 8, 9]
liste_ausgeben(liste)


liste = ["hallo", "test", "welt"]	
# Ein Eintrag kann so gelesen werden:
ersterEintrag = liste[0] # = "hallo". Achtung wir beginnen bei 0
# Negative Indices beginnen am Ende zu zählen
letzterEintrag = liste[-1] # = "welt". 

print(ersterEintrag, letzterEintrag) # => "Hallo Welt"

