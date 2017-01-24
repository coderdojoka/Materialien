---
title: Python - Tutorials und Aufgaben
permalink: python/
layout: page
---


{% assign allowed = ['example', 'exercise'] %}
{% assign exs = site.python | where_exp:"item","item.type == 'exercise'" %}
{% assign tuts = site.python | where_exp:"item","item.type == 'tutorial'" %}
{% assign exps = site.python | where_exp:"item","item.type == 'example'" %}


## [Tutorials]({{ "/python/tutorials.html" | absolute_url }})

{% include max_list.html data=tuts max=3 %}
Alle Tutorials findest du [hier]({{ "/python/tutorials.html" | absolute_url }})

## [Aufgaben]({{ "/python/aufgaben.html" | absolute_url }})

{% include max_list.html data=exs max=3 %}
Alle Aufgaben findest du [hier]({{ "/python/aufgaben.html" | absolute_url }})

## [Beispiele]({{ "/python/beispiele.html" | absolute_url }})

{% include max_list.html data=exps max=3 %}
Alle Beispiele findest du [hier]({{ "/python/beispiele.html" | absolute_url }})

## [Pyenguin]({{ "/python/pyenguin.html" | absolute_url }})
Ein Framework um Spiele und grafische Oberflächen in Python zu entwickeln.

## Nützliche Links

* Eine sehr schöne interaktive Seite zum Python lernen: [http://cscircles.cemc.uwaterloo.ca/de/](http://cscircles.cemc.uwaterloo.ca/de/)

* Python Online Dokumentation: [https://py-tutorial-de.readthedocs.io/de/python-3.3/](https://py-tutorial-de.readthedocs.io/de/python-3.3/)