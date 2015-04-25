# Öffnet die Datei 'meine_datei.txt'. Die Datei muss existieren :)
datei = open("meine_datei.txt")

# Angegebene Datei einlesen und in die Variable 'text' speichern
text = datei.read()

# Eingelesen Text ausgeben
print(text)

