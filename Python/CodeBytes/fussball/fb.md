---
minted_ausgabe: tmp_latex  
autor: Rafael, Mark  
version: 1.0  
datum: 14.05.16  
keine_sektions_nummern: ja  
titel: CodeBytes - Fußball
---

# Themen:
- `if`-Abfragen. Siehe dazu das Tutorial XY
- Schleifen. Siehe dazu das Tutorial XY

# Aufgabe:

Deine Freunde und du haben nie Zeit Fußball zu schauen, weil ihr immer
Hausaufgaben machen und für Klassenarbeiten lernen müsst. Aber du kannst
aus deinem Zimmer den Fernseher hören! Du bekommst also immer mit, wenn
eine Mannschaft ein Tor schießt.

![Tor!!!](Fussball_Bild.png){w=.45}

Schreibe ein Programm, dass:

- Solange auf Eingabe des Benutzers wartet, bis `Abpfiff` eingegeben wird
- Wird eine `1` oder eine `2` eingegeben, hat die erste bzw. zweite Mannschaft ein Tor geschossen.
- Wurde `Abpfiff` eingegeben, ist das Spiel zu Ende. Gib das Ergebnis des Spiels aus.


# Vorüberlegung
- Das Spiel läuft bis `Abpfiff` eingegeben wird, wie kannst du Programm solange laufen lassen, bis das eingegeben wird?
- Du musst die Tore der beiden Mannschaften speichern, um sie zum Schluss ausgeben zu können

# Beispielablauf:

```
Gib eine 1 bzw. 2 für ein Tor der ersten bzw. zweite Mannschaft ein.
Gib `Abpfiff` ein, wenn das Spiel zu Ende ist:

1
1
2
1
Abpfiff

Das Spiel ist 3:1 ausgegeben.
```

**Hinweis:** Die Zahlen `1`,`2` und `Abpfiff` werden vom Benutzer eingegeben.
