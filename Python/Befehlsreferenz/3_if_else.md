---
autor: Mark Weinreuter
version: 0.5
datum: 23.01.16
minted_ausgabe: tmp_latex
titel: Python - Befehlsübersicht
---
# Bedingungen und if-Abfragen

## Bedingung
Eine Bedingung ist entweder Wahr (True) oder Falsch (False).

```python
bedingung = 10 > 20 # False 
print("Die Bedingung ist:", bedingung)
```

## if-Abfragen
Eine if-Abfrage überprüft ob eine Bedingung Wahr oder Falsch ist.

```python
wert = 10 # Eine Variable mit einem beliebigen Wert (hier 10)

if wert > 20: # wird NUR ausgeführt wenn die Bedingung wahr ist
    print("Der Wert ist größer als 20") # (ACHTUNG: Einrückung)

# Hier gehts weiter (ACHUTUNG: Nicht eingerückt)
```

## if-else-Abfragen
Mit einer if-else Abfrage kann man auch auf eine nicht erfüllte Bedingung mit dem ’else’-Zweig reagieren.

```python
if wert > 20: # wird ausgeführt wenn die Bedingung erfüllt ist
    print("Der Wert ist größer als 20")
    
else: # wird ausgeführt wenn die Bedingung nicht erfüllt ist
    print("Wert ist kleiner oder gleich 20.")

# Hier gehts weiter (nicht eingerückt)
```

## Vergleichsoperationen:
Alle Vergleichsoperationen liefern entweder Wahr oder Falsch. Diese können als Bedingung in einer `if`-Abfrage verwendet werden.

### Standardvergleichsoperationen
```python
a = 10 
b = 20

a == b # = False
a != b # = True
a > b  # = False
a >= b # = False
a < b  # = True
a <= b # = True
```

### Überprüfen, ob ein Textstück in einem Text enthalten ist
```python
a = "Hallo Welt"

"allo" in a # = True
"oo" in a   # = False
```

### Überprüfung auf None
```python
a = "Hallo Welt"

a is None # = False
a is not None # = True
```
