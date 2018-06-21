---
title: Erste Schritte
permalink: /python/fortgeschritten/
layout: page
date: 2018-06-15
author: Mark
---

{% assign tuts = site.python | where_exp:"item","item.group == 'fortgeschritten'" %}

{% include max_list.html data=tuts %}
