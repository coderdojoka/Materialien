---
layout: tutorial  
title: Schleifen • Teil 1
author: Mark
date: 2015-12-01
uid: for
topic: basics
type: tutorial
tags: [t_for]
level: l3
next_tut: while
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

## Die for-Schleife

Die `for`-Schleife dient dazu Elemente, einer Liste durchzugehen und einzeln aufzulisten.

```python
liste = [1, 2, 3, 4, 5]
for zahl in liste:
    # Diese Zeile wird 5mal ausgeführt
    # zahl hat jedes mal einen neuen Wert von 1-5
    print(zahl)
```    
Diese werden dann nacheinander
in die Variable `zahl` geschrieben und daraufhin werden jeweils alle eingerückten Zeilen der `for`-Schleife ausgeführt.  

Der obige Code gibt also alle Zahlen von 1 bis 5 (`1, 2, 3, 4, 5`) aus!


### Listen mittels `range()`
Um Listen nicht von Hand mit Zahlen füllen zu müssen, gibt es die `range()`-Funktion: `liste = range(1, 6)`.

`range(1, 5)` (engl. für Bereich) erzeugt also eine Liste mit allen Zahlen vom Startwert (hier `1`)
bis zum Endwert (hier `5`), also: `[1, 2, 3, 4, 5]`

```python
for zahl in range(1, 6):
    print(zahl)
```    

**Wichtig:** Der Endwert ist nicht inklusive!


`range(1, 100, 2)` erzeugt eine Liste mit allen Zahlen zwischen 1 und 100 in 2-er
Schritten. Also `1, 3, ..., 97, 99`. Anstelle von `2` kann jede beliebige andere Zahl verwendet
werden.

**Hinweis:** Die Verwendung von `range(<Startwert>, Endwert>)` entspricht `range(<Startwert>, <Endwert>, 1)`.

Für einfache `for`-Schleifen kann man also einfach schreiben:

```python
for <variable> in range(<Startwert>, <Endwert>, <Schritt>):
    # Anweisungen für jeden Durchlauf
```


Aufgaben
========

-   Schreibe eine `for`-Schleife, die alle Zahlen zwischen 40 und 100 in 3-er
    Schritten ausgibt

-   Experimentiere mit den Werten von `range`. Was passiert, wenn der Startwert
    größer ist als der Endwert? Was passiert, wenn der Schritt (z.B. die
    2 im obigen Beispiel) größer ist als der Endwert. Was passiert, wenn
    der Schritt negativ ist?

-   Schreibe eine `for`-Schleife, die alle Zahlen von 100 bis einschließlich
    1 ausgibt. Also `100, 99, ..., 2, 1`.
