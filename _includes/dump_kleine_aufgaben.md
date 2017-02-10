{% assign coll = site.collections | where_exp:"item","item.label==page.collection" | first %}
{% assign items = coll.docs | where_exp: "item","item.folder==page.uid" %}
{% for item in items %}
## [{{ item.title }}]( {{ item.url }}) 
{{ item.content }}
{% if forloop.last == false %}
  <hr>
{% endif %}
{% endfor %}
