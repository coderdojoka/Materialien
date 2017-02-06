---
date: 2017-01-25
author: Mark
version: 1.0
uid: ka_for
type: exercise
layout: exercise
folder: einfach
title: Kleine Aufgaben • Schleifen
tags: [t_for, t_while]
related_exercises: [ka_input, ka_if]
---

Hier findest du ein paar kleiner Aufgaben, die du programmieren sollst.
Sie werden immer komplizierter! Falls du nicht mehr weiter weißt,
kannst du dir die Lösung ansehen, nachprogrammieren und verstehen.

## Quadrate der Zahlen von 0 bis 20
- gib die Quadrate von 0 bis 20 aus
- das Quadrat einer Zahl `z` ist das Produkt der Zahl mit sich selbst `quadrat = z * z`

**Tipp:** `range(..)`

[Lösung](#code1){:.show_solution}
{% highlight python %}
{% include_relative code/quadrate20.py %}
{% endhighlight %}{: .hidden #code1 }

<hr>

## Quadrate kleiner 100
- gib alle Quadratzahlen `1, 2, 4, 9, ...` aus
- ist die aktuelle Quadratzahl größer 100, hör auf


[Lösung](#code2){:.show_solution}
{% highlight python %}
{% include_relative code/quadrate100.py %}
{% endhighlight %}{: .hidden #code2 }

<hr>

## Keine Zufälle mehr
- lies einen Text von der Konsole ein
- ist der Text `'stop'`, dann ist das Programm zu Ende
- ansonsten gib eine zufällige Zahl ein und beginne von vorne

**Tipp:** `range(..)`

[Lösung](#code3){:.show_solution}
{% highlight python %}
{% include_relative code/kein_zufall.py %}
{% endhighlight %}{: .hidden #code3 }

<hr>



TODO: add more