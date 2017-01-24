---
layout: page
title: Tutorials - Einsteiger
filter_by: basics
---

{% assign data = site.python | where_exp:"item","item.type == 'tutorial'" %}
{% assign tuts = data | where_exp:"item","item.folder == page.filter_by" %}

{% include dump_items.html data=tuts %}
