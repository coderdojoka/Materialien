---
layout: tutorial
title: Listen • Lösungen
author: [Mark, Norbert]
date: 2016-08-04
uid: list3
folder: basics
type: tutorial
tags: [t_list]
prev_tut: list2
---

# Schaue dir die Lösungen erst an, wenn du die Aufgaben selbständig gelöst hast!


## Erste Aufgabe: Variante 1

```python
liste1 = ['Kühe', 'Schafe', 'Ziegen', 'Schweine', 'Esel']
liste2 = ['Hühner', 'Enten', 'Tauben']
listeNeu = liste1 + liste2

# Ausgeben der neuen Liste
for eintrag in listeNeu:
    print(eintrag)
```

## Erste Aufgabe: Variante 2

```python
listeNeu = liste1 + ['Hühner', 'Enten', 'Tauben']

# Ausgben der neuen Liste
for eintrag in listeNeu:
    print(eintrag)
```

## Zweite Aufgabe

```python
liste = ['Kühe', 'Schafe', 'Ziegen', 'Schweine', 'Esel', 'Hühner', 'Enten', 'Tauben']

liste.append('Pferd')
liste.remove('Esel')

for eintrag in liste:
    print(eintrag)
```

## Dritte Aufgabe

```python
# erster Teil: Index finden

liste = ['Kühe', 'Schafe', 'Ziegen', 'Schweine', 'Hühner', 'Enten', 'Tauben', 'Pferd']

# Der Index wird in der Variablen x gespeichert
x = liste.index('Pferd')
print(x) # Zeige den Wert des Indexes (= 7)

# zweiter Teil: Pony hinter Pferd einfügen

#Füge das Pony hinter dem Pferd ein: Der Index muss 8 sein
liste.insert(8, 'Pony')

# Liste ausgeben
for eintrag in liste:
    print(eintrag)
```

## Dritte Aufgabe: elegantere Lösung

```python
liste = ['Kühe', 'Schafe', 'Ziegen', 'Schweine', 'Hühner', 'Enten',
'Tauben', 'Pferd']

# Der Index wird in der Variablen x gespeichert
x = liste.index('Pferd')

#Füge das Pony hinter dem Pferd ein: Der Index um 1 höher sein: x+1
liste.insert(x + 1, 'Pony')

for eintrag in liste:
    print(eintrag)
```

## Vierte Aufgabe

```python
zahlen =[1,2,3,4,5,6,7,8,9,10]

for wert in zahlen:
    # Eine Quadratzahl erhält man, indem man die Zahl  mit sich multipliziert
    wert = wert * wert
    print(wert)
```
