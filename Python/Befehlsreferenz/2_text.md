---
autor: Mark Weinreuter
version: 0.5
datum: 23.01.16
minted_ausgabe: tmp_latex
titel: Python - Befehlsübersicht
---

# Text

Ein Text ist im Prinzip nur eine Liste von Buchstaben und Zeichen.
Man kann daher Listenfunktionen wir `len(..)`, den Zugriff auf Element
mittels `text[1]` verwenden oder einen Text Buchstabenweiße mit einer `for`-Schleife durchlaufen. Mehr dazu in der Sektion über Listen.

## Texte kombinieren
Texte kann man ’+’ aneinander anfügen.
```python 
begruessung = "Hallo "
text = begruessung + "Mark" # "Hallo Mark"
print(text)

# Texte kann man auch multiplizieren/wiederholen
text = "Ha" * 3 # HaHaHa
print(text)
```

## Länge eines Texts
Die Funktion `len(..)` ermittelt die Länge von Texten, Listen, etc.
```python
text = "Hallo Welt"
laenge = len(text) # = 10
print(laenge)
```

## Einen einzelnen Buchstaben abfragen
Einen Buchstaben kann man über seine Position im Text abfragen:
```python
text = "Hallo Welt"
buchstabe = text[1]
print(buchstabe) # = 'a'
```
**ACHTUNG:** Wir beginnen bei 0 zu zählen, die 1 beschreibt also den zweiten Buchstaben!

## Texte sind unveränderlich
Man kann in einen Text nicht ohne weiteres verändern:
```python
text = "Hallo Welt"
text[1] = "o" # Erzeugt einen Fehler!
```