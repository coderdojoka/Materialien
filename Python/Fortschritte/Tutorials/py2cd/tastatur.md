---
minted_ausgabe: tmp_latex
autor: Mark Weinreuter
datum: 3.12.15
version: 0.1
titel: py2cd Teil IV - Tastatur
---


Ein Spiel, bei dem der Benutzer nichts tun kann ist meistens ziemlich langweilig.
 Deswegen kann man auch mit py2cd Tastatureingaben abfangen und auf Mausbewegungen und Klicks reagieren.

**Hinweis:** Als Vorbereitung solltest du dich ein wenig mit Funktionen auskennen.
 Falls du dich damit noch nicht auskennst, hier eine kurze Info zu Funktionen.
 
> **Eine Funktion** ist ein Block von Code-Zeilen. Dieser Block bekommt einen eindeutigen Namen.
> Der Code-Block wird definiert, allerdings nicht sofort ausgeführt! Um diesen Block auszuführen,
> muss man lediglich dessen Namen gefolgt von runden Klammern im Quelltext verwenden.  
> Ein Beispiel für eine Funktion ist die `print(..)`-Funktion. Diese Funktion ist vordefiniert
> und druckt nur dann etwas in der Konsole aus, wenn du sie aufrufst.
>
> Eine eigene Funktion kannst du so definieren:
> ``` python
> def dein_name(): # hier definiert
>    # Zeile 1
>    # Zeile 2
>    # ....
>
> ...
> dein_name() # irgendwo später: hier aufgerufen
> ```


## Wenn eine Taste gedrückt wird

Oft will man wissen ob eine bestimmte Taste gedrückt wird, z.B. die Leertaste, um eine Figur springen zu lassen.
Diese Variante kann man als _'wenn gedrückt'_-Variante bezeichnet.

Um einen Tastendruck abzufangen, musst du eine Funktion definieren, die aufgerufen werden soll,
 wenn diese Taste gedrückt wird. Diese Funktion wird einmal aufgerufen, wenn die Taste
 nach unten gedrückt und einmal wenn diese Taste wieder losgelassen wird. 

So wird eine Funktion für einen Tastendruck definiert:
``` {.python firstline=51 lastline=53 include=../../../Beispiele/py2cd/tastatur.py}
will be replaced
```
Hierbei gibt der erste Parameter der Funktion an, ob die Taste gerade gedrückt (unten = Wahr/True) oder 
losgelassen wird (unten = Falsch/False).

Damit diese Funktion, auch bekannt ist, muss sie registriert werden: 
``` {.python firstline=94 lastline=95 include=../../../Beispiele/py2cd/tastatur.py}
will be replaced
```

## Solange eine Taste gedrückt ist

In vielen Fällen will meine Aktion ausführen, solange eine Taste gedrückt ist. Z.B. eine Spielfigur zu bewegen.
Für diesen Fall gibt es eine andere Funktion.
Diese Variante kann man als _'solange unten'_-Variante bezeichnet.

Dafür muss ebenfalls eine Funktion definiert werden, die solange wiederholt aufgerufen wird,
 wie die angegebenen Taste gedrückt gehalten wird.  
 
So wird eine Funktion definiert, die für gedrückte Tasten aufgerufen wird:
``` {.python firstline=69 lastline=70 include=../../../Beispiele/py2cd/tastatur.py}
will be replaced
```
 
 Damit diese Funktion, auch bekannt ist, muss sie registriert werden: 
``` {.python firstline=96 lastline=97 include=../../../Beispiele/py2cd/tastatur.py}
will be replaced
```


### Ein kleines Beispiel

Hier ein kleines Spiel, dass beide Arten von Tastendrücken empfängt. 
Zur Rechts-/Linksbewegung wird die _'solange unten'_-Variante verwendet und um einen Kreis 
 zu schießen, wird die _'wenn gedrückt'_-Variante verwendet.

``` {.python include=../../../Beispiele/py2cd/tastatur.py}
will be replaced
```