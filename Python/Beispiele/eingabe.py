# Liest einen Text von der Konsole ein (\n erzeugt einen Zeilenumbruch)
name = input("Wie heißt du?\n")	

alter = input("Wie alt bist du?\n") # Alter als Text einlesen
alter = int(alter) # Text in eine Zahl konvertieren

# Gibt den eingelesenen Namen auf der Konsole aus
print("Hallo", name)

print("Du bist also", alter, "Jahre alt!")
