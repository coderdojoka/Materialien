---
author: mark
date: 2016-04-22
title: Referenz • Grundlagen
layout: tutorial
type: tutorial
folder: referenz
tags: [t_input]
uid: ref1
next_tut: ref2
---

## Kommentare

Kommentare gehören nicht zum eigentlichen Programm, sondern sind als Hilfe für den Programmierer gedacht.

```python
# Ein Kommentar, der bis ans Zeilenende geht

""" Ein Kommentar, der
über mehrere Zeilen geht.
"""
```

## Variablen

Variablen sind Wertespeicher. Man kann darin einen Wert ablegen und diesen wieder abfragen.
Sie sind wie eine kleine Schublade, die einen Namen hat und einen Wert enthält.
Um einer Variablen einen Wert zuzuweisen, muss sie links von einem `=` -Zeichen stehen.

```python
# Eine neue Variable Zahl mit dem Namen ’meineZahl’ und Wert 42
meineZahl = 42

# Den Wert um 5 erhöhen
meineZahl = meineZahl + 5

# Eine Text-Variable. Texte stehen in "..".
meinText = "Hallo Welt"
```

![Eine Variable ist wie eine kleine Schublade](schublade.png){:.img-50w}

Du darfst deinen Variablen beliebige Namen geben, verwende aber am besten sinnvolle Namen. `a1` ist ein schlechter Name, `zaehler` ist ein besserer Name! Mögliche Zeichen sind u.a. Buchstaben und Zahlen, allerdigs keine Umlaute, z.B `ä` oder Leerzeichen.


## Ausgabe

Mit der `print(..)`-Funktion kann man Text und/oder Variablen ausgeben.

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

## Rechnen mit Zahlen

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

## Eingabe durch den Benutzer


### input - Text einlesen
Die Funktion `input(..)` fordert den Benutzer auf einen Text einzugeben. Die `input(..)`-Funktion wartet solange, bis der Benutzer etwas eingetippt und mit der Enter-Taste bestätigt hat. Die Eingabe wird dann als Text zurückgegeben und in der Variablen `eingabeText` gespeichert.

```python
eingabeText = input("Bitte Text eingeben: ")
print(eingabeText) # gibt den eingelesenen Text aus
```

### input - Eine Zahl einlesen
Will man einen Zahl einlesen, so muss man diese konvertieren! Die `input(..)`-Funktion gibt immer einen Text zurück.  
Eine Zahl, die als Text vorliegt, konvertieren wir mittels `int(..)` in eine ganze Zahl oder mittels `float(..)` in eine Kommazahl:

```python
eingabeText = input("Bitte eine Zahl eingeben: ");

eingabeZahl = int(eingabeText)
# ACHTUNG: wird keine Zahl eingeben, so stürzt das Programm ab!

print(eingabeZahl)
```
