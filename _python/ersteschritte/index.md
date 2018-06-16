---
title: Erste Schritte
permalink: /python/ersteschritte
layout: page
date: 2018-06-15
author: Mark
---


{% assign tuts = site.python | where_exp:"item","item.parent == 'ersteschritte'" %}

{% include max_list.html data=tuts max=3 %}
