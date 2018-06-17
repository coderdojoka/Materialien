---
layout: tutorial  
title: Schleifen • while
autor: Mark, Norbert
date: 2015-12-01
version: 0.2
uid: while
topic: basics
type: tutorial
tags: [t_while]
level: l3
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

> Eine `while`-Schleife führt also solange Code aus bis eine Bedingung nicht mehr erfüllt ist!

### Merkregel: Die `while`-Schleife

```python
while <Bedingung>:
  # Eingerückte Anweisungen, die wiederholt werden
  # solange die Bedingung erfüllt ist

# Hier gehts normal weiter
```

**Tipp:** Erklärungen und Beispiele zu Bedingungen findest du in dem Tutorial zu {% include gen_link.html uid="if" %}.

## Aufgaben

- Schreibe eine -Schleife, die die Zahlen von 100 bis 0 in 2er Schritten ausgibt.

- Was tut folgendes Programm?

  ```python
  wert = 1
  while wert < 10:
      wert = wert + wert
      print(wert)
  ```
  
  Versuche die Aufgabe mit Stift und Papier zu lösen, indem Du die Werte einzeln ausrechnest. Schreibe das Programm nicht ab und führe es nicht aus!  
  Erst wenn Du eine Lösung hast, kannst du das Programm abtippen, um deine Lösung zu überprüfen.
