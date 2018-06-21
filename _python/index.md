---
title: Python
permalink: /python/
layout: page
---

{% assign exs = site.python | where_exp:"item","item.type == 'exercise'" %}
{% assign tuts = site.python | where_exp:"item","item.type == 'tutorial'" %}
{% assign exps = site.python | where_exp:"item","item.type == 'example'" %}

## Aufgaben, Tutorials und Beispiele

Hier findest du eine Reihe von Anleitungen und Beispielen, die nach Komplexität geordnet sind.

{% include thumb3.html img0="python_beginner.svg" link0="/python/einsteiger/" title0="Einsteiger" 
img1="python_intermediate.svg" link1="/python/fortgeschritten/" title1="Fortgeschritten"
img2="python_master.svg" link2="/python/meister/" title2="Meister" %}

Oder verwende die [Such-Funktion]({{ "/python/suche/" | relative_url }}), um alle vorhanden Anleitungen, Beispiele und Aufgaben zu durchsuchen!

-----

{% capture referenz %}
Hier findest du eine Übersicht über die wichtigsten Python Befehle und Konzepte. Wenn du z.B. herausfinden willst, welche Funktionen es für Listen gibt, wirst du hier fündig.
{% endcapture %}

{% capture projekte %}
Hier findest du eine Sammlung von Projekten, die im CoderDojo von Teilnehmern erstellt wurden. Lass dich inspierieren und finde heraus was man alles Tolles mit Python programmieren kann.
{% endcapture %}

{% capture links %}
Hier haben wir eine Liste mit hilfreichen Links zu externen Seiten rum ums Programmieren mit Python gesammelt, wie z.B:

* Eine sehr schöne, interaktive Seite zum Python lernen: [http://cscircles.cemc.uwaterloo.ca/de/](http://cscircles.cemc.uwaterloo.ca/de/)

* Python Online Dokumentation: [https://py-tutorial-de.readthedocs.io/de/python-3.3/](https://py-tutorial-de.readthedocs.io/de/python-3.3/)

{% endcapture %}

{% capture buttons %}
Verdiene dir für deine Lernfortschritte in Python diese coolen Buttons!
{% endcapture %}

{% include  img_n_text.html img="notebook.svg" title='Befehlsreferenz' link="python/referenz"  description=referenz  %}

{% include  img_n_text.html img="gears.svg" title='Eigene Projekte' link="python/projekte" class_extra="img-right"  description=projekte  %}

{% include  img_n_text.html img="folder.svg" title='Weiterführende Links' link="python/links" description=links  %}

{% include  img_n_text.html img="buttons/python_buttons.svg" title='Buttons' link="python/buttons" description=buttons  %}