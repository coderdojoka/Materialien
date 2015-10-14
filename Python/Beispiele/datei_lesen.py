# Öffnet die Datei 'meine_datei.txt'. Die Datei muss existieren :). 
# Die Datei wird zum lesen geöffnet: "r" und als Zeichensatz 'utf-8' auswählen (kann ggf. weggelassen werden)
datei = open("meine_datei.txt", "r", encoding="utf-8")

# Angegebene Datei einlesen und in die Variable 'text' speichern
text = datei.read()

# Eingelesen Text ausgeben
print(text)


# Datei schließen
datei.close()
