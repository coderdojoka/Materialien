---
author: mark
date: 2016-04-22
title: Referenz • Nützliches
layout: tutorial
type: tutorial
folder: referenz
uid: ref10
tags: [t_random, t_datetime, t_time]
prev_tut: ref6
---

## Zufallszahlen
Will man eine Zufallszahl erzeugen, kann man dies mit dem Modul `random` tun.

```python
# das random Modul muss (einmal) importiert werden um die Funktion random.randint() verwenden zu können
import random

# generiert eine Zufallszahl zwischen 1 und 100
zufallsZahl = random.randint(1,100)
print(zufallsZahl)
```

## Das Programm kurz anhalten

Um das ganze Programm komplett anzuhalten, kannst du die `time.sleep(..)`-Funktion verwenden.
**ACHTUNG:** Das ganze Programm wird angehalten!

```python
# Das Paket time einmal importieren
import time

# Hält das Programm für so viele Millisekunden an
time.sleep(1000)
```

## Aktuelles Datum
Über das Modul `datetime` kann man das aktuelle Datum abfragen.

```python
# Das Paket datetime einmal importieren
import datetime

# aktuelles Datum abfragen
heute = datetime.datetime.now()

jahr = heute.year
monat = heute.month
tag = heute.day
```  

## Die aktuelle Zeit in Sekunden

Du kannst die aktuelle Zeit in Sekunden mithilfe des Moduls `time` ermitteln:

```python
# Das Paket time einmal importieren
import time

# aktuelle Zeit in Sekunden
sekunden = time.time()
```
