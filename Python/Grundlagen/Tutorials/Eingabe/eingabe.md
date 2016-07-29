---
titel: Eingaben einlesen
autor: Mark  
---

Eingaben
========

Ein Program, in den der Benutzer nichts eingeben kann ist meinstens
langweilig. Deswegen ist es praktisch, dass wir relativ einfach die
Eingaben einlesen können.

Dies funktioniert mithilfe von `input()`.

```{.python firstline=1 lastline=2 include="../../../Beispiele/eingabe.py"}
bubber
```

Was in den Klammern bei `input()` steht wird zuerst auf der Konsole ausgeben, dann
wird auf einen Eingabe des Benutzers gewartet.\
**Wichtig:** das Programm wartet solange bis der Benutzer etwas auf der
Konsole eingetippt und mit ’Enter’ bestätigt hat!

```{.python firstline=2 lastline=2 include="../../../Beispiele/eingabe.py"}
bubber
```

Wie in dem Tutorial zu Variablen schon erklärt wurde, ist `name` eine Variable.
Dieser Variable wird der Wert zugewiesen, den der Benutzer eintippt und
mittels `input()` gelesen wird.

Zahlen einlesen
===============

Mittles `input()` kann nur Text eingelesen werden! Auch wenn der Benutzer `12` 
eintippt, so wird dies als Text `"12"` interpretiert. Wir können mit Text
allerdings nicht rechnen. Aus diesem Grund müssen wir den eingelesenen
Text mithilfe von `int(...)` in eine ganze Zahl konvertieren.

```{.python firstline=4 lastline=5 include="../../../Beispiele/eingabe.py"}
bubber
```

Hier wird nun zuerst das Alter als Text eingelesen und dann in eine Zahl
umgewandelt. Die Variable `alter` enthält zunächst also einen Text und danach
die Zahl, die dieser Text darstellt.

Aufgaben
========

-   Lies deinen Namen von der Konsole ein und gib diesen aus.

-   Was passiert, wenn du einen Text in eine Zahl umwandelst und der
    Text ist keine Zahl?

-   Lies dein Alter ein und berechne wie viele Monate du ungefähr alt
    bist


