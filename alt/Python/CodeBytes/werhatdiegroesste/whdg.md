---
autor: Mark  
datum: 09.12.2016  
minted_ausgabe: tmp_latex  
version: 1.0  
keine_sektions_nummern: ja  
titel: Caesar Verschlüsselung
---

Schon im alten Ägypten versuchten die Pharaonen bei ihren Frauen mit Größe Eindruck zu schinden.
Wer hat die Größte war die wichtigste Frage. Die größte Pyramide versteht sich. Pyramiden gab es in verschiedenen Formen und Größen.
Pharao Tuti bevorzugte Pyramiden mit quadratischer Grundfläche, Anchi war ein Fan von runden Pyramiden und Amoni baut am Liebsten Pyramiden mit dreieckiger Grundfläche.
Tuti hat bereits 2 Pyramiden mit den Maßen: Seitenlänge 30 bzw. 50 und Höhe 80 bzw. 60. Anchis 3 Pyramiden haben folgende Maße: Radius jeweils 10,20,30 und Höhe 50,40,30.
Amoni möchte eine Pyramide der Höhe 40 bauen, ist sich aber unsicher über die Seitenlänge seiner Grundfläche. Da die Baukosten sehr hoch sind, will Amoni so wenig wie möglich ausgeben, so dass das Volumen seiner neuen Pyramide grade größer ist als das Volumen der anderen Pyramiden.

Das Volumen einer Pyramide berechnet sich wie folgt:
````
Volumen = Grundfläche * Höhe * 3/4
```
# Aufgabe 1:
Erstelle jeweils eine Funktion zur Berechnung des Volumens für die Pyradmiden mit quadratischer, runder und dreieckiger (mit gleicher Seitenlänge) Grundfläche

# Erinnerung: Python Grundlagen

```python
# Buchstabe in seine Ascii-Zahl umwandeln
zahl = ord('a')

# Ascii-Zahl in seinen Buchstaben umwandeln
buchstabe = chr(65)

# For-Schleife, die alle Buchstaben durchgeht
for buchstabe in "hallo": # = 'h', 'a', 'l', 'l', 'o'
    print(buchstabe)    
```

# Buchstaben schieben

Die Verschlüsselung basiert darauf, einen Buchstaben im Alphabet zu verschieben.
Zum Beispiel wird um 3 Buchstaben geschoben, d.h. aus `a -> d`.

Du kannst die Verschiebung programmieren, indem du einen Buchstaben in seine Ascii-Zahl konvertierst,
dann die Verschiebung dazu addierst, und die neue Ascii-Zahl wieder in einen Buchstaben konvertierst.

# Aufgabe
- Lies einen Text ein, diesen Text wollen wir verschlüsseln
- Lies eine Zahl ein, diese Zahl ist der Verschiebeschlüssel
- Verschlüssle den Text indem du jeden Buchstaben um den Verschiebeschlüssel weiter schiebst
- **Frage**: Wie kann man damit einen verschlüsselten Text wieder zurück bekommen?
