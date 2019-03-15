---
author: Mark
date: 2018-06-22
title: Kommandozeilen-Argumente
layout: referenz
topic: python-referenz
uid: python-referenz-9
tags: [t_dict]
order: 9
next: python-referenz-10
prev: python-referenz-8
---

Manchmal ist es nützlich das Programm über die Kommandozeile aufzurufen, und dabei direkt Startwerte zu übergeben.

```bash
python program.py erstesArgument 2 "Argument mit Leerzeichen"
```

## Kommandozeilen Argumente abfragen

Diese Start-Werte werden in der Liste `sys.argv` gespeichert.

```python
import sys

# Kommandozeilen-Argumente lesen
argmumente = sys.argv
print(argumente)

```

Als erster Eintrage steht immer der Programm-Name, danach folgen die Argumente der Reihe nach als **Texte**.

| Index | Wert                         |
| :---: | :--------------------------- |
| 0     | `"program.py"`                 |
| 1     | `"erstesArgument"`           |
| 2     | `"2"`                        |
| 3     | `"Argument mit Leerzeichen"` |

## Beispiel zur Verwendung

Dieses Programm erwartet einen Text und wie oft der Text wiederholt werden soll.

```python

import sys
argumente = sys.argv

if len(argumente) < 3:
    print("Bitte aufrufen mit: python program.py [text] [wiederholungen]")
    exit(-1)

text = argumente[1]
wiederholungen = int(argumente[2]) # in Zahl konvertieren

print(text * wiederholungen)
```

Aufruf über:

```bash
python program.py "ha" 100
```