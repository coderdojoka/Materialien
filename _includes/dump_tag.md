
{% assign hits = site.python | where_exp: "item","item.tags contains page.uid "%}

{% assign tuts = hits | where_exp: "item","item.type=='tutorial'" %}
{% assign exs = hits | where_exp: "item","item.type=='exercise'" %}
{% assign exps = hits | where_exp: "item","item.type=='example'" %}

# Tutorials
{% if tuts.size > 0 %}
{% include dump_items.html data=hits %}
{% else %}
<p>Keine Treffer</p>
{% endif %}

# Aufgaben
{% if exs.size > 0 %}
{% include dump_items.html data=exs %}
{% else %}
<p>Keine Treffer</p>
{% endif %}


# Beispiele
{% if exps.size > 0 %}
{% include dump_items.html data=exps %}
{% else %}
<p>Keine Treffer</p>
{% endif %}
