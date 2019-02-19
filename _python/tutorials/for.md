---
layout: tutorial  
title: Schleifen • for-Schleife
author: Mark
date: 2015-12-01
uid: for
topic: python-grundlagen
type: tutorial
tags: [t_for]
level: 3
next: while
---

## Einstieg

Du hast die Aufgabe ein Programm zu schreiben, das die Zahlen von 1 bis
100 ausgibt. Wie könnte man diese Aufgabe lösen? Einfach hintereinander
hinschreiben:

```python
print(1)
print(2)
# ... 96 Zeilen mehr
print(99)
print(100)
```

Diese Methode ist umständlich und sehr aufwendig. Glücklicherweise gibt
es dafür eine schlaue Lösung.

## Die `for`-Schleife

Die `for`-Schleife dient dazu Elemente, einer Liste durchzugehen und einzeln aufzulisten.

```python
liste = [10, 20, 30]
for zahl in liste:
    # Diese eingerückten Zeilen werden 3 ausgeführt
    print(zahl)

# Ausgabe:
# 1
# 10
# 20
```

Diese werden dann nacheinander in die Variable `zahl` geschrieben und daraufhin werden jeweils alle eingerückten Zeilen der `for`-Schleife ausgeführt.  


Die Werte der Liste werden nacheinanderin die Variable `zahl` geschrieben. Daraufhin werden alle eingerückten Zeilen der `for`-Schleife ausgeführt. Dies wird wiederholt bis alle Elemente der Liste durch gegangen wurden.

### Listen mittels `range()`

Um Listen nicht von Hand mit Zahlen füllen zu müssen, gibt es die `range()`-Funktion:  
`liste = range(1, 6)`.

`range(1, 6)` (engl. für Bereich) erzeugt also eine Liste mit allen Zahlen vom Startwert (hier `1`)
bis zum Endwert (hier `6`), also: `[1, 2, 3, 4, 5]`. **Wichtig:** Der Endwert `6` ist nicht inklusive!

```python
for zahl in range(1, 6):
    print(zahl)
```

### Die `range()`-Funktion kann viel mehr

Der Aufruf `range(1, 100, 2)` erzeugt eine Liste mit allen Zahlen zwischen 1 und 100 in 2-er
Schritten. Also `1, 3, ..., 97, 99`. Anstelle von `2` kann jede beliebige andere Zahl verwendet
werden. Man kann also eine Liste von Zahlen mit einer gegeben Schrittweite generieren.

**Hinweis:** Die Verwendung von `range(<Startwert>, Endwert>)` entspricht `range(<Startwert>, <Endwert>, 1)`.

### Merkregel: `for`-Schleife

Für einfache `for`-Schleifen kann man also einfach schreiben:

```python
for <variable> in range(<Startwert>, <Endwert>, <Schritt>):
    # Anweisungen für jeden Durchlauf
```

## Aufgaben

- Schreibe eine `for`-Schleife, die alle Zahlen zwischen 40 und 100 in 3-er Schritten ausgibt

- Experimentiere mit den Werten von `range`. Was passiert, wenn der Startwert größer ist als der Endwert? Was passiert, wenn der Schritt (z.B. die `2` im obigen Beispiel) größer ist als der Endwert. Was passiert, wenn der Schritt negativ ist?

- Schreibe eine `for`-Schleife, die alle Zahlen von 100 bis einschließlich `1` ausgibt. Also `100, 99, ..., 2, 1`.
