---
date: 2017-01-25
author: Rouven, Mark
uid: ka_schleifen_4
layout: exercise_ka
folder: ka_schleifen
title: Einmaleins-Rechner
tags: [t_input, t_if, t_while]
solution:  code/python/ka/lerner_1x1.py
related_exercises: [ka_input, ka_if]
---


- Schreibe ein Programm das dich 1x1-Aufgaben abfragt.
- Lass den Benutzer den Zahlenraum festlegen, d.h. `grenze1` und `grenze2`
- Stelle dem Benutzer eine zufällige 1x1-Aufgabe aus dem gewünschten Zahlenraum, d.h. verwende zwei Zufallszahlen `z1`und `z2`.
 Wobei `z1`und `z2` kleiner als `grenze1` bzw. `grenze2` sind.
- Fordere den Nutzer auf das Ergebnis einzugeben
- Vergleiche das Ergebnis mit dem berechneten korrekten Ergebnis und gib aus, ob der Benutzer Recht hat
- Frage den Benutzer ob er eine neue Aufgabe lösen will und stelle und wiederhole ab Schritt 3

**Tipp:** `input(..)`, `while` und `if`

