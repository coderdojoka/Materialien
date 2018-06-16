{% assign limit = lines | size %}
{% assign offset = 0 %}
{% assign lang = "python" %}


{% if include.limit > 0 %}
{% assign limit = include.limit %}
{% endif %}

{% if include.offset %}
{% assign offset = include.offset  %}
{% endif %}

{% for line in include.lines offset:offset limit:limit %}{{ line }}{% endfor %}