---
autor: Rafael, Mark
date: 2016-03-15
title: Countdown
layout: exercise
type: exercise
level: l2
uid: aufg_countdown
tags: [t_input, t_while]
---


Daniel Düsentrieb hat eine Rakete gebaut, mit der er zum Mond fliegen
will um dort etwas Urlaub zu machen. Doch er hat das wichtigste
vergessen: **den Countdown!**

![Daniel und seine Rakete](rakete.png){:.img-50w}

Hilf dem zerstreuten Daniel, damit auch er seinen Urlaub auf dem Mond
genießen kann. Schreibe ein Programm, dass:  

- eine Zahl einliest
- von dieser Zahl runter bis zu `1` zählt
- wenn der Countdown bei `0` angekommen ist, `START!!!` ausgibt


## Vorüberlegung

- Wie kannst du eine Zahl einlesen?
- Wie kannst du wiederholt einen Text ausgeben?

## Beispielablauf:

```
Bei welcher Zahl soll der Countdown beginnen? 10
9..
8..
7..
6..
5..
4..
3..
2..
1..
START!!!
```

**Hinweis:** Die `10` wurde vom Benutzer eingegeben.

## Tipps:
- Beachte, das `input(..)` einen Text liefert, konvertiere ihn mittels `int(..)` in eine Zahl
- Willst du den Countdown verzögert ausgeben, dann den Befehl `time.sleep(..)` benutzen.

```python
# Das Paket time einmal importieren
import time

# Hält das Programm für so viele Millisekunden an
time.sleep(1000)
```  
