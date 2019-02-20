---
minted_ausgabe: tmp_latex  
autor: Mark  
version: 1.0  
datum: 13.09  
title: Klassen II - Klassenvariablen und Vererbung 
layout: page
group: fortgeschritten
---

Klassen beschreiben den Aufbau eines Objektes aus dem beliebig viele Instanzen mit allen beschrieben Attributen erstellt werden können. Nun kann es sein, dass man verschiedene Arten von Objekten erstellen will, die unterschiedliche Eigenschaften haben aber auch viele Gemeinsamkeiten. Damit man hier nicht Dinge doppelt und dreifach schreiben muss, wird hier u.a. das Konzept der Vererbung vorgestellt.

# Statische Variablen (Klassenvariablen)

Wird eine Variable in der `__init()__`-Methode mit `self.farbe = farbe` angelegt, so ist dies eine Instanzvariable. Jede Instanz hat diese Variable und kann diese **unabhängig** von allen anderen Instanzen ändern.  

Eine Klassenvariable hingegen wird über alle Instanzen dieser Klasse geteilt. Wird diese Klassenvariable an einer Stelle geändert, so wird diese für **ALLE** instanzen geändert.

> Beispiel: In einem Teich schwimmen Fische, jeder Fisch hat ein Gewicht, je nach dem ist er dicker oder dünner wenn er mehr zu fressen bekommt. Wird die Wassertemparatur geändert, ändert sich derren Aktivitätsverhalten, so betrifft das alle Fische gleichermaßen.

Klassenvariablen werden außerhalb der `init()`-Methode, am besten oben direkt nach der Klassendefinition, angelegt:

```python
class Fisch:

  wasser_temparatur = 20

  def __init(self, gewicht):
    self.gewicht = gewicht
```

Will man eine Klassenvariable abfragen, so tut man dies nicht über eine Instanz-Variable. Stattdessen wird der Klassennamen verwendet. Dadurch ist sofort ersichtlich, dass es sich um eine Klassen-Variable handelt.

```python
fisch1 = Fisch(20)
fisch2 = Fisch(24)

# Instanzvariablen abfragen
print("Gewicht 1:", fisch1.gewicht) # Gewicht 1: 20
print("Gewicht 2:", fisch2.gewicht) # Gewicht 2: 24

# Die Klassenvariablen abfragen/setzen
print(Fisch.wasser_temparatur) # 20
Fisch.wasser_temparatur = 21
```

Klassenvariablen werden manchmal auch als statische Variablen bezeichnet. Hier noch ein weiteres Beispiel, wie man einen Zähler erstellt der Instanz-übergreifend zählt.

```python
class Zaehler:
  gemeinsamer_zaehler = 0

  def init(self):
    self.eigener_zaehler = 0

  def zaehle(self):  
    self.eigener_zaehler += 1
    Zaehler.gemeinsamer_zaehler += 1


z1 = Zaehler()
z2 = Zaehler()

z1.zaehle()
print(z1.eigener_zaehler, Zaehler.gemeinsamer_zaehler) # 1, 1

z2.zaehle()
print(z2.eigener_zaehler, Zaehler.gemeinsamer_zaehler) # 1, 2
```

# Vererbung

Wir wollen verschiedene geometrische Formen erstellen und derren Fläche und Umfang ausgeben. Jede Form hat eine andere Formel, wie die Fläche/Umfang zu berechnen ist. Hier bietet es sich an, von Vererbung Gebrauch zu machen. Klassen können von einander erben. D.h. sie bekommen alle Variablen und Funktionen ihrer Elternklasse zur Verfügung gestellt! Als Beispiel erstellen wir nun eine Elternklasse, die noch nicht so viel Funktionalität besitzt.

```python
class Form:

  def init(self):
    # hier passiert nichts
    pass

  def umfang(self):
    print("Nicht implementiert!")
    return 0

  def flaeche(self):
    print("Nicht implementiert!")
    return 0

  def info(self):
      print("Diese Figur hat eine Fläche von", self.flaeche(), "und einen Umfang von", self.umfang())
```

Diese Klasse ist lediglich eine Beschreibung einen abstrakten Form. Beim Programmieren muss man oft über 'abstrakte' Konzepte nachdeneken. Man weiß im Vorraus nicht, was die krrrekte Berechnungsvorschrift ist, um z.B. die Fläche auszurechnen. Stattdessen legt man eine Platzhalter-Methode an, die später ausgefüllt werden kann.

```python
class Kreis(Form): # Ich will von Form erben

  # Eine statische Variable
  PI = 3.1415926

  def init(self, radius):
    # WICHTIG: Das Eltern-__init__() aufrufen
    Form.__init__(self)

    # Eine Instanz-Variable anlegen
    self.radius = radius

  def umfang(self):
    return 2 * self.radius * Kreis.PI

  def flaeche(self):
    return self.radius * self.radius * Kreis.PI
```

Kreis erbt von Form, deshalb muss in der `__init__()`-Methode aud die `__init__()`-Methode
der Elternklasse aufgerufen werden mit allen nötigen Parameter. Parameter sind `self`,
und danach weitere Extraparameter, falls gefordert. Danach werden erneut die Funktionen
`umfang()` und `flaeche()` angelegt. Dies nennt man überschreiben. Es gibt diese beiden
Funktionen nun _zweimal_, einmal in der Eltern- und einmal in der Kindklasse.
Ruft man diese nun auf, so wird immer die Funktion aus der Kindklasse gewählt!

```python
class Rechteck(Form): # Ich will von Form erben

  def init(self, breite, hoehe):
    # WICHTIG: Das Eltern-__init__() aufrufen
    Form.__init__(self)

    self.breite = breite
    self.hoehe = hoehe

  def umfang(self):
    return 2 * (self.breite + self.hoehe)

  def flaeche(self):
    return self.breite * self.hoehe
```

Die `Rechteck`-Klasse wird analog zu `Kreis` angelegt, nur mit anderen Formeln.

Nun können wir verschiedene Formen erstellen und derren Werte berechnen lassen.

```python
rechteck = Rechteck(4, 3)
kreis = Kreis(1)

# Beide haben .info() von Form geerbt
rechteck.info() # ... 12 ... 14
kreis.info()# PI ... 2PI
```

Intern ruft `.info()` die überschriebenen Methoden für `umfang()` und `flaeche()` der jeweiligen Klassen auf!
In der Elternklasse ist bereits die komplette Logik für `.info()` hinterlegt, obwohl die Kindklassen noch gar nicht
programmiert waren!