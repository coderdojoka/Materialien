---
autor: Mark  
version: 1.0  
date: 2016-07-29
title: Der Geldspeicher  
layout: exercise
level: 4
type: exercise
related_files: [code/python/geldspeicher.py, code/python/geldspeicher_test.py]
tags: [t_for, t_if]
related_exercises: [ht]
uid: geldspeicher
---

Eines Tages stellt Onkel Dagobert fest, dass er sein Notizzettel
verloren hat. Dort hat er das Passwort für seinen Geldspeicher notiert.
Nun hat er Angst davor, dass die bösen Panzerknacker seine Reichtümer
verschleppen und will deshalb sein Geld in Sicherheit bringen.

Onkel Dagobert ist ganz verzweifelt und hofft auf deine Hilfe. Versuche
ein Programm zu schreiben, welches ihm beim Öffnen des Geldspeichers
hilft.

## Aufgabe

Ermittle die geheime Kombination von Onkel Dagoberts Safe! Onkel Dagobert weiß noch, dass die Kombination eine dreistellige Zahl ist.

## Hilfestellung

Daniel Düsentrieb hat ein Hilfsprogramm entwickelt, mit dem du ein dreistelliges Passwort (nur Ziffern) im Sicherheitsfeld eingeben kannst. Hierzu musst du das Modul `geldspeicher` importieren und die Methode
`teste_passwort()` mit deinem geratenen Passwort aufrufen.

## Vorrausetzungen

Um diese Aufgabe erfolgreich lösen zu können solltest du dich mit Schleifen auskennen und die Aufgaben zu
-Schleifen und geschachtelten
-Schleifen gemacht haben.

## Umsetzung

Überlege dir eine Technik, mit der du möglichst geschickt die richtige Kombination ermitteln kannst.
Um die Aufgabe zu lösen benötigst du die Dateien `geldspeicher.py` und `geldspeicher_test.py`.

Lade beide Datei runter und schreibe deine Lösung in `geldspeicher_test.py`:

```python
{% include code/python/geldspeicher_test.py %}
```

**Hinweis:** Du kannst beliebig viele Falscheingaben ausprobieren.  

Die Methode `teste_passwort()` gibt wahr oder falsch zurück. Außerdem erscheint die Ausgabe `’Geldspeicher geöffent’`, wenn du die richtige Kombination gefunden hast.

Onkel Dagobert wird sich in diesem Fall bestimmt erkenntlich zeigen.
