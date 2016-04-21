---
minted_ausgabe: tmp_latex  
autor: Mark  
version: 1.0  
datum: 19.04.16  
titel: CodeBytes - Wie alt bist du?  
---

# Themen:
- Eingabe über die Konsole. Siehe dazu das Tutorial XY
- `if`-Abfragen. Siehe dazu das Tutorial XY

# Aufgabe:
Schreibe ein Programm, dass dich auffordert dein Geburtsdatum einzugeben. Rechne anhand des Datums aus, wieviele Jahre du alt du bist.

# Beispielablauf:

```
Wann bist du geboren?
Geburtsjahr: 1993
Geburtsmonat: 2
Geburtstag: 16

Du bist 23 Jahre alt.
```
**Hinweis:** Die Zahlen `1993`, `2` und `16` sind hier die Benutzereingabe.

# Tipps:

Das heutige Datum bekommst du so:

```python
# Das Paket datetime einmal importieren
import datetime

# aktuelles Datum abfragen
heute = datetime.datetime.now()

jahr = heute.year
monat = heute.month
day = heute.day
```  

- Beachte, das `input(..)` einen Text liefert, konvertiere ihn mittels `int(..)` in eine Zahl
- Lies dein Geburtsdatum als drei einzelne Zahlen ein: Jahr, Monat, Tag
- Unterscheide zwei Fälle: Du hattest dieses Jahr schon Geburtstag oder du hattest dieses Jahr noch nicht Geburtstag.
