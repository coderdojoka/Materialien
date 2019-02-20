---
author: mark
date: 2016-04-22
title: Dateien I
layout: referenz
topic: python-referenz
uid: ref7
tags: [t_io]
order: 7
next: ref10
prev: ref6
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

Man kann auch eine Liste von Zeilen in eine Textdatei schreiben,
bzw. eine Textdatei auch als eine Liste von Zeilen lesen.

```python

datei = open("meine_datei.txt","r")
# Liest die Zeilen als Liste ein.
# ACHTUNG: Das Zeilenumbruchzeichen am Ende wird nicht automatisch entfernt!
zeilen = datei.readlines()
datei.close()
print(zeilen)

# Alternativ kann man eine Datei auch direkt mit einer for-Schleife durchlaufen
datei = open("text_test.py","r")
for zeile in datei:
    print(zeile)
datei.close()

# Eine Liste in eine Datei schreiben. 
datei = open("zeilen_test.txt", "w")
zeilen = ["hallo welt\n", "schöner tag heute\n"]
# ACHTUNG: Das Zeilenumbruchzeichen muss von Hand hinzugefügt werden
datei.writelines(zeilen)
datei.close()
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

Allerdings gibt es einen Befehl um einen Ordner und alle Dateien darin zu löschen:

```python
# Alle Dateien innerhalb eines Ordner und dann den Ordner löschen
import shutil
shutil.rmtree('mein_ordner')
```

## Einen Ordner kopieren
Kopiert den Ordner `mein_ordner` und alle Dateien darin in den neuen Ordner `kopie`.

```python
import shutil
shutil.copytree('mein_ordner', 'kopie')
```

## Einen Ordner oder Datei umbennen
Bennennt eine Datei/Ordner von `alter_name` zu `neuer_name` um.
```python
import shutil
shutil.move("alter_name", "neuer_name")
```

## Startordnerpfad
Relative Pfadangaben benutzen den Startordnerpfad um eine Datei zu finden.

```python
import os
ordnerpfad = os.getcwd()
print(ordnerpfad)
```

## Dateien in einem Ordner auflisten

```python
import os
for datei_name in os.listdir("mein_ordner"):
    print(datei_name)
```

## Überprüfen ob eine Datei/Ordner exisitiert

```python
import os

# Überprüfen ob einen Datei/Ordner existiert
if os.path.exists("mein_ordner"):
    print("Ordner exisitiert")

if os.path.isfile("mein_ordner"):
    print("Ist eine Datei")

if os.path.isdir("mein_ordner"):
    print("Ist ein Ordner")
```