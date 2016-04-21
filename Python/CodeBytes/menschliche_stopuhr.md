---
minted_ausgabe: tmp_latex
autor: Mark
version: 1.0
datum: 19.04.16
titel: CodeBytes - Menschliche Stopuhr
---

# Themen:
- Eingabe über die Konsole. Siehe dazu das Tutorial XY
- Zufallszahlen. Siehe XY
- Ggf. auch `if`-Abfragen. Siehe dazu das Tutorial XY

# Aufgabe:
Schreibe ein Programm, dass sich eine zufällige Zeit zwischen 10 und 30 Sekunden ausdenkt. Wenn die ENTER-Taste gedrückt wird, soll die Startzeit gemessen werden (s. Tipps).
Beim erneuten Drücken der ENTER-Taste, soll eine zweite Zeit gemessen werden. Aus der Start- und Stopzeit kannst du den Zeitunterschied errechnen, mit der gewünschten Zeit vergleichen und eine Meldung ausgeben, wie gut die Schätzung ist.


# Beispielablauf:
```
Versuche so gut wie möglich abzuschätzen, wann die unten gezeigte Zeit  
abgelaufen ist.  
Wenn du bereit bist drücke ENTER, um die Stopuhr zu starten.  
Drücke erneut ENTER, wenn du glaubst, dass die Zeit abgelaufen ist.

Stoppe: 42 Sekunden.
<ENTER>
...
<ENTER>

Du hast 36.7 Sekunden gestoppt.

```
**Hinweis:** `<ENTER>...<ENTER>` stellt hier nur die Benutzereingabe und Wartezeit dar.


# Tipps:
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