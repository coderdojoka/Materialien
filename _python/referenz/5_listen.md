---
author: Mark
date: 2016-04-22
title: Listen
layout: referenz
topic: py_ref
uid: ref5
tags: [t_list]
order: 5
next_tut: ref6
prev_tut: ref4
---

Eine Liste ist ein Container für verschiedene Werte oder Variablen. Du kannst dir einen Liste wie einen Schubladenschrank vorstellen. Die Schubladen sind durchnummeriert und du kannst in jede Schublade einen Wert legen oder daraus lesen.

## Eine Liste erstellen

```python
# Eine leere Liste erstellen
liste = []

# eine Liste mit Einträgen erstellen
liste = [1, 2, 3, 4, 5]
```

## Einen Eintrag aus der Liste lesen

Ein Wert aus der Liste wird über seinen Index (die Position in der Liste) abgefragt.

```python
liste = ["hallo", "test", "welt"]

ersterEintrag = liste[0] # = "hallo".
```

**Achtung:** Wir beginnen bei 0 zu zählen! Das erste Element hat den Index 0.

## Einen Eintrag vom Ende der Liste lesen

```python
# Negative Indizes beginnen am Ende zu zählen
letzterEintrag = liste[-1] # = "welt".

print(ersterEintrag, letzterEintrag) # => "Hallo Welt"
```
**Achtung:** wir beginnen hinten bei -1 zu zählen! Das letzte Element hat den Index -1.

## Länge einer Liste ermitteln

```python
liste = [1, 2, 3]

# Die Länge einer Liste (die Anzahl der Elemente) abfragen:
laenge = len(liste) # = 3
print(laenge)
```

## Einen Eintrag hinzufügen
Die `.append(..)`-Funktion fügt einen Eintrag ans Ende der Liste an.

```python
liste = [1, 2]

# einen Eintrag anfügen
liste.append(3)
```

## Eine Liste mit einer `for`-Schleife durchlaufen
Die einzelnen Elemente der Liste werden mittels einer `for`-Schleife durchlaufen.

```python
for element in liste:
    print(element)
```

## **Beispiel:** Hilfsfunktion für das Ausgeben einer Liste
Gibt die Anzahl der Elemente und deren Werte aus.

```python
def liste_ausgeben(liste):
    print("Liste mit", len(liste), "Einträgen")

    # die Elemente ausgeben
    for element in liste:
        print(element)

# Diese Funktion ruft man so auf
liste = [1, 2, "Haus", "Katze"]
liste_ausgeben(liste)
```

## Überprüfen, ob ein Eintrag vorhanden ist

Mittles `x in liste` wird überprüft ob der Wert von `x`, z.B. 1 in der Liste vorhanden ist

```python
liste = [1, 2, "hallo", "welt"]

if 1 in liste:
    print("Enthalten")
else:
    print("Nicht entalten")
```

## Einen Eintrag entfernen
Die `.remove(..)`-Funktion sucht den **ersten** Eintrag mit diesem Wert und entfernt ihn.

```python
liste = [1, 2, 6]
liste.remove(6) # = [1, 2]

liste_ausgeben(liste)
```

## Einen Eintrag löschen
Die `.pop(..)`-Funktion löscht den Eintrag an der *gegeben Stelle* und gibt diesen Wert zurück.

```python
liste = [100, 200, 300]
liste.pop(1) # = 2

liste_ausgeben(liste) # [100, 300]
```


**Achtung:** Hat es keinen solchen Wert, wird ein Fehler erzeugt!

## Eine Liste erweitern
**Erweitert** (verändert!) die erste liste um die zweite Liste.

```python
liste = [1, 2, 3, 4, 5, 6]
liste.extend([7, 8, 9]) # = [1, 2.., 9]

liste_ausgeben(liste)
```

## Zwei Listen kombinieren
Erstellt eine **neue** Liste aus den beiden angegeben Listen!

```python
liste = [1, 2, 3, 4, 5, 6]
neue_liste = liste + [7, 8, 9] # = [1, 2.., 9]

liste_ausgeben(neue_liste)
```