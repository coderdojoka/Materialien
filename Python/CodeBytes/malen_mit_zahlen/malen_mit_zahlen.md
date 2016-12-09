---
autor: Mark  
datum: 25.11.2016  
minted_ausgabe: tmp_latex  
version: 1.0  
keine_sektions_nummern: ja  
titel: Malen mit Zahlen
---

# Erinnerung: Python Grundlagen
 
```python
# Text wiederholen
print("X" * 10) # XXXXXXXXXX

# Texte zusammensetzen aus Wiederholungen 
# ACHTUNG: Klammern, bei komplizierten Ausdrücken
text = "X" * 5 + "Y" * (1 + 3)
print(text) # XXXXXYYYY
 
# For-Schleife, die X,  XX, XXX ausgibt
for i in range(1, 4): # i = 1, 2, 3
    print("X" * i)    
```

# Erzeuge folgende Bilder

**Hinweis:** Die Punkte `···` sollen Leerzeichen darstellen.


# a{magic=minipageStart w=.5}

## Rechteck gefüllt: 10x5
```
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
```

# a{magic=minipageNext w=.5}

## Rechteck mit  4 Leerzeichen
```
····XXXXXXXXXX
····XXXXXXXXXX
····XXXXXXXXXX
····XXXXXXXXXX
····XXXXXXXXXX
```


# a{magic=minipageEnd}

# a{magic=minipageStart w=.5}

## Dreieck kopfüber: 6x6
```
XXXXXX
·XXXXX
··XXXX
···XXX
····XX
·····X
```

# a{magic=minipageNext w=.5}

## Dreieck kopfüber: 11x6
```
XXXXXXXXXXX
·XXXXXXXXX
··XXXXXXX
···XXXXX
····XXX
·····X
```

# a{magic=minipageEnd}

# a{magic=minipageStart w=.5}

## Dreieck: 11x6
```
·····X
····XXX
···XXXXX
··XXXXXXX
·XXXXXXXXX
XXXXXXXXXXX
```

# a{magic=minipageNext w=.5}

## Abgeschnittenes Dreieck
```
···XXXXX
··XXXXXXX
·XXXXXXXXX
XXXXXXXXXXX
```

# a{magic=minipageEnd}