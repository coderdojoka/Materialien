---
layout: page
title: Container
permalink: demos/container
---

{% capture content %}

## Überschrift

Hier steht Fließtext. Zeilenümbrüche werden ignoriert,
außer die vorherige Zeile endet mit  
zwei Leerzeichen!
{% endcapture %}

{% capture left %}
![Test Bild](/_assets/imgs/arduino.png)
{% endcapture %}

{% include split.html left=left right=content %}