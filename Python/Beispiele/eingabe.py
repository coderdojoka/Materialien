# Liest einen Text von der Konsole ein
name = input("Wie heißt du?: ")	

alter = input("Wie alt bist du?: ") # Alter als Text einlesen
alter = int(alter) # Text in eine Zahl konvertieren

# Gibt den eingelesenen Namen auf der Konsole aus
print("Hallo", name)

print("Du bist also", alter, "Jahre alt!")
