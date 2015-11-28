---
titel: py2cd - Bilder und Animationen
autor: Mark Weinreuter
datum: 28.11.2015
version: 0.1
minted_ausgabe: tmp_latex
---


Ein gutes Spiel zeichnet sich durch coole Grafiken und Animationen aus.
Mit den vorhanden Mittel ist es jedoch ein bisschen umständlich alles
selber aus Rechtecken, Kreisen, etc... selbst zu zeichnen.  

Deswegen ist es eine gute Idee Bilder in Bildbearbeitungsprogrammen
zu Malen oder von anderen Malen zu lassen :). Diese Bilder können dann ganz
einfach geladen und angezeigt werden.

Ein Bild laden und anzeigen
===========================

Um ein Bild zu laden gibt es den _BilderSpeicher_. Dieser verwaltet alle Bilder,
die du benötigst. Du musst Bilder einmal laden und kannst sie dir
beliebig oft wieder holen und anzeigen lassen.
Damit du dein Bild später wiederfindest, musst du jedem Bild einen eindeutigen
Namen geben:

```{.python include=../../../Beispiele//py2cd/bilder_animationen.py firstline=9 lastline=18}
 will be replaced
```

## Woher weiß mein Computer welches Bild geladen werden soll?
Das Bild, das angezeigt werden soll muss auf deinem Computer gespeichert sein.
Dann muss man den Dateinamen und Pfad, d.h. alle Ordner- und Unterordnernamen, dorthin angeben.
 
> Ein Dateipfad kann auf 2 Arten angeben werden. Als **relativer** Pfad oder als **absoluter** Pfad.  
> Ein relativer Pfad bedeutet, dass man den Pfad von dem Ordner aus angibt, in dem auch dein Programm liegt.
> Gibt man also den Dateipfad als 'scratch.png' an, so sucht Python nach der Datei mit dem
> Namen 'scratch.png', im dem Ordner, in dem auch dein Programm liegt.  
>  
> Ein absoluter Pfad beginnt immer auf unterster Ebene des Dateisystems. D.h. willst du
> eine Datei auf dem Desktop laden, könnte der Pfad unter Windows z.B. so lauten: _'C:\\Users\\Mark\\Desktop\\scratch.png'._    
>  
> Das Einfachste ist, wenn du Bilder immer dem Ordner speicherst, indem dein Programm liegt.
> Du kannst sie natürlich auch in einen Unterorder z.B. 'Bilder' in deinem Programm-Ordner
> speichern und den Pfad angeben als: _'Bilder/scratch.png'_

## Bilder skalieren und rotieren
Man kann von Bilder und Animationen ganz leicht die Größe ändern und diese drehen.
Bilder werden dabei immer um ihren Mittelpunkt gedreht, und auch beim Skalieren 
bleibt der Mittelpunkt des Bildes fest.

``` {.python include=../../../Beispiele//py2cd/bilder_animationen.py firstline=21 lastline=28}
 will be replaced
```

Animation laden und anzeigen
===========================

Eine Animation ist eigentlich nur eine Folge von Bilder,
die schnell hintereinander durchgewechselt werden. Dementsprechend
benötigt man für eine Animation eine Liste von Bilder und Zeitabständen,
in denen die Bilder gewechselt werden sollen.

``` {.python include=../../../Beispiele//py2cd/bilder_animationen.py firstline=30 lastline=50}
 will be replaced
```

## Eine Animation steuern

Eine Animation kann gestartet, pausiert und gestoppt werden. Diese Funktionen verhalten sich,
wie man erwartet, so wird z.B. die Animation nach einer Pause wieder an der pausierten Stelle fortgesetzt.


``` {.python include=../../../Beispiele//py2cd/bilder_animationen.py firstline=52 lastline=59}
 will be replaced
```

