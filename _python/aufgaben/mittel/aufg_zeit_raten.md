---
author: Mark
datum: 2016-22-04
title: Menschliche Stopuhr
layout: exercise
type: exercise
level: 2
tags: [t_input, t_if]
---

## Aufgabe:

1. Schreibe ein Programm, dass sich eine zufällige Zeit zwischen 10 und 30 Sekunden ausdenkt.
2. Wenn die ENTER-Taste gedrückt wird, soll die Startzeit gemessen werden (s. Tipps).
3. Beim erneuten Drücken der ENTER-Taste, soll eine zweite Zeit gemessen werden.
4. Aus der Start- und Stopzeit kannst du den Zeitunterschied errechnen
5. Vergleiche den Zeitunterschied der gewünschten Zeit aus 1. und gib eine Meldung aus, wie gut die Schätzung ist.

## Vorüberlegung:

- Stell dir vor, du hast eine Uhr in der Hand und jemand sagt dir wann du anfangen und
  aufhören sollst du messen. Anschließend sollst du sagen können,
  wie viele Sekunden du gemessen hast. Welche Werte musst du dir dafür merken
- Überlege dir, was eine akzeptable Abweichung von der Messzeit wäre.
  Z.B. eine Abweichung von 2 Sekunden ist ok. Für den Anfang kannst du diesen Teil aber erstmal weglassen

## Beispielablauf:

```text
Versuche so gut wie möglich abzuschätzen, wann die unten gezeigte Zeit  
abgelaufen ist.  
Wenn du bereit bist drücke ENTER, um die Stopuhr zu starten.  
Drücke erneut ENTER, wenn du glaubst, dass die Zeit abgelaufen ist.

Stoppe: 42 Sekunden.
<ENTER>
...
<ENTER>

Du hast 36.7 Sekunden gestoppt.
Das könnte besser sein :)
```

**Hinweis:** `<ENTER>...<ENTER>` stellt hier nur die Benutzereingabe und Wartezeit dar.

## Tipps:

Du kannst die aktuelle Zeit in Sekunden so ermitteln:

```python
# Das Paket time einmal importieren
import time

# aktuelle Zeit in Sekunden
sekunden = time.time()
```

Dies liefert dir das aktuelle Zeit in Sekunden als Kommazahl mit vielen Nachkommastellen. Hier siehst du, wie man nur eine Nachkommastelle anzeigen kann:

```python
meineZeit = 36.72345
print("Du hast %.1f Sekunden gestoppt." % meineZeit) # 36.7
```

Um Zahlen formatiert auszugeben, nutzt man Platzhalter: `%f` für Kommazahlen, `%d` für ganze Zahlen, innerhalb eines Textes.
Mittels `%.1f` gibt man an, dass man genau eine Nachkommastelle will. Hinter dem Text gibt man mit `% meineZeit` an, welcher Wert formatiert eingefügt werden soll.
