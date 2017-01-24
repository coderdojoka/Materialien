---
layout: page
title: Beispiele - Grundlagen
filter_by: basics
collection_name: python
---


{% assign data = site.python | where_exp:"item","item.type == 'example'" %}
{% assign tuts = data | where_exp:"item","item.folder == page.filter_by" %}

{% include dump_items.html data=tuts %}
