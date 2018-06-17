---
author: mark
date: 2016-04-22
title: Funktionen I
layout: referenz
topic: py_ref
uid: ref6
tags: [t_function]
order: 6
next: ref10
prev: ref6
---

## Was ist eine Funktion?
Eine Funktion ist ein Block Code, der vom Haupt-Programm getrennt definiert wird. Die Funktion wird erst dann ausgeführt, wenn man sie über ihren Namen aufruft. Dafür kann man einen Funktion so oft mal will verwenden. Variablen, die innerhalb einer Funktion definiert sind, sind **nur** innerhalb der Funktion verwendbar!

## Eine einfache Funktion
Funktionen bestehen aus einem Block von eingerückten Code-Zeilen.
Diese werden erst ausgeführt, wenn die Funktion aufgerufen wird.

```python
# Neue Funktion mit dem Namen 'sageHallo' definieren
def sageHallo():
    print("Hallo Welt") # Einrückung!

# Funktion aufrufen (keine Einrückung)
sageHallo()
```

## Funktion mit Übergabeparametern
Funktion können Parameter (Variablen, die nur innerhalb der Funktion existieren) haben.
Die Werte für diese Variablen *müssen* beim Aufrufen mitübergeben werden.

```python
# Funktion definieren
def sageHallo(name, alter):
    print("Hallo", name)
    print("Du bist", alter, "Jahre alt")

# Funktion aufrufen
sageHallo("Mark", 22)
```
Die Funktion `sageHallo`hat zwei Parameter: `name` und `alter`.

## Funktion mit Rückgabewerten
Funktion können einen Wert zurückgeben, müssen aber nicht. Wenn nichts zurückgeben wird,
wird automatisch `None` zurückgeben.

```python
# Funktion definieren
def addiere(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

# Funktion aufrufen
ergebnis = addiere(12, 22)
print(ergebnis)
```
