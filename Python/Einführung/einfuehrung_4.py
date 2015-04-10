# Python Einführung 2:  Boolsche Werte (Wahr/Falsch) und if-Abfragen


# Hinweis: Die verwendeten Befehle beziehen sich auf Python3.
# Sie sind deshalb nicht zwangsweise mit Pyhton2 kompatibel!

# Hinweis: Alle (hoffentlich alle) verwendeten Begriffe, können auch noch einmal
# in der Datei 'uebersicht.py' nachgelesen werden.


"""
Programme können kompliziert werden. Und je länger der Quellcode wird, desto unübersichtlicher und verwirrender wird es
diesen zu lesen und zu verstehen. Hinzu kommt, dass an einigen Stellen im Code werden Zeilen mehrmals verwendet werden
oder ganze Zeilenblöcke kommen mehrfach vor.

Um den Quellcode besser zu strukturieren, einfacher lesbar zu halten und Verdoppelungne zu vermeiden, kann
man Funktionen einsetzen um Codeblöcke zu trennen und wiederholte Funktionalität auszulagern.


Ein einfaches Beispiel:
"""


def hallo():    # Funktionsdefinition
    print("Hallo Welt") # ist eingerückt


# ist nicht mehr eingerückt
hallo()


"""
Funktionsdefinition (Synthax:


Ein Funktion ist immer so aufgebaut:

def name_der_funktion():
    tue was
    tue noch was
    ...

"def" bedeutet, jetzt kommt eine Funktionsdefinition. danach der Name der Funktion (Buchstaben, Zahlen, '_' )
danach ein jetzt noch leeres Klammernpaar '()' und abschließend ein Doppelpunkt.

Alle nachfolgenden Zeilen, die eingerückt sind gehören zur Funktion und werden nur dann ausgeführt wenn die
Funktion aufgerufen wird!

Zur Erinnerung:
Python gruppiert Dinge durch Einrückungen, entweder 4 Leerzeichen oder ein 'Tab' (Tabulatortaste drücken)
Die Tabulatortaste mit den zwei Pfeile in entgegengesetzte Richtung ist am linken Rand mittig/oben auf der Tastatur.


Um einen Funktion aufzurufen schreibt man:


name_der_funktion()


Dieser Aufruf führt den Code innerhalb der Funktion aus, also alles was nach der Funktion eingerückt ist.
"""



"""
Die hallo() Funktion ist nicht soo sinnvoll. Aber mit Funktionen kann man viel coolere Sachen machen.
"""

def gruesse(name):
    print("Hallo", name)

gruesse("Mark")


"""
Funktions-Parameter:
Eine Funktion können auch Dinge übergeben werden! Dafür muss die Funktionsdefinition angepasst werden:

def name_der_funktion(parameter):
    tue etwas

Die Funktion enthält nun innerhalb der Klammern einen Wert namens "parameter". Dies ist eine Variable, die in der
Funktion verwendet werden kann und einen Wert enthält, der beim Funktionsaufruf gesetzt wird.
Der Funktionsaufruf sieht dem entsprechend anderst aus:

name_der_funktion("ich bin der wert")

"""

gruesse(10)

"""
Funktions-Parameter:
Du sieht an dem Funktionsaufruf: gruesse(10), dass nicht unbedingt Text and die Funktion übergeben werden muss,
wie in gruesse("Mark"), sondern auch andere Werte wie z.B. Zahlen.

WICHTIG: Python überprüft NICHT, ob du einen gültigen Wert einer Funktion übergibst!!! Wenn du eine Funktion
schreibst, die einen Text(engl. String)  als Parameter erwartet, aber bpsw. eine Zahl bekommt,
kann dies zu Fehlern führen!

Zum Beispiel:
"""

# Funktion, die einen übergeben Text an Leerzeichen trennt
def trenne(was):

    # Trennt den Text an Leerzeichen: erzeugt eine Liste mit Worten
    was = was.split()

    # gibt die getrennten Wörter als Liste aus
    print(was)


# Das funktioniert, da ein String erwartet wird
trenne("Hallo Welt")


# ALLERDINGS funktioniert das hier nicht! Zum Ausprobieren entferne das Kommentarzeichen '#' vom Zeilenanfang!
# sage_haelfte(10)



"""
Funktions-Parameter:

Eine Funktion kann mehr als einen Parameter haben:

def name_der_funktion(parameter1, parameter2):
    tue was

Diese müssen lediglich in den Klammer mit Komma getrennt ',' aufgelistet sein.


WICHTIG: Ein Funktionsaufruf muss immer genau soviele Werte übergeben, wie Parameter definiert sind!
Man kann Parametern auch Anfangswerte zuweisen, dazu aber später mehr

"""