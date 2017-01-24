---
author: mark
date: 2016-04-22
title: Referenz • if-Abfragen
layout: tutorial
type: tutorial
folder: referenz
uid: ref2
tags: [t_if]
next_tut: ref3
prev_tut: ref1
---


## Bedingung
Eine Bedingung ist entweder Wahr (True) oder Falsch (False).

```python
bedingung = 10 > 20 # False
print("Die Bedingung ist:", bedingung)
```

### Eine Bedingung negieren
Wollen wir einen Bedingung umdrehen (ins Gegenteil kehren ) verwenden wir den `not`-Operator. Dieser macht `True` zu `False` und umgekehrt.

```python
bedingung = 10 > 20 # False
gegenteil = not bedingung
print("Die Bedingung ist nicht:", gegenteil)
```

## if-Abfragen
Eine if-Abfrage überprüft ob eine Bedingung Wahr oder Falsch ist.
Alles was nach dem `if`-Abfrage mit 4 Leerzeichen oder einem Tab eingerückt gehört zum Körper der `if`-Abfrage und wird nur ausgeführt, wenn die Bedingung war ist!

```python
wert = 10 # Eine Variable mit einem beliebigen Wert (hier 10)

if wert > 20: # wird NUR ausgeführt wenn die Bedingung wahr ist
    print("Der Wert ist größer als 20") # (ACHTUNG: Einrückung)

# Hier gehts weiter (ACHUTUNG: Nicht eingerückt)
```

## if-else-Abfragen
Mit einer if-else Abfrage kann man auch auf eine nicht erfüllte Bedingung mit dem ’else’-Zweig reagieren. Es wird immer *entweder* der `if`-Zweig oder der `else`-Zweig ausgeführt.

```python
if wert > 20: # wird NUR ausgeführt wenn die Bedingung erfüllt ist
    print("Der Wert ist größer als 20")

else: # wird NUR ausgeführt wenn die Bedingung nicht erfüllt ist
    print("Wert ist kleiner oder gleich 20.")

# Hier gehts weiter (nicht eingerückt)
```

## Vergleichsoperationen:
Alle Vergleichsoperationen liefern entweder Wahr oder Falsch. Diese können als Bedingung in einer `if`-Abfrage verwendet werden.

### Standardvergleichsoperationen
```python
a = 10
b = 20

a == b # Gleichheit => False
a != b # Ungleichheit => True
a > b  # = False
a >= b # = False
a < b  # = True
a <= b # = True
```

### Überprüfen, ob ein Textstück in einem Text enthalten ist

Mit dem `in` Operator kann man überprüfen, ob ein Textstück in einem Text enthalten ist:

```python
a = "Hallo Welt"

"allo" in a # = True
"oo" in a   # = False
```

### Überprüfung auf None
`None` ist ein Spezialwert, der soviel ausdrückt wie Nichts. Diesen Wert verwendet man als Platzhaltere. Mit dem `is` Operator kann man testen ob eine Variable gleich `None` ist.

```python
a = "Hallo Welt"

a is None # = False
a is not None # = True
```
