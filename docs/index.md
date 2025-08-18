---
layout: landing
title: ""
---

<!-- Minimal header to avoid repetition -->
<div class="hero" style="max-width:1040px;margin:18px auto 6px;padding:0 16px;">
  <div class="hero__meta">Updated: {{ site.time | date: "%Y-%m-%d" }}</div>
</div>

<section class="controls">
  <input id="q" type="search" placeholder="Search projects… (title, subtitle, tag)" aria-label="Search projects">
  <div id="chips" class="chips">
    <button class="chip active" data-cat="all">All</button>
    <button class="chip" data-cat="measurements">Measurements</button>
    <button class="chip" data-cat="electronics">Electronics</button>
    <button class="chip" data-cat="logic">Logic</button>
    <button class="chip" data-cat="power">Power/Thermo</button>
  </div>
</section>

<section class="grid" id="grid">
{% for p in site.data.projects %}
  {% include card.html p=p %}
{% endfor %}
</section>
