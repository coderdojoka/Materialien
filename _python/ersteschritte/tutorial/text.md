---
titel: Text
autor: Mark Weinreuter
datum: 1.12.15
version: 0.2
layout: page
group: ersteschritte
---

Warum Text?
===========

An vielen Stellen beim Programmieren hat man mit Text zu tun. Man muss
Texte lesen, auf bestimmte Buchstaben untersuchen, etc...

{% include read_lines.md rel_file="code/text.py" %}
{% highlight python %}{% include select_lines.md lines=lines offset=2 limit=3 %}{% endhighlight %}

Textstücke erkennt man daran, dass sie in einfachen `'...'` oder doppelten `"..."`
Anführungszeichen stehen.

Operatoren
==========

Man kann Textstücke kombinieren:

{% highlight python %}{% include select_lines.md lines=lines offset=6 limit=3 %}{% endhighlight %}


Dies könnte man auch mit `print` direkt
ausgeben, da mehrere Parameter übgergeben werden können:

{% highlight python %}{% include select_lines.md lines=lines offset=10 limit=3 %}{% endhighlight %}


Analog zum Plus-Operator gibt es auch den Mal-Operator:

{% highlight python %}{% include select_lines.md lines=lines offset=13 limit=2 %}{% endhighlight %}


Länge eines Textes
==================

Manchmal ist es praktisch zu wissen aus wie vielen Buchstaben ein Text
besteht. Wir nennen dies auch die Länge eines Textes. Um die Anzahl der
Buchstaben, eines Textes zu ermitteln, benutzt man den Befehl `len(...)` (’length’
ist Englisch für Länge) wie folgt:

{% highlight python %}{% include select_lines.md lines=lines offset=16 limit=2 %}{% endhighlight %}

Texte als Buchstabenketten
==========================

Im Rechner intern, werden Texte als ein Kette von einzelnen Buchstaben
gespeichert. Dies können wir uns zu Nutzen machen.

{% highlight python %}{% include select_lines.md lines=lines offset=19 limit=3 %}{% endhighlight %}

Mit den eckigen Klammern am Ende der Text-Variablen `meinText[2]` deuten wir an, dass
wir den Buchstaben wissen wollen, der an der in Klammern geschrieben
Stelle steht.

> **Achtung:** Beim Programmieren fangen wir oft bei `0` mit dem Zählen an.
> D.h., dass wir, um den dritten Buchstaben zu erfahren, nicht `3`, sondern `2` in
> die eckigen Klammern schreiben müssen.


Texte sind unveränderlich
=========================

Eine interessante Eigenschaft von Texten ist, dass diese nicht verändert
werden können. Wenn wir versuchen, z.B. den vierten Buchstaben zu
überschreiben, erhalten wir einen Fehler:


{% highlight python %}{% include select_lines.md lines=lines offset=23 limit=2 %}{% endhighlight %}




Aufgaben
========

-   Erstelle eine Text-Variable und las dir den Wert ausgeben.

-   Spiele mit den Operatoren herum. Wie kannst du 100-mal `HaHa` ausgeben?

-   Lass dir den zweiten und vorletzen (Hinweis: berechne die Länge
    des Textes) Buchstaben von `Hallo Welt` ausgeben.

-   Probiere wie oben beschrieben den Text zu ändern. Bekommst du auch
    einen Fehler?
