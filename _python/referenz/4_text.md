---
author: mark
date: 2016-04-22
title: Text
layout: referenz
topic: py_ref
uid: ref4
tags: [t_text]
order: 4
next: ref5
prev: ref3
---

Ein Text ist im Prinzip nur eine Liste von Buchstaben und Zeichen.
Man kann daher Listenfunktionen wir `len(..)`, den Zugriff auf Element
mittels `text[1]` verwenden oder einen Text Buchstabenweiße mit einer `for`-Schleife durchlaufen. Mehr dazu in der Sektion über Listen.

## Texte kombinieren
Texte kann man mit dem `+`-Operator aneinander anfügen.

```python
begruessung = "Hallo "
text = begruessung + "Mark" # "Hallo Mark"
print(text)

# Texte kann man auch multiplizieren/wiederholen
text = "Ha" * 3 # HaHaHa
print(text)
```

## Länge eines Texts
Die Funktion `len(..)` ermittelt die Länge von Texten, d.h. die Anzahl an Buchstaben/Zeichen aus denen der Text besteht.

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

buchstabe = text[6]
print(buchstabe) # = 'W'
```

**ACHTUNG:** Wir beginnen bei `0` zu zählen, die `1` beschreibt also den zweiten Buchstaben!

## Texte aufspalten
Einen Text kann man an einem Trennzeichen oder sogar einem Wort aufspalten.

```python
text = "hallo#welt#test"
teile = text.split("#")
print(teile)
```

## Texte zusammenfügen

Eine Liste von Textstücken kann man wieder zu einem Text zusammenfügen:

```python
teile = ["hallo", "welt", "test"]
text = " ".join(teile) # klebt die Teile mit Leerzeichen dazwischen zusammen
print(teile)
```

## Texte sind unveränderlich

Man kann in einen Text nicht ohne weiteres verändern:

```python
text = "Hallo Welt"
text[1] = "o" # Erzeugt einen Fehler!
```

## Texte und Encodierungen

Wie der Computer Texte und insbesondere Sonderzeichen interpretiert hängt von der verwendeten Codierung ab.
Relevant sind im Prinzip Byte Codierungen und UTF-8 Codierung.

**Wichtig:** Als Byte-Codierung werden die Buchstaben als Zahlen interpretiert.

```python
text1 = "Hallo Welt" # utf-8 Text
text2 = b"Hallo Welt" # Byte-Text

print(text1[0], text2[0]) # => H 72

text2b = text2.encode() # utf-8 in Byte-Text
text2u = text2b.decode() # Byte-Text in utf-8 Text
```

Dies macht vorallem bei Sonderzeichen (Nicht-Ascii Zeichen) einen Unterschied, da diese nicht als ein Zeichen sondern als mehrere dargestellt werden!

```python
text1 = "äöü"
text2 = text1.encode()

print(len(text1), text1) # => 3 äöü
print(len(text2), text2) # => 6 b'\xc3\xa4\xc3\xb6\xc3\xbc'

```