---
layout: page
title: Aufgaben
uid:  python-aufgaben
permalink: python/aufgaben
---

Hier findest du Aufgaben rund um Python. Die Aufgaben sind farblich nach Schwierigkeit sortiert.
Wenn du eine Aufgabe gelöst hast, kannst du sie abhaken! Aber erst wenn du sie wirklich gelöst hast!

**Tipp:** Bearbeite die Aufgaben auf deinem Computer und speichere sie einzeln in verschiedenen Dateienen ab.
Du kannst sie dann einen Mentor zeigen und auf Korrektheit überprüfen lassen

{% assign data = site.python | where_exp:"item","item.layout == 'exercise'" %}
{% include color_items.html data=data %}
