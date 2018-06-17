---
layout: tutorial
title: Listen • Teil 2
author: Mark, Norbert
date: 2016-08-04
uid: list2
topic: basics
type: tutorial
tags: [t_list]
level: 3
order: 2
prev: list1
next: list3
---

# Zwei Listen zusammenfügen

Wir haben zwei Listen `liste1`und `liste2` und wollen sie zu einer Liste `listeNeu` zusammenfügen. Dies können wir mit dem Pluszeichen `+` erreichen:

```python
liste1 = [0,1,2,3,4,]
liste2= [5,6,7,8,]

# die beiden Listen werden in ListeNeu zusammengefügt
 listeNeu = liste1 + liste2

# Ausgeben der neuen Liste
for eintrag in listeNeu:
    print(eintrag)

# Als Ausgabe erhalten wir die Zahlen von 0 bis 8.
```

Wir könne auch Werte hinzufügen, ohne sie vorher in eine Listen-Variable
zu schreiben.

```python
listeNeu = liste1 + liste2 + [100,500]

# Hier erhalten wir die Ausgabe: 0 1 2 3 4 5 6 7 8 100 500
```

# Aus einer Liste ein Element herauslöschen

Wir haben eine Liste mit Farben: ` farben = ['rot','gelb','grün','rot','blau']`. Wie man sieht, ist der Eintrag `'rot'` doppelt enthalten. Den vierten Eintrag müssen wir also entfernen.

# Die .pop()- Funktion

Elemente aus der Liste entfernen kann man mit der Funktion .pop()

```python
farben = ['rot','gelb','grün','rot','blau']
farben.pop(3)
# ACHTUNG: Das Programm beginnt bei 0 (Null) zu zählen.
# Der vierte Eintrag hat also den Index [3]

for eintrag in farben:
    print(eintrag)
# Ausgabe: rot gelb grün blau
```

# Die .remove()-Funktion

Eine weitere Möglichkeit, einen Wert zu entfernen bietet die Methode `remove(xy)` (engl.: entfernen). Diese Funktion schaut in der Liste nach und entfernt den ersten Eintrag mit dem Wert `xy`:

```python
farben = ['rot','gelb','grün','rot','blau']
farben.remove('rot')

for eintrag in farben:
    print(eintrag)
# Die Ausgabe sieht dann so aus: gelb grün rot blau
```

# Ein bestimmtes Element löschen

Wir haben wieder unsere Farbenliste und wissen, dass die Farbe zweimal
vorkommt. Soll jetzt der zweite Eintrag von entfernt werden. Dafür
benutzen wir die Methode

# Die .index()-Funktion

Zuerst wird der erste Eintrag von `'rot'` ermittelt:

```python
farben = ['rot','gelb','grün','rot','blau']
ersteStelle = farben.index('rot')

# wir wollen wissen welchen Index das erste 'rot' hat
print(ersteStelle)

# Anzeige auf dem Bildschirm: 0
```

Dies ist korrekt. `'rot'` ist das erste Element und das erste Element einer
Liste hat den Index Null.  

Jetzt sagen wir der Methode `index(..)`, sie soll den zweiten Eintrag von `rot`
finden und an der nächsten Stelle mit der Suche fortfahren. Dies können
wir indem wir die Nummer des Start-Indexes mitgeben, ab dem die Liste
durchsucht werden soll.

```python
# Fahre mit der Suche beim nächsten Index fort
zweiteStelle = farben.index('rot', 1)

print(zweiteStelle)
# Anzeige auf dem Bildschirm: 3
```

Den ersten Index speichern wir in der Variable `ersteStelle`. Für die weitergehende Suche müssen wir `ersteStelle` um `1` erweitern , um beim nächsten Index fortzufahren. Haben wir das nächste Vorkommen von `'rot'` gefunden, kann der Wert mit `pop(..)` gelöscht werden.

```python
farben = ['rot','gelb','grün','rot','blau']

# Ermitteln des ersten Indexes => 0
ersteStelle = farben.index('rot')

# Suche fortführen beim nächsten Index > 0 +1
zweiteStelle = farben.index('rot', ersteStelle + 1)

# Der zu löschende Index (= 3) ist in zweiteStelle gespeichert
farben.pop(zweiteStelle)

for eintrag in farben:
    print(eintrag)

# Bildschirmanzeige: rot gelb grün blau
```

# Ein Element einfügen

Ein Element an einer beliebigen Stelle der Liste hinzu fügen mit der
Methode `insert(..)` (engl.: einfügen). In unserer Farbliste wollen wir an die zweite Stelle die Farbe `'lila'` hinzufügen. Wie müssen unserer Methode sagen an welcher Stelle und was wir hinzufügen wollen:

```python
farben = ['rot','gelb','grün','rot','blau']

# an zweiter Stelle einfügen, d.h. nach 'rot'
farben.insert(1, 'lila')

# Bildschirmanzeige: rot lila gelb grün rot blau
```

# Eine Teilliste erzeugen

Eine Liste von Elemente kann man mittels des "Ausschneide"-Operators aus einer Liste ausschneiden.
Wie bei der Indizierung verwendet der Ausschneide-Operator eckige Klammern `[]`, aber jetzt werden zwei Werte erwartet `[start:ende]`:

> Du kannst dir das Ganze so merken. Schreibst du nur eine Zahl, z.B. die
`2` in die Klammer, also `liste[2]`erhälst du das Element an dieser(der dritten) Stelle.
> Willst du allerdings nicht nur einen Wert, sondern einen Teil der Liste,
z.B. das zweite bis zum vierten Element, so schreibt man `liste[1:4]`.


Hier ein paar Beispiele zur Verwendung des Slicing-Operators:

```python
farben = ['rot','schwarz','gelb','grün','rot','blau']

# Teilliste von zweiten bis zum vierten Element
neue_farben = farben[1:4]

# Bilschirmausgabe: schwarz gelb grün

# Lässt man in der eckigen Klammer den Anfangswert frei,
# beginnt das Programm von Anfang an zu zählen und zeigt uns:

neue_farben = farben[:2]
# Ausgabe: rot schwarz

# Lässt man in der eckigen Klammer den Endwert frei,
# so zählt das Programm ab diesem Index und geht bis zum Ende.

neue_farben = farben[2:]
# Es zeigt an: gelb grün rot blau

# Lässt man Anfangs- und Endwert weg, erhält man die ganze Liste(als Kopie):
neue_farben = farben[:]

# Ausgabe: rot schwarz gelb grün rot blau
```


# Aufgabe: Was kann man alles mit Listen machen?

## Aufgabe 1: Landwirt Fritz Bauer

1. Landwirt Fritz Bauer hat sich zwei Listen mit Tieren, die sich auf
   seinem Hof befinden, erstellt.

   ```python
   liste1 = ['Kühe', 'Schafe', 'Ziegen', 'Esel']
   liste2 = ['Hühner', 'Enten', 'Tauben']
   ```

   Es gibt zwei Möglichkeiten, aus den beiden Listen eine einzige Liste
   zu machen. Zeig sie Herrn Bauer!

2. Wir haben jetzt eine neue Liste:

   ```python
   liste = ['Kühe', 'Schafe', 'Ziegen', 'Esel', 'Hühner', 'Enten', 'Tauben']
   ```

   - Herr Bauer tauscht mit seinem Nachbarn seinen Esel gegen ein Pferd. Lösche den Esel aus der Liste und füge das Pferd hinzu.
   - Herr Bauers Tochter Eliane wünscht sich zum Geburtstag ein Pony. Da Herr Bauer seiner Tochter nichts abschlagen kann, hat    sein Hof jetzt ein Tier mehr und er muss wieder seine Liste erweitern. Füge das Pony vor dem Pferd ein.  

     **Tipp:** lass Dir den Index für das Pferd anzeigen, dann kann man das Pony leicht einfügen.

## Aufgabe 2: Quadratzahlen

Wir haben eine Liste der Zahlen 1 bis 10 und wollen nun die Quadrate dieser Zahlen ermitteln.

```python
zahlen = [1,2,3,4,5,6,7,8,9,10]
```

Zur Erinnerung: eine Quadratzahl bekommt man, wenn man die Zahl mit sich selber multipliziert.  
Bsp. `2² = 2 * 2 = 4`:



