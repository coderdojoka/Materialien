---
author: mark
date: 2016-04-22
title: Referenz • Schleifen
layout: tutorial
type: tutorial
folder: referenz
uid: ref3
tags: [t_while, t_for]
next_tut: ref4
prev_tut: ref2
---

# Schleifen

## while-Schleife
Eine `while`-Schleife führt den eingerückten Code aus, solange die Bedingung erfüllt ist.

```python

zahl = 1
while zahl < 10: # solange die Bedingung wahr ist...
    # ...wird dieser eingerückte Code wird wiederholt
    print("Zahl:", zahl)
    zahl = zahl + 1 # Zähler erhöhen

# Hier gehts normal weiter (Achtung: nicht eingerückt)
```

**Achtung:** Ist die Bedingung immer wahr läuft das Programm in einer Endlosschleife.

## for-Schleife

Eine `for`-Schleife wird verwendet um eine Liste, Text (ein Text ist nur eine Liste von Buchstaben), o.ä. zu durchzulaufen.
Der eingerückte Code wird für jedes Listenelement einmal ausgeführt.

### Eine Liste durchlaufen:

```python
liste = [1, 2, 3, 4]

for zahl in liste:    
    print("Zahl:", zahl)

# Hier gehts normal weiter (ACHTUNG: nicht eingerückt)
```

### Einen  Text buchstabenweiße durchlaufen:

```python
text = "abcdefghijklmnopqrstuvwxyz"

for buchstabe in text:    
    print("Buchstabe:", buchstabe)

```

## Geschachtelte Schleifen

Bei geschachtelten Schleifen befindet sich eine Schleife innerhalb einer anderen Schleife!
D.h. die innere Schleife und somit der Code innerhalb der inneren Schleife wird mehrmals ausgeführt!  

In diesem Beispiel wird die äußere `for`-Schleife 9 mal ausgeführt.
Die innere `for`-Schleife 4 mal. Der Code in der inneren Schleife wird also:
`9 * 4 = 36` mal ausführt!

```python

for zahlAussen in range(1, 10): # nimmt Werte 1-9 an
    # Achtung Einrückung!

    for zahlInnen in range(1, 5): # nimmt Werte 1-4 an
        # Achtung nochmal einrücken!
        print("Außen:", zahlAussen, "Innen:", zahlInnen)
```

**Hinweis:** `range(untergrenze, obergrenze)` erzeugt eine Liste der Zahlen von der Untergrenze bis zur Obergrenze.
Die Obergrenze ist allerdigs nicht enthalten.
