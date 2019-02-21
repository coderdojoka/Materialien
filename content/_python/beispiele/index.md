---
layout: page
title: Beispiele
uid: python-beispiele
permalink: /python/beispiele/
---

{% assign data = site.python | where_exp:"item","item.type == 'example'" %}

{% for cats in site.data.python_examples %}

{% assign items = data | where_exp:"item","item.folder == cats.name" %}
{% if items.size > 0 %}
## {{ cats.title }}
{% include dump_items.html data=items %}
{% endif %}
{% endfor %}
