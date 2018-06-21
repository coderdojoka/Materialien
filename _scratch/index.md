---
title: Scratch
author: Ricarda
date: 21.06.2018
permalink: scratch
layout: page
---

TODO: Scratch content


{% assign data = site.scratch | where_exp:"item","item.type == 'tutorial'" %}
{% assign tuts = data | where_exp:"item","item.folder == basics" %}

{% include dump_items.html data=data %}