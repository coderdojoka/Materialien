{% capture filecontent %}
    {% include_relative {{ include.rel_file }} %}
{% endcapture %}

{% assign lines = filecontent | newline_to_br | split: '<br />' %}
