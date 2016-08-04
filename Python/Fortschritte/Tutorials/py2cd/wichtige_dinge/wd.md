---
minted_ausgabe: tmp_latex  
autor: Mark  
version: 1.1  
datum: 30.07.16  
titel: pyenguin - Zeichnen mit Python Teil III
---

Bewegung
========

> **Erinnerung:** Der Koordinatenursprung `(0,0)` liegt in der Mitte eines Objektes.
> Eine Änderung der x-Koordinate, die größer `0` ist (z.B. `5`), ist eine Bewegung nach rechts. Eine negative Änderung bedeutet eine Bewegung nach links (z.B. `-5`).  
>
> Eine Änderung der y-Koordinate, die größer `0` ist, ist eine Bewegung nach **unten!**.  
> Dies ist zunächst verwirrend, allerdings ist dies bei vielen Computerprogrammen so. Eine negative Änderung bedeutet demzufolge eine Bewegung nach oben!
>
> ```python
> box = Rechteck(10, 10, 50, 50, ROT) # Ändert die x- und > y-Koordinate um 5 Pixel
> box.aendere_position(5, 5)
> ```

> Dies ist also eine Bewegung um jeweils 5 Pixel nach rechts unten!


Objekte positionieren
---------------------

Es gibt verschiedene Möglichkeiten Objekte, wie Kreise, Bilder, Texte etc.. zu platzieren:

### Mit links, rechts, oben, unten:

Die Positionen des zum linken, rechten, oberen oder unteren Rand des Objekts kann wie folgt gesetzt werden:

```{.python firstline=10 lastline=24 include="../../../Beispiele/py2cd/objekte_positionieren.py"}
...
```

**Achtung:** Denke immer daran, dass Objekte (z.B.) von einem _unsichtbaren_ Rechteck umgeben sind. Es ist immer der Rand dieses Rechtecks gemeint!

### Die Objekte-Mitte festlegen:

Die x-,y-Koordinaten beziehen sich immer auf die Objektmitte. Durch setzen dieser verschiebt man also die Mitte eines Objektes.

```{.python firstline=10 lastline=24 include="../../../Beispiele/py2cd/objekte_positionieren.py"}
...
```

### Relative Änderung

Die Position um einen Wert ändern. `x_neu = x_alt + wert`.

```python
box = Rechteck(10, 10, 50, 50, ROT)
# Ändert die x- und y-Koordinate um 5 Pixel box.aendere_position(5, 5)
```

### Absolute Position setzen

Die Position auf einen Wert setzen. `x_neu = wert`.

```python
box = Rechteck(10, 10, 50, 50, ROT)
# Setzt die x- und y-Koordinate auf die gegebenen Werte box.setze_position(50, 50)
```


## Objekte zentrieren:

Objekte können horizontal, vertikal oder in beide Richtungen zentriert werden.

```{.python firstline=10 lastline=24 include="../../../Beispiele/py2cd/objekte_positionieren.py"}
...
```


## Geschwindigkeit festlegen und bewegen

Man kann Objekte auch mithilfe von bewegen. Dabei wird das Objekt um die
mit definierte Distanz (hier: 6 Pixel nach rechts und 6 Pixel nach
unten).

box = Rechteck(10, 10, 50, 50, ROT) \# Die x- und y-Geschwindigkeit
setzen box.setze\_geschwindigkeit(6,6) \# Bewegt die Box bei jedem
Aufruf von bewege() um 6 Pixel box.bewege()

Position abrufen
----------------

### x- und y-Koordinaten

Man kann die x- und y-Koordinaten eines Objektes ganz einfach abfragen

\# Box an der Stelle 10x10 box = Rechteck(10, 10, 50, 50, ROT) \# x- und
y-Koordinate abfragen und ausgeben print(box.x, box.y)

### Abstand zum Rand

Genau wie man den Abstand zum linken, rechten, oberen oder unteren Rand
setzen kann, kann man ihn auch abfragen. Das Gleiche gilt auch für die
Objektmitte.

### Größe des umgebenden Rechtecks

Wie zuvor beschrieben, ist jedes Objekt von einem unsichtbaren Rechteck
eingegrenzt. Man kann auch dessen Breite und Höhe abfragen.

Aufgaben
========

1.  Bewege ein Objekt mit den verschiedenen Funktionen über
    die Spielfläche.

2.  Frage die Position von Objekten und derren Abstand zum Rand ab.
    Ändert sich die Postion wie erwartet, wenn du sie bewegst? Z.B.
    sollte sich die x-Koordinate um 20 ändern, wenn aufrufst.
