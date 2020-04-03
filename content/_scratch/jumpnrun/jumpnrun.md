---
title: Mein erstes Projekt
author: Ricarda
date: 2019-03-15
version: 1.0
uid: jumpnrun_einstieg
permalink: /scratch/jumpnrun_einstieg
layout: tutorial
type: tutorial
---

Bevor du loslegst:
- Ein Jump'n'Run-Spiel zu programmieren, ist eine Herausforderung. Aber es lohnt sich durchzuhalten!

- Falls du nach diesem Tutorial weitere Ideen umsetzten möchtest, könnte auch dieses Tutorial interessant für dich sein: https://de.scratch-wiki.info/wiki/Jump%27n_Run

- Damit die erste Hürde vereinfacht ist, verwendet dieses Tutorial eine Vorlage in der schon die ersten Figuren und Hintergründe vorhanden sind. Später kannst du aber auch die Bilder austauschen und so deine eigene Gestaltung vornehmen.

- Die hier verwendeten Bilder und weitere super dazu passende Grafiken sind hier zu finden: https://opengameart.org/content/platformer-art-deluxe

- Wir erstellen hier 3 verschiedene Level. Du kannst diese später durch eigene Level ergänzen.

- Hier kannst du ausprobieren, wie dein Spiel am Ende des Tutorials aussehen könnte: 

<iframe src="https://scratch.mit.edu/projects/382019558/embed" allowtransparency="true" width="485" height="402" frameborder="0" scrolling="no" allowfullscreen></iframe>


### 1.Öffne die Tutorial-Version des Spiels:
[https://scratch.mit.edu/projects/382408036/editor/](https://scratch.mit.edu/projects/382408036/editor/)

Hier sind die ersten Figuren und Hintergründe schon im Projekt gespeichert. Du solltes folgende Figuren sehen:
- Alien 1, Alien 2, Alien 3: Suche dir hier die Figur aus, die du am besten findest und **lösche die anderen beiden Aliens**. Diese Figur wird dein Hauptcharakter.
- Dot: Diese Figur sieht seltsam aus, ist aber wichtig! Genaueres klären wir später.
- Plattformen: Diese Figur hat verschiedene Kostüme für die verschiedenen Leven, die wir nachher programmieren. So sieht jedes Level anders aus. Die Figur soll auf diesen Plattformen später entlanglaufen können.
- Abgrund: Bisher ist der Abgrund nur Wasser. Es gibt wieder 3 verschiedene Kostüme für die 3 geplanten Level. Später könnte hier noch Lava anstelle von Wasser eingesetzt werden oder böse Stacheln ...
- Ziel: Diese Figur markiert das Ende eines Levels. Ziel jedes Levels ist es die Flagge zu erreichen.
- Leben: Das kleine Herz zeigt an, wie viele Leben deine Spielfigur noch hat. Die Programmierung dieser Lebensanzeige ist die letzte Herausforderung dieses Tutorials. 


### 2. Programmiere deine Hauptfigur:

Das geht einfacher als du denkst. Wir machen für diese Figur nur 2 kleine Skripte und den Rest der Programmierung verlagern wir in Schritt 3 und die Figur "Dot".

- Damit es so aussieht, als würde die Figur laufen, welchseln wir einfach immer wieder zwischen den ersten beiden Kostümen hin und her. Dazwischen sollte eine kleine Pause sein.

- Das zweite Skript ist auch sehr einfach. Sobald das Spiel gestartet wird, soll das Alien immer zur Figur Dot gehen.

Der erste Schritt ist geschafft! Aber bisher ist noch nicht viel zu sehen.

### 3. Programmiere die Bewegungen:

Die Hauptfigur soll sich durch drücken der Pfeiltasten nach links und rechts bewegen können. Verwende hier nicht die "Wenn Pfeil nach ... gedrückt"- Blöcke direkt, sondern einen "wiederhole fortlaufend"-Block, sowie einen "falls ... dann"-Block mit dem "Taste Pfeil nach ... gedrückt?"-Block aus der Kategorie "Fühlen". Probiere aber beide Varianten aus. Warum ist die zweite, etwas kompliziertere Variante besser?

Später soll das Alien nur auf den Plattformen laufen können und ansonsten nach unten fallen, bis es wieder eine Plattform berührt. Verwende den "wird ... berührt?"-Block und ein paar andere, damit das Alien immer nach unten fällt, wenn die Plattform **nicht** berührt wird.

Jetzt soll die Figur auch springen können und zwar immer nur dann, wenn sie festen Boden unter den Füßen hat. Auch hier benötigst du den "wird ... berührt?"-Block und einige andere. 

Die Werte für die Fallgeschwindigkeit und die Sprunghöhe musst du einfach ausprobieren. Im Beispiel oben fällt die Figur bei jeder Wiederholung um -7 in y-Richtung und springt, beim Klicken der Leertaste, in 5 Wiederholungsschritten um je 20 in y-Richtung nach oben. Um die perfekten Werte für dein Spiel zu ermitteln, musst du:

**Abspeichern und Testen!**

Wenn alles passt, sollte die Figur jetzt nach links und rechts gehen und springen können.

