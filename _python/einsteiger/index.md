---
title: Übersicht
author: Mark
date: 17.06.2018
permalink: /python/einsteiger/
layout: page
---

{% assign exs = site.python | where_exp:"item","item.type == 'exercise'" %}
{% assign tuts = site.python | where_exp:"item","item.type == 'tutorial'"  %}
{% assign exps = site.python | where_exp:"item","item.type == 'example'" %}

{% assign exs = exs   |  where_exp:"item","item.level < 5" | sort: order   %}
{% assign tuts = tuts |  where_exp:"item","item.level < 5" | sort: order   %}
{% assign exps = exps |  where_exp:"item","item.level < 5" | sort: order   %}

# Python installieren

Unter {% include link_by_id.md uid="python_install" %} findest du eine Anleitung zur Installation von Python.

# Erste Schritte für komplette Neueinsteiger

Du programmierst zum ersten Mal mit Python? Dann ist {% include link_by_id.md uid="ersteschritte" %} genau das richtige für dich!

# Tutorials

{% include max_list.html data=tuts max=5 more="python-einsteiger-tutorials" %}

# Aufgaben

{% include max_list.html data=exs max=5 more="python-einsteiger-aufgaben" %}

# Beispiele

{% include max_list.html data=exps max=5 more="python-beispiele" %}
