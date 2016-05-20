---
autor: Mark  
datum: 05.05.2016  
version: 1.0  
keine_sektions_nummern: ja  
titel: Schnelles Quadrieren  
---

# Aufwärmen: Einer- und Zehnerstellen

Eine Zahl zweistellige Zahl $X = ZE$ kann man in ihre Zehnerer (Z)- und Einerstelle (E) aufteilen. Es gilt:

$$ X = 10 * Z + E $$

Z.B:

$$42 = 4 * 10 + 2$$

Oder als Tabelle dargestellt:

| Zahl\quad\quad | \quad Zehnerstelle\quad | \quad Einerstelle\quad |
|----------------|:------------:|:-----------:|
| ZE             |      Z       |      E      |
| 23             |      2       |      3      |
| 72             |      7       |      2      |

## Aufgabe 1:
Schreibe ein Programm, dass eine Zufallszahl zwischen 10 und 99 ermittelt. Zerlege diese Zahl in Zehner- und Einerstelle und gib sowohl die Zufallszahl, als auch die Einer und Zehnerstelle aus.

### Beispielausgabe:

```
Zufallszahl: 58
Zehnerstelle: 5
Einerstelle: 8
```

### Tipps:
- mit `str(..)` kannst du einen Zahl in einen Text umwandeln, mit `int(..)` kannst du einen Text in eine Zahl umwandeln
- Aus einem Text kannst du die einzelnen Buchstaben abfragen mit:

```python
text = "245"
text[0] # = 2
text[1] # = 4
text[2] # = 5
```
**Hinweis:** Der ersten Buchstaben steht an der Stelle 0.


# Multiplikation einer einstelligen mit einer zweistelligen Zahl

Wie schnell kannst du im Kopf einen beliebige zweistellige Zahl mit einer einstelligen Multiplizieren?

$$ 4 * 67 = ? $$

Teilen wir nun $67$ in $67 = 60 + 7$ auf, erhalten wir:

$$ 4 * 67 = 4 * (60 + 7) $$

Daraus ergeben sich die zwei Rechnungen:  

$$ 4 * 60 = ? $$

$$ 4 * 7 = 28 $$

Die erste Multiplikation mit 60 sieht auf den ersten Blick vielleicht noch komplizierter aus, ist sie aber nicht. Den die Multiplikation mit einer runden zweistelligen Zahl enstpricht einfach der Multiplikation mit der Zehnerstelle und dann dem Anfügen einer 0 am Ende, also der Multiplikation mit 10:

$$ 4 * 60 = 4 * 6 * 10 = 24 * 10 = 240 $$

Addieren wir nun die beiden Teilergebnisse $240$ und $28$ erhalten wir das Endergebnis:

$$ 240 + 28 = 268 $$


# Aufgabe 2:
Schreibe ein Programm, dass den Nutzer auffordert eine einstellige Zahl und eine zweistellige Zahl einzugeben. Multipliziere die beiden eingelsenen Zahlen nach dem obigen Muster. Gib alle Zwischenschritte dabei aus. Du darfst in deinem Programm **NUR** einstellige Zahlen  miteinander multiplizieren! Ausnahme ist die Multiplikation mit 10.

### Beispielausgabe

```
Gib eine zweistellige Zahl ein: 53
Gib eine einstellige Zahl ein: 3

Gesucht: 53 * 3
Zerlege: 53 = 50 + 3
Zerlege: 50 = 5 * 10
Berechne: 5 * 3 = 15
Berechne: 15 * 10 = 150
Berechne: 3 * 3 = 9
Ergebnis: 150 + 9 = 159  
```
**Hinweis:** Die Zahlen _53_ und _3_ in den ersten beiden Zeilen wurden vom Benutzer eingegeben.

### Tipps
- Ermittle die Einer- und Zehnerstelle wie in Aufgabe 1
-









Kannst du $73² = 73 * 73$ schnell im Kopf ausrechnen? Nein? Mit dem normalen Multiplikationsverfahren,
geht das nicht so einfach. Zum Glück gibt es schlauere Methoden.

# Die Idee
Anstatt $73²$ direkt auszurechnen, rechnet man:

$$ 73² = 70 * 76 + 3² $$  

Hierbei untersuchen wir die zu quadrierende Zahl $73$ und suchen die kleinste Zahl, so dass wir zur nächsten ganzen zweistelligen Zahl kommen. In unserem Fall ist das die $3$, denn $73 - 3 = 70$. Für die Zahl $46$, wäre es die $4$, da $46 + 4 = 50$.


Der komplizierte Teil ist nun das Produkt: $70 * 76$ zu berechnen. Allerdings kann man $70 = 10 * 7$ schreiben.

$$ 70 * 76 = 10 * 7 * 76 $$

Die Multiplikation mit $10$ ist einfach, indem man an das Ergebnis einen $0$ anhängt. Es bleibt das Produkt von $7 * 76$ zu berechnen.
Auch hier kann man den gleichen Trick anwenden, und die zweistellig Zahl durch einen Multiplikation mit 10 ausdrücken


$$ 7 * 76 = 7 * (70 + 6) $$  
$$ 7 * 70 + 7 * 6 = 7 * 7 * 10 + 7 * 6 $$

Wir berechnen die Produkte $7 * 7 = 49$ und $7 * 6 = 42$ und verwenden die Ergebnisse:

$$ 7 ∗ 76 = 49 * 10 + 42 = 532 $$

Nun haben wir alles ausgerechnet, wobei $3³ = 9$ ergibt, und verwenden die Ergebnisse:

$$ 72² = 532 * 10 + 9 $$
$$ = 5320 + 9 = 5329$$

# Die Idee in Python mit Variablen

Wir wollen die Zahl $z = x + y$ quadrieren, also das Ergebnis von $z²$. Hierbei ist $y$ eine einstellige Zahl und $x$ einen zweistellig Zahl, deren letzte Stelle $0$ ist. Aus dem obigen Beispiel:

$$ z = x + y $$
$$ z = 73, x = 70, y = 3 $$

Wir suchen nun die Zahl $u$, um unsere Zahl $z$ auf die nächste zweistellige Zahl mit einer $0$ an zweiter Stelle zu finden. Z.B für die Zahl $46$, ist dies die $4$, da $46 + 4 = 50$.

Um diese Zahl $u$ zu finden, müssen wir zwei Fälle unterscheiden:
- falls $y > 5$ ist, müssen erhalten wir $u = 10 - y$. Z.B die $4$, falls die Zahl $z = 46$
- falls $y <= 5$ ist, ist $u = y$. Z.B die $3$, falls die Zahl $z = 73$

Wir suchen also das Ergebnis der Berechnung $z² = (z - u) * (z + u) + u²$. Für den Fall $z = 73$, $73² = (73 - 3) * (73 + 3) + 3² = 70 * 76 + 9$.
