---
layout: tutorial
type: tutorial
title: Text
author: Mark
date: 2015-12-01
uid: python-tutorial-text
permalink: /python/tutorials/text/
topic: python-grundlagen
level: 2
tags: [t_text]
---


## Warum Text?

An vielen Stellen beim Programmieren hat man mit Text zu tun. Man muss
Texte lesen, auf bestimmte Buchstaben untersuchen, etc...

```python
# eine Variable mit dem Wert 'Hallo Welt'
meinText = "Hallo Welt"
print(meinText)
```

Textstücke erkennt man daran, dass sie in einfachen `'...'` oder doppelten `"..."`
Anführungszeichen stehen.


## Operatoren

Man kann Textstücke kombinieren:

```python
name = "Mark"
meinText = "Hallo " + name  # Textstücke zusammenkleben
print(meinText)
```

Dies könnte man auch mit `print(..)` direkt
ausgeben, da mehrere Parameter übgergeben werden können:

```python
# Kombinierte Ausgabe
print("Hallo", name)
```

Analog zum Plus-Operator gibt es auch den Mal-Operator:
```python
meinText = "Hallo" * 2
print(meinText)  # gibt 'HalloHallo' aus
```

## Länge eines Textes

Manchmal ist es praktisch zu wissen aus wie vielen Buchstaben ein Text
besteht. Wir nennen dies auch die Länge eines Textes. Um die Anzahl der
Buchstaben, eines Textes zu ermitteln, benutzt man den Befehl `len(...)` (’length’
ist Englisch für Länge) wie folgt:

```python
laenge = len(meinText)  # Länge des Textes ermitteln
print(laenge)
```


## Texte als Buchstabenketten

Im Rechner intern, werden Texte als ein Kette von einzelnen Buchstaben
gespeichert. Dies können wir uns zu Nutzen machen.

```python
meinText = 'Hallo'
buchstabe = meinText[2]  # dritter Buchstabe! Die erste Stelle ist 0!
print(buchstabe)  # Gibt 'l' aus
```

Mit den eckigen Klammern am Ende der Text-Variablen `meinText[2]` deuten wir an, dass
wir den Buchstaben wissen wollen, der an der in Klammern geschrieben
Stelle steht.

> **Achtung:** Beim Programmieren fangen wir oft bei `0` mit dem Zählen an.
> D.h., dass wir, um den dritten Buchstaben zu erfahren, nicht `3`, sondern `2` in
> die eckigen Klammern schreiben müssen.


## Texte sind unveränderlich

Eine interessante Eigenschaft von Texten ist, dass diese nicht verändert
werden können. Wenn wir versuchen, z.B. den vierten Buchstaben zu
überschreiben, erhalten wir einen Fehler:

```python
# Dies erzeugt einen Fehler! Texte sind nicht veränderlich
meinText[3] = 'b'
```


## Aufgaben

-   Erstelle eine Text-Variable und las dir den Wert ausgeben.
-   Spiele mit den Operatoren herum. Wie kannst du 100-mal `HaHa` ausgeben?
-   Lass dir den zweiten und vorletzen (Hinweis: berechne die Länge
    des Textes) Buchstaben von `Hallo Welt` ausgeben.
-   Probiere wie oben beschrieben den Text zu ändern. Bekommst du auch
    einen Fehler?
