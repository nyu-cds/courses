---
layout: page
title: Exercises
---

<ul>
{% for page in site.pages %}
  {% if page.layout == 'exercise' %}
    <li><a href="{{ site.github.url }}{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
