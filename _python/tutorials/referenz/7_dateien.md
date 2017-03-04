---
author: mark
date: 2016-04-22
title: Dateien I
layout: referenz
topic: py_ref
uid: ref7
tags: [t_io]
next_tut: ref10
prev_tut: ref6
---

Ein Computer speichert Informationen in Dateien. Dateien sind in Ordnern gruppiert.
Eine Datei/Ordner wird über ihren Pfad eindeutig angegeben.



## Eine Datei öffnen
Mithilfe von `open(pfad, modus)` kann man eine Datei öffnen.
Der `modus` kann dabei folgende Werte sein:

| r | w | a | rb | wb |
| --- | --- | --- | --- | --- |
| Lesen | Schreiben | Anfügen | Binärdatei lesen | Binärdatei schreiben

> Python unterscheidet zwischen dem Lesen/Schreiben von Text und Binärdateien.
Standartmäßig geht es von Textdateien aus! Mit dem `b`-Wert wird der Binärmodus aktiv.

```python
# Eine Datei zum Schreiben öffnen
# Falls die Datei schon existiert wird sie überschrieben
datei = open("meine_datei.txt", "w")
datei.write("Hallo ")
datei.close()

# Eine Datei zum Schreiben/Anhängen öffnen
# Falls die Datei schon existiert wird der neue Inhalt hinten angefügt
datei = open("meine_datei.txt", "a")
datei.write("Welt")
datei.close()

# Datei zum Lesen öffnen
datei = open("meine_datei.txt", "r")
inhalt = datei.read()
datei.close()
print(inhalt)
```

## Eine Datei löschen
```python
import os
os.remove("mein_datei.txt")
```

## Einen Ordner erstellen
```python
import os
os.mkdir("mein_neuer_ordner")
```


## Einen Ordner löschen
Man kann nur leere Ordner löschen! Ist der Ordner nicht leer,
dann muss man zuvor alle Dateien darin löschen!

```python
import os
# Einen leeren Ordner löschen
os.rmdir("mein_neuer_ordner")
```

Allerdings gibt es dafür einen Befehl:

```python
# Alle Dateien innerhalb eines Ordner und dann den Ordner löschen
import shutil
shutil.rmtree('mein_ordner')
```

## Einen Ordner kopieren
Kopiert den Ordner `mein_ordner` und alle Dateien darin in den neuen Ordner `kopie`.

```python
shutil.copytree('mein_ordner', 'kopie')
```

## Startordnerpfad
Relative Pfadangaben benutzen den Startordnerpfad um eine Datei zu finden.

```python
ordnerpfad = os.getcwd()
print(ordnerpfad)
```

## Dateien in einem Ordner auflisten

```python
for datei_name in os.listdir("mein_ordner"):
    print(datei_name)
```

## Überprüfen ob eine Datei/Ordner exisitiert

```python
# Überprüfen ob einen Datei/Ordner existiert
if os.path.exists("mein_ordner"):
    print("Ordner exisitiert")

if os.path.isfile("mein_ordner"):
    print("Ist eine Datei")

if os.path.isdir("mein_ordner"):
    print("Ist ein Ordner")
```