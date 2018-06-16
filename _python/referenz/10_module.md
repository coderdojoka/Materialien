---
author: mark
date: 2016-04-22
title: Nützliches
layout: referenz
topic: py_ref
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

## Zip-Archive erstellen und entpacken
Will man ein Zip-Archiv erstellen, muss man jede Datei einzeln hinzufügen!
Auch Dateien in einem Ordner müssen einzeln hinzugefügt werden!!

```python
# Ein neues Zip-Archiv erstellen
zip_archiv = zipfile.ZipFile('mein_zip.zip', 'w', zipfile.ZIP_DEFLATED)
# Alle zu zippenden Dateien hinzufügen
zip_archiv.write("datei1.txt")
# Einen Ordner hinzufügen
zip_archiv.write("ordner1")
# Die Dateien im Ordner müssen einzeln! hinzugefügt werden
zip_archiv.write("ordner1/datei2.txt")
# ...
zip_archiv.close()
```

Will man nur einen ganzen Ordner zippen, geht das auch einfacher:

```python
import shutil
# Einen ganzen Ordner zippen
shutil.make_archive("mein_zip", 'zip', "pfad/zum/ordner")
```

Ein Zip-Archiv kann man ganz einfach entpacken:

```python
# Archiv zum Lesen öffnen
zip_archiv = zipfile.ZipFile("mein_zip.zip", "r")

# Alles in einen neuen Ordner entpacken
zip_archiv.extractall("test")

# Alles im aktuellen Verzeichnis entpacken
zip_archiv.extractall()
```