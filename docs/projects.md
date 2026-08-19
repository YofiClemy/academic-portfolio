---
layout: landing
title: Projects
permalink: /projects/
---

{% raw %}{% assign lang = page.lang | default: "en" %}
{% assign L = site.data.i18n[lang] | default: site.data.i18n.en %}{% endraw %}

<section class="controls">
  <input id="q" type="search" placeholder="{{ L.projects.search_placeholder }}" aria-label="Search projects… (title, subtitle, tag)">
  <div id="chips" class="chips">
    <button class="chip active" data-cat="all">{{ L.projects.category_all }}</button>
    <button class="chip" data-cat="measurements">{{ L.projects.category_measurements }}</button>
    <button class="chip" data-cat="electronics">{{ L.projects.category_electronics }}</button>
    <button class="chip" data-cat="logic">{{ L.projects.category_logic }}</button>
    <button class="chip" data-cat="power">{{ L.projects.category_power }}</button>
  </div>
</section>

<section class="grid" id="grid">
{% raw %}{% assign lang = page.lang | default: 'en' %}{% endraw %}
{% for p in site.data.projects %}
  {% raw %}{% assign title = p['title_' | append: lang] | default: p.title_en %}
  {% assign subtitle = p['subtitle_' | append: lang] | default: p.subtitle_en %}
  {% include card.html p=p lang=lang title=title subtitle=subtitle %}{% endraw %}
{% endfor %}
</section>
