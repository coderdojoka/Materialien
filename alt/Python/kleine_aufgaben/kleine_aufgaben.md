---
datum: 16.09.16  
autor: Rouven, Mark  
version: 1.0  
minted_ausgabe: tmp_latex  
titel: Kleine Aufgaben
---

Hier findest du ein paar kleiner Aufgaben, die du programmieren sollst. Sie werden immer komplizierter! Falls du nicht mehr weiter weißt, kannst du dir die Lösung ansehen, nachprogrammieren und verstehen.

# Durchschnitt ausrechnen
- Lies zwei Zahlen ein
- berechne den Durchschnitt dieser Zahlen und gib in aus

**Tipp:** `input(..)` und `int(..)`

# Rückgeldrechner
- Gib ein, wieviel Geld du hast in Euros
- Gib an wieviel du bezahlt hast in Cents
- Berechne daraus das Rückgeld

**Tipp:** `input(..)` und `int(..)`

# Im Jahr 2050
- Gib ein, in welchem Jahr du geboren bist
- Berechne daraus, wie alt du im Jahr 2050 sein wirst!

**Tipp:** `input(..)` und `int(..)`

# Süßigkeiten einkaufen
- Fordere den Bentzer auf einzugeben, wieviel Geld in Euro er hat.
- Berechne daraus, wieviele Gummibärchen, Lackritzschnecken, Bonbons, Kaugummis du dir kaufen kannst
- Preise: Gummibär: 2ct, Lackritzschnecke: 20ct, Bonbons: 10ct, Kaugummi: 25ct

**Tipp:** `input(..)`, `int(..)` und `\\` Division ohne Nachkommastellen

# Sekundenumrechner
- Fordere den Benutzer auf eine Stundenzahl einzugeben
- Berechne wie viele Sekunden das sind und gib das Ergebnis aus

**Tipp:** `input(..)` und `int(..)`


# Bargeld
- Gib ein, wieviele:
  - 2 Euro Stücke
  - 1 Euro Stücke
  - 50ct Stücke
  - 20ct Stücke
  - 10ct Stücke
  - 5ct Stücke
  - 1ct Stücke

  du hast. Berechne daraus wieviel Bargeld du zur Verfügung hast.

**Tipp:** `input(..)` und `int(..)` und Kopieren und Einfügen

# Durchschnittsgeschwindichkeit
- Gib an wieviele Kilometer du zurückgelegt hast
- Gib ein, wie viel Zeit du dafür benötigt hast
- Berechne die Durchschnittsgeschwindichkeit daraus

**Tipp:** `input(..)`, `int(..)`. Geschwindikgeit (km/h) errechnet man aus zurückgeleger Strecke durch vergangene Zeit.

# Wann bist du Hundert?
- Gib ein, wie alt du bist
- Errechne daraus, wann du 100 Jahre alt bist

**Tipp:** `input(..)` und `int(..)`


# Stopuhr
- Schreibe ein Programm, dass dir hilft die Zeit zu stoppen
- Starte die Stopuhr, wenn du auf Enter drückst
- Stoppe die Stopuhr, wenn du erneut auf Enter drückst
- Berechne wieviele Sekunden vergenangen willst (Du kannst auch die Zeit in Sekunden und Minuten Berechnen)

**Tipp:** `input(..)` und ggf. `%` (Divisionsrest berechnen). Die aktuelle Zeit in Sekunden bekommst du so:
```
import time
aktuelle_zeit = time.time()
```

# Schaltjahrrechner
- Schreibe ein Programm, dass errechnet, ob ein Jahr ein Schaltjahr ist
- Gib eine Jahreszahl ein, bestimme mit folgenden Bedingungen, ob es ein Schaltjahr ist:
  - Jahreszahl durch 400 teilbar: immer ein Schaltjahr
  - Durch 100 teilbar: Ist kein Schaltjahr
  - Falls durch 4 teilbar: Ist ein Schaltjahr

  Die Regel sind in der angegebenen Reihenfolge anzuwenden.

**Tipp:** `input(..)` und `if`


# Einmaleins-Rechner

- Schreibe ein Programm das dich 1x1-Aufgaben abfragt.
- Lass den Benutzer den Zahlenraum festlegen.
- Stelle dem Benutzer eine zufällige 1x1-Aufgabe aus dem gewünschten Zahlenraum
- Fordere ihn auf das Ergebnis einzugeben
- Vergleiche das Ergebnis mit dem berechneten korrekten Ergebnis und gib aus, ob der Benutzer recht hat
- Frage den Benutzer ob er eine neue Aufgabe lösen will und stelle und wiederhole ab Schritt 3

**Tipp:** `input(..)`, `while` und `if`
