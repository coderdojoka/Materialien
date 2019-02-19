---
title: Einsteiger Tutorials
permalink: /python/einsteiger/tutorials/
uid: python-einsteiger-tutorials
layout: page
---

{% assign exs = site.python | where_exp:"item","item.type == 'tutorial'" %}
{% assign exs = exs   |  where_exp:"item","item.level < 5" | sort: order   %}

# Aufgaben

{% include dump_items.html data=exs %}
