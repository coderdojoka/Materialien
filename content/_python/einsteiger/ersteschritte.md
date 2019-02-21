---
title: Erste Schritte
permalink: /python/ersteschritte/
layout: page
uid: ersteschritte
date: 2018-06-15
author: Mark
---


Tutorials:

{% assign tuts = site.python | where_exp:"item","item.group == 'ersteschritte'" %}

{% include max_list.html data=tuts max=3 more="python-einsteiger-tutorials" %}
