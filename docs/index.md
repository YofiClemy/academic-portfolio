---
layout: landing
title: ""
---

<section class="portfolio-hero">
  <div class="portfolio-hero__inner">

    <div class="hero__eyebrow">
      Electrical Engineering · Power Systems · Automation
    </div>

    <h1>Clément Chevauchey</h1>

    <h2>
      Electrical Engineering Student focusing on
      <span>Power Systems & Industrial Automation</span>
    </h2>

    <p class="hero__intro">
      Building practical experience in power-system studies, electrical
      engineering and automation, with particular interest in load-flow and
      short-circuit analysis, protection, PLCs and SCADA.
    </p>

    <div class="hero__actions">
      <a href="#projects" class="btn btn--primary">
        View Projects
      </a>

      <a href="#cv" class="btn btn--secondary">
        View CV
      </a>

      <a href="https://github.com/YofiClemy"
         class="btn btn--ghost"
         target="_blank"
         rel="noopener">
        GitHub ↗
      </a>
    </div>

    <div class="hero__availability">
      <span class="status-dot"></span>
      Looking for 2026–27 internships and entry-level opportunities
      in France, Europe, Argentina or remote.
    </div>

  </div>
</section>

<!-- =========================
     ABOUT
========================= -->

<section class="portfolio-section" id="about">

  <div class="section-heading">
    <span class="section-kicker">Profile</span>
    <h2>Engineering with a practical focus.</h2>
  </div>

  <div class="about-grid">

    <div class="about-grid__main">
      <p>
        I am an Electrical Engineering student developing a specialization
        around electrical networks, power-system analysis and industrial
        automation.
      </p>

      <p>
        My academic and personal projects combine electrical engineering
        fundamentals with simulation, measurement and programming. I am
        particularly interested in applying tools such as DIgSILENT
        PowerFactory and Python to real engineering problems.
      </p>
    </div>

    <div class="about-grid__aside">

      <div>
        <span>Currently</span>
        <strong>Electrical Engineering Student</strong>
      </div>

      <div>
        <span>Target roles</span>
        <strong>Power Systems · Automation</strong>
      </div>

      <div>
        <span>Mobility</span>
        <strong>France · EU · Argentina · Remote</strong>
      </div>

    </div>

  </div>

</section>

<!-- =========================
     PROJECTS
========================= -->

<section class="portfolio-section" id="projects">

  <div class="section-heading section-heading--split">

    <div>
      <span class="section-kicker">Portfolio</span>
      <h2>Engineering projects.</h2>
      <p>
        Academic and personal work covering electrical systems,
        electronics, measurement and automation.
      </p>
    </div>

    <span class="project-count">
      {{ site.data.projects | size }} projects
    </span>

  </div>


  <!-- Project browser -->

  <div class="project-controls">

    <input
      id="q"
      type="search"
      placeholder="Search projects…"
      aria-label="Search projects"
    >

    <div id="chips" class="chips">
      <button class="chip active" data-cat="all">All</button>
      <button class="chip" data-cat="power">Power Systems</button>
      <button class="chip" data-cat="electronics">Electronics</button>
      <button class="chip" data-cat="measurements">Measurements</button>
      <button class="chip" data-cat="logic">Automation / Logic</button>
    </div>

  </div>


  <div class="grid" id="grid">

    {% for p in site.data.projects %}
      {% include card.html p=p %}
    {% endfor %}

  </div>

</section>


<!-- =========================
     EDUCATION
========================= -->

<section class="portfolio-section" id="education">

  <div class="section-heading">
    <span class="section-kicker">Background</span>
    <h2>Education & experience.</h2>
  </div>

  <div class="timeline">

    <article class="timeline-item">

      <div class="timeline-item__date">
        Current
      </div>

      <div class="timeline-item__content">
        <h3>Electrical Engineering</h3>
        <p class="timeline-item__meta">
          Universidad Nacional de Santiago del Estero
        </p>

        <p>
          Engineering curriculum covering electrical circuits,
          electromagnetics, electrical machines, electronics,
          mathematics, physics and power-related systems.
        </p>
      </div>

    </article>


    <article class="timeline-item">

      <div class="timeline-item__date">
        2022–2025
      </div>

      <div class="timeline-item__content">
        <h3>University Teaching Assistant</h3>

        <p>
          Supported university students in computing and engineering-related
          coursework including Excel, programming fundamentals and Scilab.
        </p>
      </div>

    </article>


    <article class="timeline-item">

      <div class="timeline-item__date">
        Current
      </div>

      <div class="timeline-item__content">
        <h3>IEEE Member</h3>

        <p>
          Member of the IEEE Power & Energy Society and Industry
          Applications Society.
        </p>
      </div>

    </article>

  </div>

</section>


<!-- =========================
     CV
========================= -->

<section class="portfolio-section cv-section" id="cv">

  <div class="cv-box">

    <div>
      <span class="section-kicker">Curriculum Vitae</span>

      <h2>Want the conventional version?</h2>

      <p>
        View or download my CV in English or Spanish.
      </p>
    </div>


    <div class="cv-actions">

      {% assign cv_en = '/assets/CV English.pdf' | relative_url %}
      {% assign cv_es = '/assets/CV spanish.pdf' | relative_url %}

      <a
        href="{{ cv_en }}"
        target="_blank"
        class="btn btn--primary">
        English CV
      </a>

      <a
        href="{{ cv_es }}"
        target="_blank"
        class="btn btn--secondary">
        CV en Español
      </a>

    </div>

  </div>

</section>


<!-- =========================
     CONTACT
========================= -->

<section class="portfolio-section contact-section" id="contact">

  <span class="section-kicker">Contact</span>

  <h2>Interested in working together?</h2>

  <p>
    I am open to internships, graduate opportunities and engineering
    projects related to power systems, electrical engineering and automation.
  </p>

  <div class="hero__actions">

    <a
      href="mailto:"
      class="btn btn--primary">
      Email me
    </a>

    <a
      href=""
      target="_blank"
      rel="noopener"
      class="btn btn--secondary">
      LinkedIn ↗
    </a>

    <a
      href=""
      target="_blank"
      rel="noopener"
      class="btn btn--ghost">
      GitHub ↗
    </a>

  </div>

</section>