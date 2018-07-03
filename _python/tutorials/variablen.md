---
layout: tutorial
title: Variablen
author: Mark
date: 2015-12-01
uid: tut_var
level: 1
topic: basics
type: tutorial
tags: [t_input]
---

# Was sind Variablen

Als Programmierer sind Variablen deine besten Freunde. Variablen werden
benutzt, um darin Werte zu speichern. Du kannst sie dir wie eine kleine
Schublade vorstellen. Auf der Schublade steht der Name deiner Variablen.

![Variablen als Schubladen]({{ site.url }}/_assets/imgs/schublade.png)

Du kannst die Schublade aufmachen und einen Wert z.B. eine Zahl
reinlegen. Genauso kannst du zu jeder Zeit die Schublade aufmachen, um
den Wert zu lesen.

## Variablen in Python

In Python sieht das Ganze so aus:

{% include read_lines.md rel_file="code/variablen.py" %}
{% highlight python %}{% include select_lines.md lines=lines offset=2 limit=2 %}{% endhighlight %}

Auf der linken Seite des `=`-Zeichens steht der Name der Variablen, die erstellt wird.
Auf der rechten Seite steht der Wert, der ihr zugewiesen wird. Mithilfe
des `print()`-Befehls, kann der Wert einer Variablen ausgegeben werden.

{% highlight python %}{% include select_lines.md lines=lines offset=5 limit=1 %}{% endhighlight %}

Der Wert der Variablen kann ganz leicht geändert werden.

## Rechnen mit Variablen

Man kann Zahlen in Variablen speichern, warum also nicht auch mit ihnen
rechnen.

{% highlight python %}{% include select_lines.md lines=lines offset=12 limit=6 %}{% endhighlight %}

Hier gibt es zwei neue Variablen: `zahl` und `ergebnis`. Die Variable bekommt als Wert
das Ergebnis der Berechnung von `code * 5` zugewiesen.

{% highlight python %}{% include select_lines.md lines=lines offset=19 limit=5 %}{% endhighlight %}

Es können alle Grundoperationen wie Plus, Minus, Mal, Geteilt verwendet werden. Allerdings sind hierbei Rechenregeln wie ’Punkt vor Strich’ zu beachten.

## Merkregel

> Um eine Variable zu erzeugen oder zu verändern steht die Variable auf der
> linken Seite des `=`-Zeichens, z.B: `zahl = 42`
>
> Um den Wert zu lesen steht die Variable auf der rechten Seite des `=`-Zeichens.  
> Z.B. zum Verändern des Wertes einer anderen Variablen: `ergebnis = zahl + 1`

## Variablen mit sich selbst verrechnen

Anfänglich mag es vielleicht etwas verwirrend erscheinen, aber man kann den Wert einer Variablen überschreiben, indem man den vorherigen Wert in einer Berechnung verwendet:

{% highlight python %}{% include select_lines.md lines=lines offset=24 limit=3 %}{% endhighlight %}

Hier gilt einfach die Merkregel von oben. Zuerst wird die rechte Seite berechnet. Es wird der Wert von `zahl` gelesen und `1` dazu addiert. Dann wird die Variable auf der linken Seite auf den neu ausgerechneten Wert gesetzt.

## Variablen erstellen

Variablen können auf verschiedene Arten mit Werten gefüllt werden. Der grundlegende Aufbau ist aber immer der Gleiche.

![Variablen erstellen]({{ site.url }}/_assets/imgs/variablen.svg)

## Aufgaben

Damit du mit Variablen vertrauter wirst, spiele einfache ein bisschen mit Variablen herum!

- Erstelle eine Variable und ändere mehrmals ihren Wert
- Gib den Wert deiner Variablen mittels `print` aus und sieh wie er sich verändert
- Überschreibe den Wert deiner Variablen mit 10-fachen des    ursprünglichen Wertes
- Finde heraus, welche Buchstaben, Zahlen, Sonderzeichen in Variablen    erlaubt sind. Um dies auszuprobieren starte mit einem Namen der nur Buchstaben enthält, z.B. `zahl`. Starte das Programm, es sollte erfolgreich durchlaufen. Füge nun neue Zeichen hinzu und teste erneut das Program.

## Ausblick

Man kann in Variablen natürlich nicht nur Zahlen speichern. Es kann z.B. auch Text darin gespeichert werden.

{% highlight python %}{% include select_lines.md lines=lines offset=28 limit=3 %}{% endhighlight %}

Mehr Infos zum Umgang mit Text findest du in dem gleichnamigen Tutorial ’Text’.
