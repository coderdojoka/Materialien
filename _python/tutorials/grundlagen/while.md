---
layout: tutorial  
title: Schleifen • Teil 2
autor: Mark Weinreuter
date: 2015-12-01
version: 0.2
uid: while
folder: basics
type: tutorial
tags: [t_while]
prev_tut: for
---

## Die while-Schleife

Zusätzlich zur `for`-Schleife gibt es die `while`-Schleife. Die -Schleife kann verwendet werden, um Anweisungen wiederholt auszuführen, bis eine Bedingung erfüllt ist.

```python
zaehler = 1
while zaehler <= 100:
  print(zaehler)
  zaehler = zaehler +
```

Im obigen Beispiel wiederholt die `while`-Schleife den eingerückten Code
solange die Bedingung `1 <= 100` erfüllt ist. Dieses Beispiel gibt somit die Zahlen
von `1` bis einschließlich `100` aus.

### Syntax

Eine `while`-Schleife hat den Syntax:

```
while <Bedingung>:
  # Anweisungen, die wiederholt werden
  # solange die Bedingung erfüllt ist
```

**Tipp:** Erklärungen und Beispiele zu Bedingungen findest du in dem Tutorial zu {% include gen_link.html uid="if" %}.

Aufgaben
========

-   Schreibe eine -Schleife, die die Zahlen von 100 bis 0 in 2er
    Schritten ausgibt.

-   Was tut folgendes Programm?

    ```
    wert = 1
    while wert < 10:
      wert = wert + wert
      print(wert)
    ```

    Versuche die Aufgabe mit Stift und Papier zu lösen, indem Du die
    Werte einzeln ausrechnest. Schreibe das Programm nicht ab und führe
    es nicht aus!  
    Erst wenn Du eine Lösung hast, kannst du das Programm
    abtippen, um deine Lösung zu überprüfen.
