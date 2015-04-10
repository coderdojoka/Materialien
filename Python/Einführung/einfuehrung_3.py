import random


# Python Einführung 2:  Boolsche Werte (Wahr/Falsch) und if-Abfragen


# Hinweis: Die verwendeten Befehle beziehen sich auf Python3.
# Sie sind deshalb nicht zwangsweise mit Pyhton2 kompatibel!

# Hinweis: Alle (hoffentlich alle) verwendeten Begriffe, können auch noch einmal
# in der Datei 'uebersicht.py' nachgelesen werden.


"""

Als Programmierer benötigt man an vielen Stellen "Bedingungen", eine Aussage, die entweder wahr oder falsch ist.
Z.B. bei einer if-Abfrage (s. u.) wird eine Bedingung daraufhin überprüft, ob sie wahr und nur dann etwas getan.

Ein Bedingung ist im normalen Sprachgebrauch eine Aussage wie: "Ich bin größer als 1.5m".
Solche Aussagen müssen immer entweder wahr oder falsch!

In Python, wie in anderen Programmiersprachen auch, gibt es aus diesem Grund "Wahr- und Falschausdrücke".
Diese Ausdrücke sind entweder Wahr oder Falsch. Kein Vielleicht wahr oder unter Umständen wahr!
"""

wert1 = 10 > 20  # falsch
wert2 = 10 < 20  # wahr

"""
Hier werden nun die Variablen ist_groesser und ist_kleiner definiert und entweder "Wahr" oder "Falsch" gesetzt.

Da Python eine englische Programmiersprache ist, heißen die Werte "True" für Wahr und "False" für Falsch.
Dies kann nachgeprüft werden, indem wir die Werte mit print() ausdrucken.
"""
print("10 > 20:", wert1)  # gibt 'False' aus
print("10 < 20", wert2)  # gibt 'True' aus

"""
Wichtig: Alle Vergleichsoperation liefern entweder Wahr(True) oder Falsch (False).

Folgende Vergleichsoperationen sind verfügbar:
"""

print("\nGleichheit:")

# Vergleich auf Gleichheit
wert1 = (10 == 10)  # Wahr
wert2 = (10 == 11)  # Falsch
print("10 == 10:", wert1, "\n10 == 11:", wert2)

print("\nUngleichheit:")

# Vergleich auf Un-Gleichheit
wert1 = (10 != 10)  # Falsch
wert2 = (10 != 11)  # Wahr

print("10 != 10:", wert1, "\n10 != 11:", wert2)

"""
Vielleicht ist dir aufgefallen, das die Vergleich (10 == 10) und (10 != 10) genaue Gegenteile zueinander sind!

D.h. es kann immer nur eine der beiden Aussagen falsch sein! Entweder ist 10 gleich 10 oder nicht!
=> die Aussage ist das Gegenteil der anderen Aussage!

Allgemein gilt: ist eine Aussage wahr ist ihr Gegenteil falsch!
"""

print("\nGrößer Vergleich:")

# Der Größer-Vergleich
wert1 = (10 > 10)  # Falsch
wert2 = (11 > 10)  # Wahr
print("10 > 10:", wert1, "\n11 > 10:", wert2)

print("\nGrößer-Gleich Vergleich:")

# Der Größer-Gleich-Vergleich
wert1 = (10 >= 10)  # Wahr
wert2 = (10 >= 11)  # Falsch

print("10 >= 10:", wert1, "\n10 >= 11:", wert2)

print("\nKleiner Vergleich:")

# Der Kleiner-Vergleich
wert1 = (10 < 10)  # Wahr
wert2 = (10 < 11)  # Falsch

print("10 < 10:", wert1, "\n10 < 11:", wert2)

print("\nKleiner-Gleich Vergleich:")

# Der Größer-Gleich-Vergleich
wert1 = (10 <= 10)  # Wahr
wert2 = (10 <= 11)  # Wahr

print("10 <= 10:", wert1, "\n10 <= 11:", wert2)

"""
Okay und wozu sind diese Wahr- und Falschwert nun gut?

Wie bereits erwähnt für if-Abfragen. "if" ist Englisch für "Wenn", als wenn diese Bedingung erfüllt ist,
tue etwas:

if Wahr oder Falsch:
    Tue etwas
    Noch etwas

Wichtig ist hierbei der Doppelpunkt ':' am Ende der "if" Zeile
und die Einrückung (mit 4 Leerzeichen oder Tabulator-Taste) der "Tue etwas" Zeilen.

WICHTIG: Alle Zeilen, die nach der "if" Anweisung eingerückt sind,
werden NUR dann ausgeführt, wenn die angegbene Bedingung wahr ist!

"""

print("\nIf-Else:")
if 10 < 20:
    print("10 ist kleiner als 20")
else:
    print("10 ist nicht keliner als 20")

"""
Im obigen Beispiel sieht man auch die Alternative zum "if"-Zweig. Eine "if-else" Anweisung entspricht auf Deutsch
einer "Wenn dann tue dies, ansonsten etwas anderes:

if Wahr:
    tue dies
else:
    etwas anderes

Auch hier sind die ":" und die Einrückungen zu Beachten!
"""

wert = 20 > 10
print("\nIf mit Variablen:")

if wert:
    print("\nEine Bedingung kann auch eine Variable sein, die einen wahren oder falschen Wert enthält!")

"""
WICHTIG: Eine Wahr-Falsch Bedingung muss nicht direkt hingeschrieben werden, sonder kann auch in einer Variable
gespeichert sein!
"""

wert = True
print("\nIf-Else mit Variablen:")

if wert:
    print("Das ist wahr")

if True:
    print("Das ist offentsichtlich auch wahr")

"""
Man kann auch direkt die Werte "True" und "False" verwenden! Abfragen mit diesen sind allerdings immer offensichtlich
wahr oder falsch :D
"""

"""
Neben einer if-else Anweisung gibt es auch eine "if-elif-else" Anweisung. Also eine Abfrage, ob eine von
mehreren Bedingung wahr ist und falls keine von diesen wahr ist, wir die "else" Anweisung genommen.

Info: Falls du dich über das Wort 'elif' wunderst, dies ist eine Abkürzung für 'else if'


if Wahr oder Falsch:
    tue dies
elif Wahr oder Falsch:
    tue das
else:
    tue was anderes
"""

print("\nIf-Elif-Else:")

wert = 20
if wert < 10:
    print("Kleiner 10")
elif wert < 20:
    print("Kleiner 20")
else:
    print("Größer gleich 20")

"""
Aufgabe:
Du hast einen Variable mit dem Namen Zufall (s.u.) Schriebe eine if-else Abfrage die bestimmt,
ob der Wert der Varibalen größer ist als 50 oder nicht. Dies sollst du dann auch mithilfe des print() Befehls
ausgeben.


Auf Deutsch sähe das ungefähr so aus:

Falls zufall größer gleich 50 dann:
    drucke("Zahl ist größer als 50")
Ansonsten:
    drucke("Zahl ist kleiner als 50")

"""

zufall = random.randint(1, 100)

# Deine if-else-Abfrage





"""
Falls du die erste Aufgabe erfolgreich gemeißert hast, füge bitte einen 'elif'-Zweig in deine 'if-else' abfrage
so das überprüft wird, ob die zufällige Zahl kleiner als 50, kleiner als 75 oder größer als 75 ist.

Hinweis: es ist wichitg in welcher Reihenfolge die Zahlen überprüft werden, das

"""


zufall = random.randint(1, 100)

# Deine if-elif-else-Abfrage
