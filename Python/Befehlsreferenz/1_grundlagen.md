---
autor: Mark Weinreuter
version: 0.5
datum: 23.01.16
minted_ausgabe: tmp_latex  
kapitel: 1  
titel: Python - Befehlsübersicht
---

# Grundlagen

## Kommentare

Kommentare gehören nicht zum eigentlichen Programm, sondern sind als Hilfe für den Programmierer gedacht.
```python
# Ein Kommentar, der bis ans Zeilenende geht

""" Ein Kommentar, der
über mehrere Zeilen geht. 
"""
```

Variablen
---------
Variablen sind Wertespeicher. Man kann darin einen Wert ablegen und diesen wieder abfragen.
Sie sind wie eine kleine Box, die einen Namen hat und einen Wert enthält.
Um einer Variablen einen Wert zuzuweisen, muss sie links von einem `=`-Zeichen stehen.
```python
# Eine neue Variable Zahl mit dem Namen ’meineZahl’ und Wert 42
meineZahl = 42

# Eine Text-Variable. Texte stehen in "..".
meinText = "Hallo Welt"
```

Ausgabe
-------

```python
# Gibt einen Text aus
print("Hallo Welt")

# Gibt den Wert einer Variablen aus
name = "Mark"
print("Hallo")
print(name)

# ’print’ gibt auch mehrere Werte mit Leerzeichen getrennt aus
print("Hallo", name)
```

Rechnen mit Zahlen
-----------
Man kann mit Zahlen und Variablen ganz normal rechnen.
```python
# Mit Zahlen kann ganz normal rechnen
wert = 10 + 20 # = 30
wert = 10 - 20 # = -10
wert = 10 / 2 # = 5
wert = 10 * 2 # = 20
wert = 10 % 3 # = 1, da 10 / 3 = 3 Rest 1
wert = 10 ** 3 # = 1000 = 10 * 10 * 10
```

Eingabe durch den Benutzer
--------------------------

### input - Text einlesen
Die Funktion `input(..)` fordert den Benutzer auf einen Text einzugeben.
```python

eingabeText = input("Bitte Text eingeben: ")
print(eingabeText) # gibt den eingelesenen Text aus
```

### input - Eine Zahl einlesen
Eine Zahl, die als Text vorliegt (in Anführungszeichen) konvertieren wir mittels `int(..)` in eine Zahl:
```python
eingabeText = input("Bitte eine Zahl eingeben: ");

eingabeZahl = int(eingabeText) 
# ACHTUNG: wird keine Zahl eingeben, so stürzt das Programm ab!

print(eingabeZahl)
```

