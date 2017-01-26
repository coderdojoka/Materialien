---
autor: Mark
datum: 2016-04-22
title: Sekunden-Rechner
layout: exercise
type: exercise
folder: einfach
tags: [t_input]
---

## Aufgabe
Schreibe ein Programm, dass dazu auffordert eine Zeit in Stunden und Minuten einzugeben.
Das Programm rechnet dann die Stunden- und Minutenangabe in Sekunden um.

## Vorüberlegung
- Stell dir vor, dass man dir die Anzahl an Stunden und Minuten nennt.
 Wie kannst du sie in Sekunden umrechnen?
- Übersezte das Vorgehen in ein Programm, dass mittels `input(..)` zwei Zahlen einliest

## Beispielablauf:
```
Wie viele Studen: 1
Wie viele Minuten: 42

Das sind 6120 Sekunden.
```
**Hinweis:** Die Zahlen `1` und `42` sind hier die Benutzereingabe.

## Tipps:
- Beachte, das `input(..)` einen Text liefert, konvertiere ihn mittels `int(..)` in eine Zahl
- Eine Stunde hat 60 Minuten, eine Minute 60 Sekunden, d.h. eine Stunde hat 60 * 60 = 3600 Sekunden
