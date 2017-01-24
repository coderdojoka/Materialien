---
layout: page
title: Aufgaben Übersicht
permalink: python/aufgaben.html
---

{% assign data = site.python | where_exp:"item","item.type == 'exercise'" %}

{% for cats in site.data.python_exercises %}

{% assign items = data | where_exp:"item","item.folder == cats.name" %}
{% if items.size > 0 %}
## {{ cats.title }}
{% include dump_items.html data=items %}
{% endif %}
{% endfor %}
