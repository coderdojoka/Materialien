---
autor: Mark  
datum: 29.07.16  
version: 1.0  
title: Wiederholungen mit Schleifen
layout: page
group: ersteschritte
---

## Wofür sind Schleifen gut?


Du hast die Aufgabe ein Programm zu schreiben, das die Zahlen von 1 bis
100 ausgibt. Wie könnte man diese Aufgabe lösen? Einfach hintereinander
hinschreiben:

```python
print(1)
print(2)
# ... 96 Zeilen mehr
print(99)
print(100)
```

Diese Methode ist umständlich und sehr aufwendig. Glücklicherweise gibt
es dafür eine schlaue Lösung.

## Die `for`-Schleife


Die -Schleife dient dazu Elemente, z.B. die einer Liste einzeln
durchzugehen und aufzulisten.

```python
liste = [1, 10, 20]
for zahl in liste:
    print(zahl)

# Ausgabe:
# 1
# 10
# 20
```

Die Werte der Liste werden nacheinanderin die Variable `zahl` geschrieben. Daraufhin werden alle
eingerückten Zeilen der `for`-Schleife ausgeführt. Dies wird wiederholt bis alle Elemente der Liste durch gegangen wurden.

> Eine `for`-Schleife führt also wiederholt Code für jedes Elemente einer Liste aus.

### Die `range(..)`-Funktion, der beste Freund der `for`-Schleife

```python
for zahl in range(1,100):
    print(zahl)
```

Die Funktion `range(1, 100)` (engl. für Bereich) erzeugt eine Art Liste mit dem Zahlen von `1`
bis `99`, also `(1, 2, ..., 98, 99)`. **Wichtig:** Der  Endwert `100` ist nicht inklusive!

Der obige Code gibt also alle Zahlen von `1` bis `100` (`1, 2, ..., 98, 99`) aus!
Die `range(...)`-Funktion ist sehr nützlich, um eine Liste von Zahlen zu generieren.

### Die `range(..)`-Funktion, genauer betrachtet

Man kann auch die Schrittweite der `range(..)`-Funktion angeben:

```python
for zahl in range(1, 100, 2):
    print(zahl)
```

Dieser Code erzeugt eine Art Liste mit allen Zahlen zwischen `1` und `100` in 2-er Schritten.  
Also: `1, 3, ..., 97, 99`. Anstelle von `2` kann jede beliebige andere Zahl verwendet werden.

### Merkregel: Die `for`-Schleife mit `range(..)`

Für einfache `for`-Schleifen gilt der Syntax:
```python
for <variable> in range(<Startwert>, <Endwert>, <Schritt>): 
    # Anweisungen für jeden Durchlauf, die eingerückt sind

# Hier gehts normal weiter
```  

**Achtung:** Die Angaben in spitzen Klammern im obigen Code-Beispiel, wie `<variable>` sind Platzhalter, die im Code entsprechende angepasst werden müssen

### Aufgaben

- Schreibe eine `for`-Schleife, die alle Zahlen zwischen `40` und `100` in 3-er
    Schritten ausgibt
- Experimentiere mit den Werten von `range`. Was passiert, wenn der Startwert
    größer ist als der Endwert? Was passiert, wenn der Schritt (z.B. die
    `2` im obigen Beispiel) größer ist als der Endwert. Was passiert, wenn
    der Schritt negativ ist?
- Schreibe eine `for`-Schleife, die alle Zahlen von 100 bis einschließlich
    1 ausgibt. Also `100, 99, ..., 2, 1`.

## Die while-Schleife

Zusätzlich zur `for`-Schleife gibt es die `while`-Schleife. Die `while`-Schleife kann
verwendet werden, um Anweisungen wiederholt auszuführen, bis eine
Bedingung erfüllt ist.

```python
zaehler = 1
while zaehler <= 100:
    print(zaehler)
    zaehler = zaehler +1
```

Im obigen Beispiel wiederholt die `while`-Schleife den eingerückten Code
solange die Bedingung `1 <= 100` erfüllt ist. Dieses Beispiel gibt somit die Zahlen
von `1` bis einschließlich `100` aus.

> Eine `while`-Schleife führt also solange Code aus bis eine Bedingung nicht mehr erfüllt ist!

### Merkregel: Die `while`-Schleife

```python
while <Bedingung>:
    # Anweisungen, die wiederholt werden solange die Bedingung erfüllt ist
    # Diese Zeilen sind eingerückt!

# Hier geht es nach der Schleife weiter
```

**Tipp:** Erklärungen und Beispiele zu Bedingungen findest du in dem Abschnitt zu `if`-Abfragen.

### Aufgaben

- Schreibe eine -Schleife, die die Zahlen von 100 bis 0 in 2er Schritten ausgibt.

- Was tut folgendes Programm?
    ```python
    wert = 1
    while wert < 10:
        wert = wert + wert
        print(wert)
    ```

    Versuche die Aufgabe mit Stift und Papier zu lösen, indem Du die
    Werte einzeln ausrechnest. Schreibe das Programm nicht ab und führe
    es aus! Erst wenn Du eine Lösung hast, kannst du das Programm
    abtippen um deine Lösung zu überprüfen.
