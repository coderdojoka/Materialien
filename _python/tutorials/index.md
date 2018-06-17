---
layout: page
title: Tutorial-Übersicht
permalink: python/tutorials.html
---


{% assign data = site.python | where_exp:"item","item.type == 'tutorial'" %}
{% assign tuts = data | where_exp:"item","item.folder == basics" %}

{% include dump_items.html data=tuts %}



{% assign data = site.python | where_exp:"item","item.layout == 'tutorial'" %}

{% for cats in site.data.python_tut_cats %}

{% assign items = data | where_exp:"item","item.topic == cats.name" %}
{% if items.size > 0 %}
## {{ cats.title }}

{% include color_items.html no_tags=true data=items %}

{% endif %}
{% endfor %}
