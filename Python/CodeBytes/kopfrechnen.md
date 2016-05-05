---
autor: Mark  
datum: 05.05.2016  
minted_ausgabe: tmp_latex  
version: 1.0  
keine_sektions_nummern: ja  
titel: Kopfrechnen
---

# Aufwärmen: Einer- und Zehnerstellen

Eine zweistellige Zahl $X = ZE$ kann man in ihre Zehnerer (Z)- und Einerstelle (E) aufteilen. Es gilt:

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

Wie schnell kannst du im Kopf eine beliebige zweistellige Zahl mit einer einstelligen multiplizieren?

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
