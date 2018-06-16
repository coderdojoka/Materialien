---
date: 2018-06-15
author: Mark
parent: ersteschritte
layout: exercise
title: Erste Schritte - Grundlagen
tags: [t_input]
related_exercises: [ka_input, ka_for]
---


## Hallo Python


### Lernziele
- Wie man Variablen erstellt, verwendet und ändert
- Texte, Zahlen und was die Unterschiede sind
- Operatoren: `+`, `*`, um mit Zahlen und Texte zu rechnen
- Neue Funktionen: 
    - `print(..)` und `input(..)` zur Ausgabe, bzw. Eingabe
    - `int(..)` und `str(..)` zur Konvertierung in Zahlen, bzw. Texten.



### Ein Python-Programm schreiben. Was ist das und was muss ich beachten?
- Korrekte Schreibweise ist **SEHR** wichtig
- Eine Anweisung pro Zeile
- Kommentare: Was in einer Zeile hinter einem `#`-Zeichen steht wird von Python ignoriert und nicht ausgeführt. Das ist nützlich für Notizen und um Code 'auszukommentieren', d.h. der Code wird nicht mehr ausgeführt, aber du musst ihn nicht löschen und kannst in jeder Zeit wieder einkommentieren.
- Anweisungen werden von oben nach unten ausgeführt
- Ausführung einer Zeile kann dauern (z.B. `input(...)` wartet auf Benutzereingabe s.u.) alle weiteren Anweisungen werden erst nach Abarbeitung der aktuellen Anweisung ausgeführt

### Programm #1 hallo.py:  `Hallo Welt` ausgeben
- `print("Hallo Welt")` Zeichen für Zeichen abschreiben und ausführen, was passiert?

### Wie funktioniert die `print(...)`-Funktion?
- Allg. Aufbau von Funktionsaufrufen: NAME(Parameter1)
- Texte in Anführungszeichen: `"`
- Was passiert ohne Anführungszeichen?

### Variablen ertsellen und ausgeben
- Was sind Variablen
- Allg. Aufbau beim Erstellen von Variablen NAME = WERT
- print(meineVariable)

### Anführungszeichen - Wann und wann nicht?
- Python erkennt Texte an Anführungzeichen. Alles was nicht in Anführungszeichen steht muss eine Variable, Befehl, o. ä. sein.
- **Wichtig**: Variablen ohne Anführungszeichen, Texte mit Anführungszeichen!


### `Hallo Python` einlesen
- `input("Schreib mir etwas: ")` schreiben, ausführen und *Hallo Python* eingeben `ENTER`-Taste drücken, was passiert?
- Was wird ausgegeben? was nicht?


### Programm #2: echo.py
- Funktionen wie `input(..)` haben Rückgabewerte
- Rückgabe von `input(..)` in einer Variable speichern und mit `print(..)` ausgeben


### Texte kombinieren
- Plus-Operator/**Kombination** : `+` fügt zwei Text-Stücke zusammen: `text = "Hallo " + "Welt"`
- Mal-Operator/**Wiederholung**: `*` wiederholt den Text: `text = "Ha" * 10`
- Ausprobieren


### Programm #3: wellen.py
- Male mit Hilfe von `print(..)` und den Text-Operatoren ein Meer aus Wellen
- Verwende verschiedene Wellen-Zeichen, z.B: `^` und `~`
- **Beispiel**: So könnte die Ausgabe deines Programms aussehen:
```
~~~~~~~~~~
^^^^^^^^^^
^~^~^~^~^~
~~~~~~~~~~
```
- Wie sieht dein Meer aus? Versuche mit möglichst wenig Zeichen ein möglichst großes Meer zu erzeugen.

---


### Programm #4: werbistdu.py
- Frage den Nutzer mithilfe von `input(..)` nach seinem Namen, Alter, etc.
- Nachdem du die Eingaben eingelsen und in Variablen gespeichert hast, gib sie in einer schönen Form aus, z.B:
```
Hallo Mark!
Du bist 24 Jahre alt.
```
- Frage weitere Dinge ab und gib sie aus.


### Datentypen: Texte `str` und Zahlen `int`
- Python unterscheidet was für einen Datentyp Werte/Variablen haben.
- Neben Texten (in Python `str`, von engl. *string*) z.B. `"abc"` gibt es auch Ganzzahlen, z.B. `234` (in Python `int` von engl. **integer**) oder Kommazahlen ,wie `-123.567` (in Python `float` von engl. *floating point*). Diese benötigen keine Anführungzeichen nur Zahlen mit optinaler Kommastelle `.` und Minuszeichen `-` erlaubt
- Je nach Datentyp, haben Operationen wie `+`und  `*` andere Bedeutung. 

- Versuche die Ausgabe der folgenden Zeilen vorherzusagen (schreibe sie auf ein Blatt Papier), ohne sie auszuführen:
    - `text = "12" + "8"`
    - `zahl = 12 + 8`
    - `text2 = "12" * 2`
    - `zahl2 = 12 * 2`  

   Führe die Zeilen jetzt aus (mit zusätzlichen `print(..)`-Befehlen für die Ausgabe) Was ist die Ausgabe? Waren deine Erwartungen korrekt?
- Die Datentypen müssen zu den verwendeten Operatoren passen, nicht alle Kombinationen sind erlaubt! Beispiel:
- `zahl3 = 12 * "2"`
- Welche Kombinationen von Zahlen und Texten sind möglich, welche davon sind erlaubt (liefern keinen Fehler)

### Anführungszeichen - Wann und wann nicht? Teil II
Was sind folgende Ausdrücke: Variablen oder Werte und welchen Typ haben die Werte?

- `12345`
- `text`
- `"text"`
- `"12345"`
- `text2`
- `-345`
- `"ab23"`
- `234.34`




### Zahlen in Texte umwandeln und umgekehrt
- Neue Funktionen: `int(..)` und `str(..)` 
- `int("1234")` erzeugt aus einem Text, der eine Zahl darstellt einen Zahl
- `str(12345)` erzeugt aus einer Zahl einen Text, der diese Zahl darstellt
- Was passiert, wenn `int(..)` einen Text übergeben wird, der keine gültige Zahl ist?



### Programm #5: zahlensalat.py
- lies 2 zahlen ein
- gib als Zahlen addiert und als string addiert aus
- gib als zahlen multipliziert und als text mit zahl multipliziert aus


---


### Programm #6: wiealt.py
- lies das Geburtsjahr ein
- bereichne mit dem aktuellen Jahr wie alt der Nutzer ist
- Ist das Ergebnis immer richtig? Warum nicht?


### Rechnen mit Python
Python unterstüzt alle Grundrechenarten und noch viel mehr! Grundrechenarten:
- `zahl1 = 22 + 20`
- `zahl2 = 22 - 20`
- `zahl3 = 22 * 20`
- `zahl4 = 22 / 20` 


Kann man diese Operationen auch für Texte verwenden?


Besonderheiten der Division:
- `zahl = 18 / 4`
- `zahl1 = 18 // 4` 
- `zahl2 = 18 % 20`

Was tun diese drei verschiedenen Operationen?

### Programm #7: grundrechenarten.py
- Lies 2 Zahlen ein
- Berechne das Ergebnis der sieben oben aufgeführten Berechnungen und gib jeweils die Rechnung mit Ergebnis aus.


### Programm #8: rechenmeister.py
- Lies 2 Zahlen ein
- Fordere jemand (dich selbst) auf die beiden Zahlen im Kopf zu multiplizeren 
- Lass dir das Ergebnis ausgeben, wenn du `ENTER` drückst (einen beliebigen Text einliest)

### Programm #9 Alle meine Fehler
- Schreibe ein Programm, das abstürzt (einen Fehler erzeugt)
- Wie viele verschiedene Fehlermeldungen kannst du erzeugen?

### Programm #10 Ein eigenes Programm
- Denke dir ein eigenes kleines Programm aus, dass die neuen Befehle verwendet, die du gelernt hast
- 


### Abschluss

- Du solltest 10 Programme erstellt haben, toll!
- Kommentiere alle Programme die du erstellt hast! Schreibe zu jeder (wichtigen) Zeile einen Kommentar-Hinweis, was die entsprechende Zeile bewirkt
- Halte dein Cheat-Sheet aktuell! Hast du alle Befehle und Operationen eingetragen?!



## Du solltest folgende Dinge/Funktionen jetzt kennen (und nie wieder vergessen :)

- Die `print`-Funktion, um etwas auf der Konsole auszugeben
- Die `input`-Funktion, um Texte einzulesen
- Was Texte sind:
    - Woran erkennt man Texte?
- Zahlen:
    - Woran erkennt man Zahlen?
    - Wie unterscheiden sie sich von Texten?
- Variablen:
    - Woran erkennt man Variablen?
    - Wie ändert man den Wert einer Variablen?
    - Wie liest man den Wert einer Variablen
    - Wie unterscheiden sie sich von Texten/Zahlen?
    - Variablen haben verschiedene Typen, je nachdem welchen Wert sie speichern
- Die Operatoren `+`, `*` für Texte und für Zahlen!
    - Was bewirken die Operatoren für Texte und was für Zahlen?
- Die `int(..)`-Funktion, um Texte in Zahlen umzuwandeln
- Die `str(..)`-Funktion, um Zahlen in Texte umzuwandeln
