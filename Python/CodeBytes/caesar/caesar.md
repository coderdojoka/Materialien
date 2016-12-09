---
autor: Mark  
datum: 09.12.2016  
minted_ausgabe: tmp_latex  
version: 1.0  
keine_sektions_nummern: ja  
titel: Caesar Verschlüsselung
---

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
