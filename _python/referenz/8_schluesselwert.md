---
author: Mark
date: 2018-06-22
title: Schluessel-Wert Speicher - Dictionaries
layout: referenz
topic: py_ref
uid: ref8
tags: [t_dict]
order: 8
next: ref9
prev: ref7
---

Ein Schlüssel-Wert Speicher oder Wörterbuch oder Dictionary (`dict`) ist ein Container in dem du Werte unter einem bestimmten Text-Schlüssel ablegest. Du kannst es dir wie ein Schubladenschrank vorstellen. Die Schubladen sind mit Texten beschriftet und du kannst in jede Schublade einen Wert legen oder daraus lesen. Im Prinzip verhalten diese sich ähnlich wie Listen, nur das die Einträge nicht durchnummeriert sind, sonder freiwählbare Texte als Schlüssel fungieren.

## Ein `dict` erstellen

```python
# Ein leeres dict
speicher = {}

# oder über
speicher = dict()

# ein dict mit Einträgen erstellen
speicher = {"schlüssel1" : "wert1", "schlüssel2" : 2}
```

## Einen Eintrag  lesen

Ein Wert wird ähnlich wie bei Liste über seinen Schlüssel in `[]` abgefragt.

```python
speicher = {"s1" : "hallo", "s2" : "welt"}

ersterEintrag = speicher["s1"] # = "hallo".
```

Ist kein solcher Eintrag vorhanden, wird ein Fehler geworfen, deswegen kann man auch die `.get()`-Methode verwenden, die einen Alternativ-Wert als Standartwert akzeptiert.

```python
speicher = {"s1" : "hallo", "s2" : "welt"}

# kein solcher Eintrag => Fehler
eintrag = speicher["s3"] # => KeyError

# kein solcher Eintrag => Alternativ-Wert zurückgeben
eintrag = speicher.get("s3", "test") # => test

# Eintrage vorhanden, diesen zurückgeben
eintrag = speicher.get("s1", "test") # => hallo

```

## Die Länge ermitteln

```python
speicher = {"s1" : "hallo", "s2" : "welt"}

# Die Länge einer Liste (die Anzahl der Elemente) abfragen:
laenge = len(speicher) # = 2
```

## Einen Eintrag hinzufügen

Einträge können über `[schlüssel] = wert` eingefügt werden. Eventuell zuvor eingetragene Werte werden überschrieben.

```python
speicher = {"s1" : "hallo", "s2" : "welt"}

# einen Eintrag anfügen
speicher["s3"] = "test"

# einen Eintrag ändern
speicher["s2"] = "mars"

```

## Ein `dict` mit einer `for`-Schleife durchlaufen

Die einzelnen Schlüssel, Wert, oder Schlüsselwert-Paare können mittels einer `for`-Schleife durchlaufen werden.

```python
speicher = {"s1" : "hallo", "s2" : "welt"}

# Schlüssel durchlaufen
for schluessel in speicher.keys():
    print(schluessel)  # => "s1" dann "s2"

# Werte durchlaufen
for wert in speicher.values():
    print(wert)  # => "hallo" dann "welt"

# Schlüssel und Werte durchlaufen
for schluessel, wert in speicher.items():
    print(schluessel, wert)  # => "s1 hallo" dann "s2 welt"

```

## Überprüfen, ob ein Eintrag vorhanden ist

Mittles `x in speicher` wird überprüft ob der Schlüssel-Wert `x`, z.B. `"s1"` in der Liste vorhanden ist

```python
speicher = {"s1" : "hallo", "s2" : "welt"}

if "s1" in speicher:
    print("Enthalten")
else:
    print("Nicht entalten")
```

## Einen Eintrag löschen

Die `.pop(..)`-Funktion löscht den Eintrag mit dem *gegeben Schlüssel* und gibt dessen Wert zurück.

```python
speicher = {"s1" : "hallo", "s2" : "welt"}
speicher.pop("s1") # = "hallo"

print(speicher) # {"s2" : "welt"}
```

**Achtung:** Hat es keinen solchen Wert, wird ein Fehler erzeugt!
