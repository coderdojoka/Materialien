---
title: Eingaben einlesen
author: Mark  
uid: tut_input
layout: tutorial
group: ersteschritte
---

# Eingaben

Ein Program, in den der Benutzer nichts eingeben kann ist meinstens langweilig. Deswegen ist es praktisch, dass wir relativ einfach die Eingaben einlesen können.

Dies funktioniert mithilfe von `input()`.

{% include read_lines.md rel_file="code/eingabe.py" %}
{% highlight python %}{% include select_lines.md lines=lines offset=2 limit=2 %}{% endhighlight %}

Was in den Klammern bei `input()` steht wird zuerst auf der Konsole ausgeben, dann wird auf einen Eingabe des Benutzers gewartet.

**Wichtig:** das Programm wartet solange bis der Benutzer etwas auf der Konsole eingetippt und mit ’Enter’ bestätigt hat!

{% highlight python %}{% include select_lines.md lines=lines offset=2 limit=2 %}{% endhighlight %}

Wie in dem Tutorial zu Variablen schon erklärt wurde, ist `name` eine Variable.
Dieser Variable wird der Wert zugewiesen, den der Benutzer eintippt und
mittels `input()` gelesen wird.

## Zahlen einlesen

Mittles `input()` kann nur Text eingelesen werden! Auch wenn der Benutzer `12` 
eintippt, so wird dies als Text `"12"` interpretiert. Wir können mit Text
allerdings nicht rechnen. Aus diesem Grund müssen wir den eingelesenen
Text mithilfe von `int(...)` in eine ganze Zahl konvertieren.

{% highlight python %}{% include select_lines.md lines=lines offset=5 limit=2 %}{% endhighlight %}

Hier wird nun zuerst das Alter als Text eingelesen und dann in eine Zahl
umgewandelt. Die Variable `alter` enthält zunächst also einen Text. Danach
wird deren Wert überschrieben mit der Zahl, die dieser Text darstellt.

## Aufgaben

- Lies deinen Namen von der Konsole ein und gib diesen aus.
- Was passiert, wenn du einen Text in eine Zahl umwandelst und der Text ist keine Zahl?
- Lies dein Alter ein und berechne wie viele Monate du ungefähr alt bist