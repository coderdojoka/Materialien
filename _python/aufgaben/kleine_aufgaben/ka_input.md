---
date: 2016-09-16
author: Rouven, Mark
uid: ka_input
type: exercise
layout: exercise
folder: einfach
title: Kleine Aufgaben • Eingaben
tags: [t_input]
related_exercises: [ka_if, ka_for]
---

Hier findest du ein paar kleiner Aufgaben, die du programmieren sollst.
Sie werden immer komplizierter! Falls du nicht mehr weiter weißt,
kannst du dir die Lösung ansehen, nachprogrammieren und verstehen.

## Durchschnitt ausrechnen
- Lies zwei Zahlen ein
- berechne den Durchschnitt dieser Zahlen und gib in aus

**Tipp:** `input(..)` und `int(..)`

[Lösung](#code1){:.show_solution}
{% highlight python %}
{% include_relative code/Durchschnitt.py %}
{% endhighlight %}{: .hidden #code1 }

<hr>

## Rückgeldrechner
- Gib ein, wieviel Geld du hast in Euros
- Gib an wieviel du bezahlt hast in Cents
- Berechne daraus das Rückgeld

**Tipp:** `input(..)` und `int(..)`

[Lösung](#code2){:.show_solution}
{% highlight python %}
{% include_relative code/Rueckgeldrechner.py %}
{% endhighlight %}{: .hidden #code2 }

<hr>

## Im Jahr 2050
- Gib ein, in welchem Jahr du geboren bist
- Berechne daraus, wie alt du im Jahr 2050 sein wirst!

**Tipp:** `input(..)` und `int(..)`

[Lösung](#code3){:.show_solution}
{% highlight python %}
{% include_relative code/Im_Jahre_2050.py %}
{% endhighlight %}{: .hidden #code3 }

<hr>

## Süßigkeiten einkaufen
- Fordere den Bentzer auf einzugeben, wieviel Geld in Euro er hat.
- Berechne daraus, wieviele Gummibärchen, Lackritzschnecken, Bonbons, Kaugummis du dir kaufen kannst
- Preise: Gummibär: 2ct, Lackritzschnecke: 20ct, Bonbons: 10ct, Kaugummi: 25ct

**Tipp:** `input(..)`, `int(..)` und `\\` Division ohne Nachkommastellen

[Lösung](#code4){:.show_solution}
{% highlight python %}
{% include_relative code/Einkaufen.py %}
{% endhighlight %}{: .hidden #code4 }

<hr>

## Sekundenumrechner
- Fordere den Benutzer auf eine Stundenzahl einzugeben
- Berechne wie viele Sekunden das sind und gib das Ergebnis aus

**Tipp:** `input(..)` und `int(..)`

[Lösung](#code5){:.show_solution}
{% highlight python %}
{% include_relative code/Stundenumrechner.py %}
{% endhighlight %}{: .hidden #code5 }

<hr>

## Bargeld
- Gib ein, wieviele:
  - 2 Euro Stücke
  - 1 Euro Stücke
  - 50ct Stücke
  - 20ct Stücke
  - 10ct Stücke
  - 5ct Stücke
  - 1ct Stücke

  du hast. Berechne daraus wieviel Bargeld du zur Verfügung hast.

**Tipp:** `input(..)` und `int(..)` und Kopieren und Einfügen

[Lösung](#code6){:.show_solution}
{% highlight python %}
{% include_relative code/Geldrechner.py %}
{% endhighlight %}{: .hidden #code6 }

<hr>

## Durchschnittsgeschwindichkeit
- Gib an wieviele Kilometer du zurückgelegt hast
- Gib ein, wie viel Zeit du dafür benötigt hast
- Berechne die Durchschnittsgeschwindichkeit daraus

**Tipp:** `input(..)`, `int(..)`. Geschwindikgeit (km/h) errechnet man aus zurückgelegter Strecke durch vergangene Zeit.

[Lösung](#code7){:.show_solution}
{% highlight python %}
{% include_relative code/Streckenrechner.py %}
{% endhighlight %}{: .hidden #code7 }

<hr>

## Wann bist du Hundert?
- Gib ein, wie alt du bist
- Errechne daraus, wann du 100 Jahre alt bist

**Tipp:** `input(..)` und `int(..)`

[Lösung](#code8){:.show_solution}
{% highlight python %}
{% include_relative code/Wann_bist_du_100.py %}
{% endhighlight %}{: .hidden #code8 }

<hr>

## Stopuhr
- Schreibe ein Programm, dass dir hilft die Zeit zu stoppen
- Starte die Stopuhr, wenn du auf Enter drückst
- Stoppe die Stopuhr, wenn du erneut auf Enter drückst
- Berechne wieviele Sekunden vergenangen willst (Du kannst auch die Zeit in Sekunden und Minuten Berechnen)

**Tipp:** `input(..)` und ggf. `%` (Divisionsrest berechnen). Die aktuelle Zeit in Sekunden bekommst du so:

```
import time
aktuelle_zeit = time.time()
```

[Lösung](#code9){:.show_solution}
{% highlight python %}
{% include_relative code/stopuhr.py %}
{% endhighlight %}{: .hidden #code9 }

<hr>

## Schaltjahrrechner
- Schreibe ein Programm, dass errechnet, ob ein Jahr ein Schaltjahr ist
- Gib eine Jahreszahl ein, bestimme mit folgenden Bedingungen, ob es ein Schaltjahr ist:
  - Jahreszahl durch 400 teilbar: immer ein Schaltjahr
  - Durch 100 teilbar: Ist kein Schaltjahr
  - Falls durch 4 teilbar: Ist ein Schaltjahr

  Die Regel sind in der angegebenen Reihenfolge anzuwenden.

**Tipp:** `input(..)` und `if`

[Lösung](#code10){:.show_solution}
{% highlight python %}
{% include_relative code/Schaltjahr.py %}
{% endhighlight %}{: .hidden #code10 }

<hr>

## Einmaleins-Rechner

- Schreibe ein Programm das dich 1x1-Aufgaben abfragt.
- Lass den Benutzer den Zahlenraum festlegen.
- Stelle dem Benutzer eine zufällige 1x1-Aufgabe aus dem gewünschten Zahlenraum
- Fordere ihn auf das Ergebnis einzugeben
- Vergleiche das Ergebnis mit dem berechneten korrekten Ergebnis und gib aus, ob der Benutzer recht hat
- Frage den Benutzer ob er eine neue Aufgabe lösen will und stelle und wiederhole ab Schritt 3

**Tipp:** `input(..)`, `while` und `if`

[Lösung](#code11){:.show_solution}
{% highlight python %}
{% include_relative code/lerner_1x1.py %}
{% endhighlight %}{: .hidden #code11 }
