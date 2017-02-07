---
layout: page
title: Aufgaben Übersicht
uid:  python_aufg
permalink: python/aufgaben.html
---

{% assign data = site.python | where_exp:"item","item.layout == 'exercise'" %}
{% include color_items.html data=data %}
