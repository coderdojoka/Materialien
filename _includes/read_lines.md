{% capture filecontent %}
    {% include {{ include.file }} %}
{% endcapture %}

{% assign lines = filecontent | newline_to_br | split: '<br />' %}
