---
title: Einsteiger Aufgaben
permalink: /python/einsteiger/aufgaben/
uid: python-einsteiger-aufgaben
layout: page
---

{% assign exs = site.python | where_exp:"item","item.type == 'exercise'" %}
{% assign exs = exs   |  where_exp:"item","item.level < 5" | sort: order   %}

# Aufgaben

{% include dump_items.html data=exs %}
