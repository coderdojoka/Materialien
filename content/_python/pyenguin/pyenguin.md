---
title: pyenguin - Spiele und Zeichenbiblothek
layout: page
date: 2017-01-24
author: Mark
permalink: python/pyenguin.html
---
{% assign data = site.python | where_exp:"item","item.topic == 'pyenguin'" %}
{% assign exps = data | where_exp:"item","item.layout == 'example'" %}


Du willst Spiele in Python entwickeln? Dann bist du hier genau richtig!

![Ein kleines Spiel in pyenguin](blocks.png)

## Installation

Eine Anleitung findest unter {% include link_by_id.html uid="pg_install" %}.
 
## [Befehlsübersicht]({{ "python/pyenguin_referenz.html" | absolute_url }})
Eine Übersicht mit den wichtigsten pyenguin Befehlen kannst hier finden.

## Beispiele

{% include color_items.html data=exps %}