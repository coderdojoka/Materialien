---
author: Mark
date: 2016-04-22  
layout: page
title: Befehlsübersicht
uid: py_ref
---

{% assign data = site.python | where_exp:"item","item.layout == 'referenz'" %}
{% assign items = data | where_exp:"item","item.topic == 'py_ref'" %}
{% include color_items.html no_tags=true data=items %}
