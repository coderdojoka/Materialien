---
title: Scratch
author: Ricarda
date: 21.06.2018
uid: scratch
permalink: /scratch/
layout: page
---

{% assign data = site.scratch | where_exp:"item","item.type == 'tutorial'" %}
{% assign tuts = data | where_exp:"item","item.folder == python-grundlagen" %}

{% include dump_items.html data=data %}


TODO: Mehr Scratch Inhalte