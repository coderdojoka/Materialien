---
layout: page
title: Tutorial-Übersicht
permalink: python/tutorials.html
---

{% assign data = site.python | where_exp:"item","item.type == 'tutorial'" %}

{% for cats in site.data.python_tut_cats %}

{% assign items = data | where_exp:"item","item.folder == cats.name" %}
{% if items.size > 0 %}
## {{ cats.title }}
{% include dump_items.html data=items %}
{% endif %}
{% endfor %}
