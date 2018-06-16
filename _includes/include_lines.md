{% capture filecontent %}
    {% include_relative {{ include.file }} %}
{% endcapture %}

{% assign lines = filecontent | newline_to_br | split: '<br />' %}
{% assign limit = lines | size  %}
{% assign offset = 0  %}

{% if include.limit > 0 %}
{% assign limit = include.limit %}
{% endif %}

{% if include.offset %}
{% assign offset = include.offset  %}
{% endif %}

{% highlight python %}{% for line in lines offset:offset limit:limit %}{{ line }}{% endfor %}{% endhighlight %}