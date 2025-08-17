---
layout: home
title: Clement — Engineering Portfolio
---

<link rel="stylesheet" href="{{ '/assets/css/projects.css' | relative_url }}">

<div class="small">Updated: 2025-08-17</div>

<div class="filter" id="filter">
  <button class="chip active" data-cat="all">All</button>
  <button class="chip" data-cat="measurements">Measurements</button>
  <button class="chip" data-cat="electronics">Electronics</button>
  <button class="chip" data-cat="logic">Logic</button>
  <button class="chip" data-cat="power">Power/Thermo</button>
</div>

<div class="projects-grid" id="grid">
{% for p in site.data.projects %}
  <article class="card" data-cat="{{ p.category }}">
    <div class="thumb">
      {% if p.thumb and p.thumb != '' %}
        <img src="{{ p.thumb | relative_url }}" alt="thumb">
      {% else %}
        <div style="color:#6e7781;font-weight:700">{{ p.category | upcase }}</div>
      {% endif %}
    </div>
    <div class="body">
      <h3>{{ p.title }}</h3>
      <p>{{ p.subtitle }}</p>
      <div class="actions">
        <a class="btn" href="{{ site.repo_url_base }}{% if p.path %}/{{ p.path }}{% endif %}" target="_blank">Repo</a>
        {% if p.report and p.report != '' %}
          <a class="btn primary" href="{{ p.report | relative_url }}" target="_blank">Report</a>
        {% endif %}
      </div>
    </div>
  </article>
{% endfor %}
</div>

<script>
(function(){
  const chips=[...document.querySelectorAll('.chip')];
  const cards=[...document.querySelectorAll('.card')];
  chips.forEach(c=>c.addEventListener('click',()=>{
    chips.forEach(x=>x.classList.remove('active'));
    c.classList.add('active');
    const cat=c.dataset.cat;
    cards.forEach(card=>{
      card.style.display = (cat==='all' || card.dataset.cat===cat) ? '' : 'none';
    });
  }));
})();
</script>
