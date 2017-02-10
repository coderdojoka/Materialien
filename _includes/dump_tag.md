
{% assign hits = site.python | where_exp: "item","item.tags contains page.uid "%}

{% assign tuts = hits | where_exp: "item","item.layout=='tutorial'" %}
{% assign refs = hits | where_exp: "item","item.layout=='referenz'" %}
{% assign exs = hits | where_exp: "item","item.layout=='exercise'" %}
{% assign exps = hits | where_exp: "item","item.layout=='example'" %}

## Befehlsübersicht
{% if refs.size > 0 %}
{% include dump_items.html data=refs %}
{% else %}
<p>Keine Treffer</p>
{% endif %}

## Tutorials
{% if tuts.size > 0 %}
{% include dump_items.html data=tuts %}
{% else %}
<p>Keine Treffer</p>
{% endif %}

## Aufgaben
{% if exs.size > 0 %}
{% include dump_items.html data=exs %}
{% else %}
Keine Treffer
{% endif %}


## Beispiele
{% if exps.size > 0 %}
{% include dump_items.html data=exps %}
{% else %}
Keine Treffer
{% endif %}
