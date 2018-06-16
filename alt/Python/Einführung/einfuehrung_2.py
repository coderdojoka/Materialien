
# Python Einführung 2:  Variablen und Strings/Zeichenketten


# Hinweis: Die verwendeten Befehle beziehen sich auf Python3.
# Sie sind deshalb nicht zwangsweise mit Pyhton2 kompatibel!

# Hinweis: Alle (hoffentlich alle) verwendeten Begriffe, können auch noch einmal
# in der Datei 'uebersicht.py' nachgelesen werden.




# 3.) Variablen

# Variablen sind ein mächtiges Konzept in der Programmierung. Variablen sind
# "Wertespeicher". Man kann ihnen Werte zuweisen und sie behalten diesen Wert
# bis man ihnen einen neuen zuweist.
# Natürlich kann man diesen Wert auch abfragen!
# Falls dir Variablen (noch) aus der Schule bekannt vorkommen, gut! Variablen
# verhalten sich ähnlich wie in der Schule.
# Info: In Python sind Variablen nicht "statisch typisiert", d.h. eine Variable kann eine
# Zahl beinhalten oder eine Zeichenkette!


# Meine erste Variable
meineVariable = "Hallo Welt"

# Hier wird eine neue Variable mit dem Namen: 'meineVariable' angelegt (deklariert)
# Gleichzeitig wird ihr der Wert 'Hallo Welt' zugewiesen (initialisiert)
# meineVariable beinhaltet (hat) den Wert 'Hallo Welt', wobei 'Hallo Welt' ein String
# bzw. Zeichenkette ist.
# Variablen können einen (fast) beliebigen Namen haben. Sie müssen mit einem
# Buchstaben beginnen und dürfen Zahlen und große und kleine Buchstaben enthalten.

# GENERELLER AUFBAU
# Auf der linken Seite des '=' steht der Variablenname,
# auf der rechten Seite steht der Anfangswert der Variablen.
# Das wars! Die Variable kann jetzt im folgenden Code verwendet werden, indem man sie
# über ihren Namen anspricht. Wichtig! Variablen sind erst  bekannt nachdem sie
# deklariert werden, nicht davor!


# Wenn du dich nun fragst was das alles soll, hier ein kleines Beispiel:
print(meineVariable)

# Hoffentlich errinierst du dich noch an den print()-Befehl, der Zeichenketten ausgeben
# kann. Allerdings hatten wir zuvor immer direkt den Wert in "Anführungszeichen" in
# die Klammern geschrieben. Hier verwenden wir die Variable, die eine Zeichenkette
# enthält um den Wert an den print()-Befehl weiter zu geben.

# Okay, aber wozu das ganze, jetzt brauche ich ja 2 Zeilen um 'Hallo Welt' auszugeben?
# Korrekt. Aber man kann viele nützliche Dinge mit Variablen machen, wie du in den
# nächsten Beispielen hoffentlich sehen wirst.


meineVariable = "Mark"
print("Hallo", meineVariable)

# Hier wurde der Wert der Variablen geändert und ausgeben! Wie zuvor beschrieben,
# kann der print()-Befehl mehere Werte die mit Komma ',' getrennt werden ausgeben!


# AUFGABE
# - Lass deinen eigenen Namen ausgeben, indem du den Wert der Variablen änderst
# und mittels print() ausgibst.
# - Probiere einfach mal aus, was du mit mehrere Variablen und dem print()-Befehl
# ausgeben kannst.





# 4.) Strings, bzw Zeichenketten

# Zeichenketten sind sehr nützlich und es ist daher wichtig den korrekten Umgang mit
# ihnen zu lernen!

name = "Mark"
begruessung = "Hallo "
ausgabe = begruessung + name
print(ausgabe)
# Mit + können zwei Zeichenketten verbunden  werden.
# Dies funktioniert mit Variablen und mit direkten Werten:

ausgabe = "Hallo " + name
print(ausgabe)

ausgabe = begruessung + "Mark"
print(ausgabe)
#Alle 3 Varianten sind gleichwertig! Und erzeugen die selbe Ausgabe.


#WICHTIG:
# Mit + werden Zeichenketten zusammengefügt. Das Ergebnis dieser Zusammenführung
# steht auf der "linken Seite" und kann als Zuweisung für einen andere Variable dienen.
# Die beiden Variablen/Zeichenketten, die zusammengefasst werden, ändern sich  NICHT.
# Zeichenketten sind alle Werte, die in einfachen oder doppelten Anführungszeichen
# geschrieben werden: "Zeichenkette Version 1" und 'Zeichenkette Version 2'.



ausgabe = "Hallo "
ausgabe += "Mark"
# Fügt die angebene Zeichenkette (Variable) an die Variable links des '+=' an.
print(ausgabe)

#Wichtig:
# Mit += wird eine Zeichenkette an eine existierende String-Variable angefügt.
# Hierbei wird die Variable geändert.


ausgabe = "ha" * 10 #wiederhole 10 mal "ha"
print(ausgabe)

# Mit * können Zeichenketten eine angegeben Anzahl oft wiederholt aneinander gefügt werden.
# Genau so wie 2 *3 = 2 + 2 + 2 ist, so ist "ha" * 3 = "ha" + "ha" + "ha".

ausgabe = "ha" * 3 + "ho" * 3       # lässt sich auch gut kombinieren
print(ausgabe)

# Analog zu += gibt es auch *= was die Zeichenkette auf der linken Seite um die
# angegebene Anzahl oft an sich sich wieder anfügt.

ausgabe = "hi"
ausgabe *= 10
print(ausgabe)


# AUFGABE
# - Gibt mithilfe von print() und den Operationen +, *, +=, *= einige lustige Sachen aus.
# Frage: steht in ausgabe1 das selbe wie in ausgabe2?
# ausgabe1 = "hallo"
# ausgabe1 + " welt"
# ausgabe2 = "hallo"
# #ausgabe2 += "welt"
# print(ausgabe1)
# print(ausgabe2)
