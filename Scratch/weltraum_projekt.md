---
autor: Ricarda
datum: 22.04.16
keine_sektions_nummern: ja
version: 1.0
titel: Weltraum
---

## Die Idee:

Gestalte ein Weltraumspiel, auf Grundlage des Spiels "weltraumspiel.sb2".
 
## Vorbereitungen:

- Kopiere dir den Ordner "Weltraum" von einem der USB-Sticks und öffne das Scratchprojekt "weltraumspiel.sb2" mit Scratch (online oder offline, besser aber offline).  

- Untersuche die schon vorhandenen Figuren. Es gibt schon:

    - eine Rakete
    - zwei Figuren, für den Hintergrund
    - die Figur Asteroiden


## Durchführung

### Asteroiden

Das schon vorhandene Skript der Asteroiden lässt immer neue Steine entstehen. Diese sammeln sich aber nur am oberen Bildrand und fallen nicht nach unten.

- Lasse die Asteroiden nach unten fallen.

- Erstelle dann folgende Überprüfungen für die Asteroiden:

   - lösche den Klon, wenn der Rand berührt wird

   - überprüfe ob die Rakete berührt wird 

Erstelle eine Variable "Schild" und setzte sie z.B. auf 5, die bei einem Treffer heruntergezählt wird. Das "Schild" wird durch die Treffer schwächer und wenn "Schild" = 0, dann soll das Spiel gestoppt werden.

### Rakete

Damit die Rakete nicht von den Asteroiden getroffen wird, muss sie bewegbar sein.

- mache die Rakete durch die Pfeiltasten oder die Maus bewegbar


## Erweiterung

Im Ordner "Weltraum" gibt es noch weitere Figuren für dieses Spiel. Es gibt einen Ball und ein Schild. 

- lade beide Figuren in das Spiel und schaue die schon vorhandenen Skripte dafür an

### Schild

Die Figur "Schild" soll die Variable "Schild" darstellen. Die Idee ist, das bei jedem Treffer das nächste Kostüm des Schilds angezeigt wird und so deutlich wird, das es immer schwächer wird. Wenn das letzte Kostüm erreicht ist, ist das Schild verschwunden und das Spiel ist verloren.


### Ball

Der Ball soll als Geschoss gegen die Asteroiden eingesetzt werden. Er kann durch drücken der Leertaste abgeschossen werden. Baue beim Asteroiden die Überprüfung ein, das er gelöscht wird, wenn der Ball berührt wird. 

## Weiterführende Aufgaben (können auch zuhause gelöst werden)

1. Erstelle eine "Punkte" Variable und einen Gegenstand, den die Rakete einsammeln soll um Punkte zu erhalten. Nimm die Skripte der Asteroiden um den Gegenstand zu klonen und passe die Häufigkeit des Klonens so an, dass der Gegenstand nur selten und zufällig verteilt kommt. Baue eine Überprüfung ein, ob die Rakete den Gegenstand eingesammelt hat und zähle gegebenenfalls die Punkte entsprechend hoch.

2. Erstelle ein eigenes Spiel, das die Funktionen "erzeuge Klon von ..." und "Wenn ich als Klon entstehe" verwendet. Lass deiner Fantasie freien Lauf. Erstelle z.B. eine Ameisenkolonie oder ein Fabrik auf der Gegenstände auf einem Fließband entlang fahren.
