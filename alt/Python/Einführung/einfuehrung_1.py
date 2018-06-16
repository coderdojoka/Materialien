
# Python Einführung 1: Kommentare und print()


# Hinweis: Die verwendeten Befehle beziehen sich auf Python3.
# Sie sind deshalb nicht zwangsweise mit Pyhton2 kompatibel!

# Hinweis: Alle (hoffentlich alle) verwendeten Begriffe, können auch noch einmal
# in der Datei 'uebersicht.py' nachgelesen werden.




# 1.) Kommentare
# Das ist ein Kommentar. Mithilfe von Kommentaren kann und soll Code kommentiert und erklärt werden!

"""
Das ist ein Kommentar über mehrere Zeilen.
Zeile 2!
"""

# 2.) der print()-Befehl:
# Um Dinge auf der Konsole (das Fenster im dem das Programm ausgeführt/gestartet
#werden) auszugeben gibt es den 'print' (dt: ausdrucken) Befehl


print("Hallo Welt!")



# GENERELLER AUFBAU:
# Schreibe 'print', dann '(' , danach das, was du ausgeben willst in " ", dann ')'. 
# Also:
# print("Was du ausgeben willst")
# Wenn du dich wunderst, warum das so komisch aussieht und warum genau so,
# dann musst du dich leider noch ein bisschen gedulden! Das wird später erklärt :)


print("Hallo", "Welt")
# Du kannst auch mehrere Dinge hintereinander ausgeben,
# d.h. mehere Zeichenketten innerhalb der Klammern mit , getrennt auflisten
# diese werden immer mit einem Leerzeichen dazwischen getrennt ausgeben.

# Der 'print'-Befehl will eine "Zeichenkette", auf Englisch 'String'
# also Buchstaben, Wörter, Sätze, alles was du in " " schreibst.


print("bsdfkdjf")
# Es muss keinen Sinn ergeben, nur die "" sind wichtig.
# print(Hallo Welt)  #Das ist ein Fehler! Entferne das erste # und probiere es aus!

# Wichtig ist außerdem, dass du sorgfältig schreibst und keine Schreibfehler machst!
# Wenn du dich vertippst und prinnt("Hallo Welt"), also 2 'n' schreibst, dann ist das ein Fehler!
# Genauer gesagt ein Syntax-Fehler, da die "Syntax", also die Rechtschreibung, oder Reihenfolge falsch ist.



# AUFGABE:
# Du bist dran! Gib ein paar Dinge mit dem print()-Befehl aus! Z.b. deinen Namen, dein Alter


# Hier sollte dein print()-Befehl stehen.




# ZUSAMMENFASSUNG:
# Ein # am Zeilenanfang, bedeutet, dass ein Kommentar folgt.

"""
Alles zwischen 3 ", ist ein Kommentar, der übere mehrere Zeilen gehen kann
"""

print("Hallo Welt")
#Gibt die Zeichenkette, die zwischen den Klammern steht auf der Konsole aus.


# Die korrekte Schreibweise von Befehlen ist wichtig! Sehr wichtig! Ein einzelner Schreibfehler
# und das gesamte Programm ist nicht ausführbar!
