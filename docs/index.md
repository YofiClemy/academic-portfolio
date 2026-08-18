---
layout: landing
title: ""
---

<style>
/* =========================================================
   PORTFOLIO LANDING PAGE
========================================================= */

:root {
  --pf-bg: #f5f7fb;
  --pf-surface: #ffffff;
  --pf-surface-soft: #eef3f9;

  --pf-navy: #071626;
  --pf-navy-2: #0b2036;
  --pf-blue: #1464f4;
  --pf-cyan: #37c5e8;

  --pf-text: #102033;
  --pf-muted: #627083;
  --pf-border: #dce4ed;

  --pf-radius-sm: 12px;
  --pf-radius: 20px;
  --pf-radius-lg: 30px;

  --pf-shadow:
    0 18px 50px rgba(16, 32, 51, 0.08);

  --pf-shadow-hover:
    0 24px 60px rgba(16, 32, 51, 0.14);
}


/* Make the theme wrapper much less restrictive */
.page-content > .wrapper {
  max-width: 1240px !important;
  padding-left: 28px !important;
  padding-right: 28px !important;
}

.page-content {
  background:
    radial-gradient(circle at 10% 0%, rgba(20,100,244,.05), transparent 32rem),
    var(--pf-bg);
}

.portfolio-page {
  color: var(--pf-text);
  padding: 24px 0 80px;
}

.portfolio-page * {
  box-sizing: border-box;
}


/* =========================================================
   TYPOGRAPHY
========================================================= */

.portfolio-page h1,
.portfolio-page h2,
.portfolio-page h3,
.portfolio-page p {
  margin-top: 0;
}

.portfolio-page h1,
.portfolio-page h2,
.portfolio-page h3 {
  color: var(--pf-text);
  letter-spacing: -0.035em;
}

.portfolio-page p {
  color: var(--pf-muted);
  line-height: 1.72;
}

.section-kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;

  margin-bottom: 10px;

  color: var(--pf-blue);
  font-size: 0.76rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .14em;
}

.section-kicker::before {
  content: "";
  width: 20px;
  height: 2px;
  border-radius: 99px;
  background: var(--pf-blue);
}


/* =========================================================
   HERO
========================================================= */

.portfolio-hero {
  position: relative;
  overflow: hidden;

  min-height: 610px;

  padding: clamp(44px, 7vw, 86px);

  border-radius: 34px;

  background:
    radial-gradient(
      circle at 84% 18%,
      rgba(55, 197, 232, .22),
      transparent 26rem
    ),
    radial-gradient(
      circle at 22% 110%,
      rgba(20, 100, 244, .28),
      transparent 34rem
    ),
    linear-gradient(
      135deg,
      #06131f 0%,
      #09233d 65%,
      #0b2d4c 100%
    );

  box-shadow:
    0 30px 80px rgba(7, 22, 38, .20);
}

.portfolio-hero::before {
  content: "";

  position: absolute;
  inset: 0;

  opacity: .16;

  background-image:
    linear-gradient(rgba(255,255,255,.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.08) 1px, transparent 1px);

  background-size: 44px 44px;

  mask-image:
    linear-gradient(to right, transparent, black 45%);
}

.portfolio-hero::after {
  content: "";

  position: absolute;
  right: -150px;
  top: -120px;

  width: 470px;
  height: 470px;

  border: 1px solid rgba(255,255,255,.13);
  border-radius: 50%;

  box-shadow:
    0 0 0 80px rgba(255,255,255,.025),
    0 0 0 160px rgba(255,255,255,.018);
}

.portfolio-hero__inner {
  position: relative;
  z-index: 2;

  display: grid;
  grid-template-columns: minmax(0, 1.6fr) minmax(270px, .65fr);
  gap: clamp(42px, 7vw, 90px);

  align-items: center;
}

.hero__eyebrow {
  display: inline-flex;
  align-items: center;

  padding: 8px 13px;
  margin-bottom: 24px;

  border: 1px solid rgba(255,255,255,.15);
  border-radius: 999px;

  background: rgba(255,255,255,.06);

  color: #a9bdd2;

  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.portfolio-hero h1 {
  max-width: 830px;

  margin-bottom: 14px;

  color: white;

  font-size: clamp(3.2rem, 7vw, 6.2rem);
  line-height: .94;
  font-weight: 820;
  letter-spacing: -.065em;
}

.portfolio-hero h2 {
  max-width: 740px;

  margin-bottom: 24px;

  color: #b8c8d8;

  font-size: clamp(1.35rem, 2.7vw, 2.1rem);
  line-height: 1.25;
  font-weight: 520;
  letter-spacing: -.035em;
}

.portfolio-hero h2 span {
  color: #ffffff;
}

.hero__intro {
  max-width: 690px;

  margin-bottom: 32px !important;

  color: #aebfd0 !important;

  font-size: 1.05rem;
  line-height: 1.75 !important;
}

.hero__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 11px;
}


/* =========================================================
   BUTTONS
========================================================= */

.portfolio-page .btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 7px;

  min-height: 44px;

  padding: 10px 17px;

  border: 1px solid transparent;
  border-radius: 11px;

  font-size: .9rem;
  font-weight: 720;

  text-decoration: none !important;

  cursor: pointer;

  transition:
    transform .18s ease,
    background .18s ease,
    border-color .18s ease,
    box-shadow .18s ease;
}

.portfolio-page .btn:hover {
  transform: translateY(-2px);
}

.btn--primary,
.portfolio-page .card .btn.primary {
  color: #fff !important;
  background: var(--pf-blue);
  border-color: var(--pf-blue);
}

.btn--primary:hover,
.portfolio-page .card .btn.primary:hover {
  background: #0758dd;
  box-shadow: 0 10px 25px rgba(20,100,244,.25);
}

.btn--secondary {
  color: var(--pf-navy) !important;
  background: white;
}

.btn--ghost {
  color: #d5e0eb !important;

  border-color: rgba(255,255,255,.18) !important;

  background: rgba(255,255,255,.055);
  backdrop-filter: blur(10px);
}

.btn--ghost:hover {
  background: rgba(255,255,255,.11);
}


/* =========================================================
   HERO SIDE PANEL
========================================================= */

.hero-panel {
  padding: 24px;

  border: 1px solid rgba(255,255,255,.13);
  border-radius: 22px;

  background: rgba(255,255,255,.055);
  backdrop-filter: blur(16px);
}

.hero-panel__label {
  margin-bottom: 18px;

  color: #7595b1;

  font-size: .72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .13em;
}

.hero-panel__item {
  padding: 16px 0;

  border-bottom: 1px solid rgba(255,255,255,.09);
}

.hero-panel__item:first-of-type {
  padding-top: 0;
}

.hero-panel__item:last-child {
  padding-bottom: 0;
  border-bottom: 0;
}

.hero-panel__item span {
  display: block;

  margin-bottom: 4px;

  color: #728fa8;

  font-size: .72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .08em;
}

.hero-panel__item strong {
  display: block;

  color: #edf5fb;

  font-size: .97rem;
  line-height: 1.45;
}


/* Availability */

.hero__availability {
  display: flex;
  align-items: center;
  gap: 10px;

  margin-top: 27px;

  color: #9eb2c4;

  font-size: .86rem;
}

.status-dot {
  position: relative;

  width: 9px;
  height: 9px;

  flex: 0 0 auto;

  border-radius: 50%;

  background: #49d797;
}

.status-dot::after {
  content: "";

  position: absolute;
  inset: -4px;

  border: 1px solid rgba(73, 215, 151, .45);
  border-radius: 50%;
}


/* =========================================================
   SECTIONS
========================================================= */

.portfolio-section {
  padding: 96px 10px 0;
}

.section-heading {
  max-width: 760px;

  margin-bottom: 38px;
}

.section-heading h2 {
  margin-bottom: 12px;

  font-size: clamp(2rem, 4vw, 3rem);
  line-height: 1.08;
}

.section-heading p {
  max-width: 650px;

  margin-bottom: 0;

  font-size: 1rem;
}

.section-heading--split {
  max-width: none;

  display: flex;
  justify-content: space-between;
  gap: 32px;
  align-items: flex-end;
}

.project-count {
  white-space: nowrap;

  padding: 8px 12px;

  border: 1px solid var(--pf-border);
  border-radius: 999px;

  background: var(--pf-surface);

  color: var(--pf-muted);

  font-size: .82rem;
  font-weight: 700;
}


/* =========================================================
   ABOUT
========================================================= */

.about-layout {
  display: grid;
  grid-template-columns: 1.15fr .85fr;
  gap: 24px;
}

.about-card,
.focus-card {
  border: 1px solid var(--pf-border);
  border-radius: var(--pf-radius-lg);

  background: var(--pf-surface);

  box-shadow: var(--pf-shadow);
}

.about-card {
  padding: clamp(28px, 4vw, 48px);
}

.about-card p {
  max-width: 730px;

  font-size: 1.02rem;
}

.about-card p:last-child {
  margin-bottom: 0;
}

.focus-card {
  padding: 30px;
}

.focus-card__title {
  margin-bottom: 20px;

  color: var(--pf-muted);

  font-size: .78rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .11em;
}

.focus-list {
  display: grid;
  gap: 10px;
}

.focus-item {
  display: flex;
  align-items: center;
  gap: 14px;

  padding: 14px;

  border: 1px solid var(--pf-border);
  border-radius: 13px;

  background: #fbfcfe;
}

.focus-icon {
  display: grid;
  place-items: center;

  width: 38px;
  height: 38px;

  flex: 0 0 auto;

  border-radius: 10px;

  color: var(--pf-blue);
  background: rgba(20,100,244,.08);

  font-size: 1.05rem;
  font-weight: 800;
}

.focus-item strong {
  display: block;

  margin-bottom: 2px;

  font-size: .92rem;
}

.focus-item span {
  color: var(--pf-muted);
  font-size: .8rem;
}


/* =========================================================
   PROJECT CONTROLS
========================================================= */

.project-controls {
  display: flex;
  gap: 14px;
  align-items: center;

  margin-bottom: 30px;
}

#q {
  width: min(100%, 340px);
  height: 48px;

  padding: 0 16px;

  border: 1px solid var(--pf-border);
  border-radius: 13px;

  outline: none;

  background: var(--pf-surface);
  color: var(--pf-text);

  font: inherit;

  box-shadow:
    0 5px 20px rgba(16,32,51,.03);

  transition:
    border-color .15s ease,
    box-shadow .15s ease;
}

#q:focus {
  border-color: rgba(20,100,244,.6);

  box-shadow:
    0 0 0 4px rgba(20,100,244,.08);
}

#q::placeholder {
  color: #98a4b1;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.chip {
  min-height: 40px;

  padding: 8px 13px;

  border: 1px solid var(--pf-border);
  border-radius: 999px;

  background: var(--pf-surface);
  color: #536174;

  font: inherit;
  font-size: .81rem;
  font-weight: 700;

  cursor: pointer;

  transition:
    background .15s ease,
    border-color .15s ease,
    color .15s ease,
    transform .15s ease;
}

.chip:hover {
  transform: translateY(-1px);

  border-color: #a9b9ca;
}

.chip.active {
  border-color: var(--pf-navy);
  background: var(--pf-navy);
  color: #fff;
}


/* =========================================================
   PROJECT CARDS
========================================================= */

.portfolio-page .grid {
  display: grid;

  grid-template-columns:
    repeat(3, minmax(0, 1fr));

  gap: 22px;
}

.portfolio-page .card {
  overflow: hidden;

  display: flex;
  flex-direction: column;

  min-width: 0;

  border: 1px solid var(--pf-border);
  border-radius: 20px;

  background: var(--pf-surface);

  box-shadow:
    0 8px 30px rgba(16,32,51,.045);

  transition:
    transform .22s ease,
    box-shadow .22s ease,
    border-color .22s ease;
}

.portfolio-page .card:hover {
  transform: translateY(-5px);

  border-color: #c5d3e1;

  box-shadow: var(--pf-shadow-hover);
}

.portfolio-page .card__thumb {
  position: relative;
  overflow: hidden;

  aspect-ratio: 16 / 9;

  background:
    linear-gradient(135deg, #e7edf5, #f5f8fb);
}

.portfolio-page .card__thumb img {
  width: 100%;
  height: 100%;

  display: block;

  object-fit: cover;

  transition: transform .35s ease;
}

.portfolio-page .card:hover .card__thumb img {
  transform: scale(1.025);
}

.portfolio-page .card__thumb--empty {
  background:
    radial-gradient(circle at 20% 10%, rgba(55,197,232,.22), transparent 40%),
    linear-gradient(135deg, #0c223a, #12466c);
}

.portfolio-page .card__tags {
  position: absolute;

  left: 12px;
  right: 12px;
  bottom: 12px;

  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.portfolio-page .tag {
  padding: 5px 8px;

  border: 1px solid rgba(255,255,255,.22);
  border-radius: 999px;

  background: rgba(4,17,29,.73);
  backdrop-filter: blur(8px);

  color: #f2f7fb;

  font-size: .66rem;
  font-weight: 720;
  line-height: 1;
}

.portfolio-page .tag--cat {
  background: var(--pf-blue);
  border-color: var(--pf-blue);
}

.portfolio-page .card__body {
  display: flex;
  flex: 1;
  flex-direction: column;

  padding: 22px;
}

.portfolio-page .card__title {
  margin-bottom: 7px;

  font-size: 1.15rem;
  line-height: 1.28;
}

.portfolio-page .card__subtitle {
  margin-bottom: 16px;

  color: var(--pf-muted);

  font-size: .88rem;
  line-height: 1.55;
}

.portfolio-page .card__meta {
  margin-top: auto;
  margin-bottom: 18px;

  padding-top: 15px;

  border-top: 1px solid #edf1f5;

  color: #768294;

  font-size: .77rem;
  line-height: 1.55;
}

.portfolio-page .card__meta strong {
  color: #4c5968;
}

.portfolio-page .card__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.portfolio-page .card__actions .btn {
  min-height: 35px;

  padding: 7px 10px;

  border: 1px solid var(--pf-border);

  background: #f8fafc;
  color: #435268 !important;

  font-size: .73rem;
}

.portfolio-page .card__actions .btn:hover {
  border-color: #b9c7d5;

  background: #f2f6fa;
}


/* =========================================================
   EXPERIENCE / EDUCATION
========================================================= */

.timeline {
  overflow: hidden;

  border: 1px solid var(--pf-border);
  border-radius: var(--pf-radius-lg);

  background: var(--pf-surface);

  box-shadow: var(--pf-shadow);
}

.timeline-item {
  display: grid;

  grid-template-columns: 150px 1fr;

  gap: 30px;

  padding: 32px 36px;

  border-bottom: 1px solid var(--pf-border);
}

.timeline-item:last-child {
  border-bottom: 0;
}

.timeline-item__date {
  color: var(--pf-blue);

  font-size: .81rem;
  font-weight: 800;
}

.timeline-item__content h3 {
  margin-bottom: 4px;

  font-size: 1.12rem;
}

.timeline-item__meta {
  margin-bottom: 10px !important;

  color: #43546a !important;

  font-size: .87rem;
  font-weight: 650;
}

.timeline-item__content > p:last-child {
  max-width: 730px;

  margin-bottom: 0;

  font-size: .9rem;
}


/* =========================================================
   CV
========================================================= */

.cv-box {
  position: relative;
  overflow: hidden;

  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 36px;

  padding: clamp(32px, 5vw, 56px);

  border-radius: var(--pf-radius-lg);

  background:
    radial-gradient(
      circle at 92% 0%,
      rgba(55,197,232,.22),
      transparent 22rem
    ),
    linear-gradient(
      135deg,
      #071626,
      #0b2945
    );

  box-shadow:
    0 25px 65px rgba(7,22,38,.17);
}

.cv-box::after {
  content: "CV";

  position: absolute;
  right: 30px;
  bottom: -58px;

  color: rgba(255,255,255,.035);

  font-size: 11rem;
  font-weight: 900;
  letter-spacing: -.08em;
}

.cv-box > * {
  position: relative;
  z-index: 2;
}

.cv-box .section-kicker {
  color: #6fd7ef;
}

.cv-box .section-kicker::before {
  background: #6fd7ef;
}

.cv-box h2 {
  margin-bottom: 9px;

  color: white;

  font-size: clamp(1.8rem, 4vw, 2.7rem);
}

.cv-box p {
  margin-bottom: 0;

  color: #aebfd0;

  font-size: .95rem;
}

.cv-actions {
  display: flex;
  gap: 9px;
  flex-wrap: wrap;
}


/* =========================================================
   CONTACT
========================================================= */

.contact-card {
  text-align: center;

  padding: 70px 32px;

  border: 1px solid var(--pf-border);
  border-radius: var(--pf-radius-lg);

  background: var(--pf-surface);
}

.contact-card .section-kicker {
  justify-content: center;
}

.contact-card h2 {
  max-width: 700px;

  margin: 0 auto 13px;

  font-size: clamp(2rem, 5vw, 3.4rem);
}

.contact-card > p {
  max-width: 620px;

  margin: 0 auto 26px;
}

.contact-card .hero__actions {
  justify-content: center;
}

.contact-card .btn--ghost {
  color: #4c5968 !important;

  background: #f6f8fb;

  border-color: var(--pf-border) !important;
}


/* =========================================================
   EMPTY FILTER RESULT
========================================================= */

.no-results {
  display: none;

  padding: 45px;

  grid-column: 1 / -1;

  border: 1px dashed #cbd5e0;
  border-radius: var(--pf-radius);

  text-align: center;

  color: var(--pf-muted);
}


/* =========================================================
   RESPONSIVE
========================================================= */

@media (max-width: 1020px) {

  .portfolio-hero__inner {
    grid-template-columns: 1fr;
  }

  .hero-panel {
    display: grid;

    grid-template-columns:
      repeat(2, minmax(0,1fr));

    gap: 0 26px;
  }

  .hero-panel__label {
    grid-column: 1 / -1;
  }

  .portfolio-page .grid {
    grid-template-columns:
      repeat(2, minmax(0,1fr));
  }

  .about-layout {
    grid-template-columns: 1fr;
  }

  .project-controls {
    align-items: flex-start;
    flex-direction: column;
  }

  #q {
    width: 100%;
  }
}


@media (max-width: 680px) {

  .page-content > .wrapper {
    padding-left: 14px !important;
    padding-right: 14px !important;
  }

  .portfolio-page {
    padding-top: 10px;
  }

  .portfolio-hero {
    min-height: auto;

    padding: 35px 24px;

    border-radius: 24px;
  }

  .portfolio-hero h1 {
    font-size: clamp(2.8rem, 14vw, 4.3rem);
  }

  .portfolio-hero h2 {
    font-size: 1.25rem;
  }

  .hero-panel {
    display: block;
  }

  .portfolio-section {
    padding-top: 70px;
  }

  .section-heading--split {
    align-items: flex-start;
    flex-direction: column;
    gap: 12px;
  }

  .portfolio-page .grid {
    grid-template-columns: 1fr;
  }

  .timeline-item {
    grid-template-columns: 1fr;

    gap: 8px;

    padding: 25px;
  }

  .cv-box {
    align-items: flex-start;
    flex-direction: column;
  }

  .cv-actions {
    width: 100%;
  }

  .cv-actions .btn {
    flex: 1;
  }
}
</style>


<div class="portfolio-page">


<!-- ======================================================
     HERO
======================================================= -->

<section class="portfolio-hero">

  <div class="portfolio-hero__inner">

    <div>

      <div class="hero__eyebrow">
        Electrical Engineering Student · Power Systems · Automation
      </div>

      <h1>
        Clément<br>
        Chevauchey
      </h1>

      <h2>
        Electrical Engineering Student focusing on
        <span>Power Systems & Industrial Automation.</span>
      </h2>

      <p class="hero__intro">
        Building practical experience in electrical network analysis,
        protection and industrial measurements through engineering projects,
        simulation and programming.
      </p>

      <div class="hero__actions">

        <a href="#projects" class="btn btn--primary">
          Explore my work ↓
        </a>

        <a href="#experience" class="btn btn--secondary">
          View CV
        </a>

        <a
          href="https://github.com/YofiClemy"
          target="_blank"
          rel="noopener"
          class="btn btn--ghost">
          GitHub ↗
        </a>

      </div>


      <div class="hero__availability">

        <span class="status-dot"></span>

        Open to 2026–27 internships and entry-level roles
        in Argentina or remote.

      </div>

    </div>


    <aside class="hero-panel">

      <div class="hero-panel__label">
        Engineering profile
      </div>

      <div class="hero-panel__item">
        <span>Focusing on</span>
        <strong>
          Power Systems · Protection · Automation
        </strong>
      </div>

      <div class="hero-panel__item">
        <span>Power studies</span>
        <strong>
          DIgSILENT PowerFactory · Load Flow · Short Circuit
        </strong>
      </div>

      <div class="hero-panel__item">
        <span>Electronics</span>
        <strong>
          LTspice · Proteus
        </strong>
      </div>

      <div class="hero-panel__item">
        <span>Programming</span>
        <strong>
          Python · NumPy · Pandas · MATLAB / Scilab
        </strong>
      </div>

      <div class="hero-panel__item">
        <span>Languages</span>
        <strong>
          French (Native) · English C1 · Spanish C1
        </strong>
      </div>

      <div class="hero-panel__item">
        <span>Undergraduate Teaching Assistant</span>
        <strong>
          Algorithms · PSeInt · Scilab · Microsoft Word, Excel, Access
        </strong>
      </div>

    </aside>

  </div>

</section>



<!-- ======================================================
     ABOUT
======================================================= -->

<section class="portfolio-section" id="about">

  <div class="section-heading">

    <span class="section-kicker">
      Profile
    </span>

    <h2>
      Engineering theory applied to practical problems.
    </h2>

    <p>
      My portfolio brings together university work, independent projects
      and technical experimentation across electrical engineering.
    </p>

  </div>


  <div class="about-layout">

    <article class="about-card">

      <p>
        I am an Electrical Engineering student developing my profile around
        electrical networks, power-system analysis and industrial automation.
      </p>

      <p>
        I am particularly interested in load-flow and short-circuit studies,
        protection fundamentals, PLC/SCADA systems and the use of engineering
        software to analyse real electrical systems.
      </p>

      <p>
        My projects combine circuit theory, simulation, measurements and
        programming using tools including DIgSILENT PowerFactory, Python,
        LTspice, Proteus and MATLAB/Scilab.
      </p>

    </article>


    <aside class="focus-card">

      <div class="focus-card__title">
        Current technical focus
      </div>

      <div class="focus-list">

        <div class="focus-item">
          <div class="focus-icon">~</div>
          <div>
            <strong>Power Systems</strong>
            <span>Network analysis & studies</span>
          </div>
        </div>

        <div class="focus-item">
          <div class="focus-icon">⚡</div>
          <div>
            <strong>Protection</strong>
            <span>Faults & protection fundamentals</span>
          </div>
        </div>

        <div class="focus-item">
          <div class="focus-icon">01</div>
          <div>
            <strong>Industrial Automation</strong>
            <span>PLC · SCADA · control logic</span>
          </div>
        </div>

        <div class="focus-item">
          <div class="focus-icon">{ }</div>
          <div>
            <strong>Engineering Computing</strong>
            <span>Python · simulation · data analysis</span>
          </div>
        </div>

      </div>

    </aside>

  </div>

</section>



<!-- ======================================================
     PROJECTS
======================================================= -->

<section class="portfolio-section" id="projects">

  <div class="section-heading section-heading--split">

    <div>

      <span class="section-kicker">
        Selected work
      </span>

      <h2>
        Engineering projects.
      </h2>

      <p>
        Academic and personal projects covering power systems,
        electronics, measurements, simulation and automation.
      </p>

    </div>

    <span class="project-count">
      {{ site.data.projects | size }} projects
    </span>

  </div>


  <div class="project-controls">

    <input
      id="q"
      type="search"
      placeholder="Search by project, skill or technology…"
      autocomplete="off"
      aria-label="Search projects">

    <div id="chips" class="chips">

      <button
        class="chip active"
        type="button"
        data-cat="all">
        All
      </button>

      <button
        class="chip"
        type="button"
        data-cat="power">
        Power Systems
      </button>

      <button
        class="chip"
        type="button"
        data-cat="electronics">
        Electronics
      </button>

      <button
        class="chip"
        type="button"
        data-cat="measurements">
        Measurements
      </button>

      <button
        class="chip"
        type="button"
        data-cat="logic">
        Automation / Logic
      </button>

    </div>

  </div>


  <div class="grid" id="grid">

    {% for p in site.data.projects %}
      {% include card.html p=p %}
    {% endfor %}

    <div class="no-results" id="no-results">
      No projects match your search.
    </div>

  </div>

</section>



<!-- ======================================================
     EXPERIENCE
======================================================= -->

<section class="portfolio-section" id="experience">

  <div class="section-heading">

    <span class="section-kicker">
      Background
    </span>

    <h2>
      Education & experience.
    </h2>

  </div>


  <div class="timeline">


    <article class="timeline-item">

      <div class="timeline-item__date">
        Current
      </div>

      <div class="timeline-item__content">

        <h3>
          Electrical Engineering
        </h3>

        <p class="timeline-item__meta">
          Universidad Nacional de Santiago del Estero
        </p>

        <p>
          Third-year student | GPA: 8.1/10
          
          Engineering studies covering electrical circuits,
          electromagnetics, electronics, mathematics, physics,
          electrical systems and engineering analysis.
        </p>

      </div>

    </article>


    <article class="timeline-item">

      <div class="timeline-item__date">
        2022–2025
      </div>

      <div class="timeline-item__content">

        <h3>
          University Teaching Assistant
        </h3>

        <p class="timeline-item__meta">
          Computing & engineering fundamentals
        </p>

        <p>
         Taught algorithms and pseudocode using PSeInt, as well as scientific programming with Scilab to Engineering students.
         Taught Microsoft Word, Excel and Access to students in scientific degrees such as Biotechnology and Chemistry.
         Applied teaching strategies combining algorithmic theory with hands-on programming, aimed at strengthening problem-solving skills for approximately 120 students per year.
        </p>

      </div>

    </article>


    <article class="timeline-item">

      <div class="timeline-item__date">
        Since 2016
      </div>

      <div class="timeline-item__content">

        <h3>
          Private English Tutor
        </h3>

        <p class="timeline-item__meta">
          Freelance
        </p>

        <p>
          Provided study-method support and academic tutoring in French, Mathematics, Science and English to secondary-school students.
        </p>

      </div>

    </article>

  </div>

  <div class="section-heading">

    <h2>
      Certifications
    </h2>

  </div>

    <div class="timeline">


    <article class="timeline-item">

      <div class="timeline-item__date">
        December 2025
      </div>

      <div class="timeline-item__content">

        <h3>
        Cambridge English
        </h3>

        <p class="timeline-item__meta">
          Cambridge university
        </p>

        <p>
          C1 Advanced - Grade A, given level C2 (CEFR)
        </p>

      </div>

    </article>


    <article class="timeline-item">

      <div class="timeline-item__date">
        August 2025
      </div>

      <div class="timeline-item__content">

        <h3>
          CS50x: Introduction to Computer Science
        </h3>

        <p class="timeline-item__meta">
          Harvard
        </p>

        <p>
         C, Python, SQL, HTML, CSS, and JavaScript.
         Memory, arrays, and data structures; high-level applications.
         Final Project: Self-directed software project, website based.
        </p>

      </div>

    </article>


    <article class="timeline-item">

      <div class="timeline-item__date">
        August 2023
      </div>

      <div class="timeline-item__content">

        <h3>
          R for Research
        </h3>

        <p class="timeline-item__meta">
          CONICET
        </p>

        <p>
          20 hours course on the use of R in various research fields.
          Practical study case and problem solving using R.
        </p>

      </div>

    </article>

  </div>

</section>


<!-- ======================================================
     CV
======================================================= -->

<section class="portfolio-section" id="cv">

  {% assign cv_en = '/assets/CV English.pdf' | relative_url %}
  {% assign cv_es = '/assets/CV spanish.pdf' | relative_url %}

  <div class="cv-box">

    <div>

      <span class="section-kicker">
        Curriculum Vitae
      </span>

      <h2>
        Prefer the conventional version?
      </h2>

      <p>
        My CV is available in English and Spanish.
      </p>

    </div>


    <div class="cv-actions">

      <a
        href="{{ cv_en }}"
        target="_blank"
        class="btn btn--primary">
        English CV ↗
      </a>

      <a
        href="{{ cv_es }}"
        target="_blank"
        class="btn btn--secondary">
        CV en Español ↗
      </a>

    </div>

  </div>

</section>



<!-- ======================================================
     CONTACT
======================================================= -->

<section class="portfolio-section" id="contact">

  <div class="contact-card">

    <span class="section-kicker">
      Contact
    </span>

    <h2>
      Let's build something useful.
    </h2>

    <p>
      I am interested in internships and entry-level opportunities
      involving power systems, electrical engineering, automation, measurement.
    </p>


    <div class="hero__actions">

      {% if site.email %}

        <a
          href="mailto:chevauchey.clement@gmail.com"
          class="btn btn--primary">
          Email me
        </a>

      {% endif %}


      {% if site.linkedin_url %}

        <a
          href="https://www.linkedin.com/in/clément-chevauchey-413644179/"
          target="_blank"
          rel="noopener"
          class="btn btn--secondary">
          LinkedIn ↗
        </a>

      {% endif %}


      <a
        href="https://github.com/YofiClemy"
        target="_blank"
        rel="noopener"
        class="btn btn--ghost">
        GitHub ↗
      </a>

    </div>

  </div>

</section>


</div>



<script>
document.addEventListener("DOMContentLoaded", function () {

  const search = document.getElementById("q");
  const chips = document.querySelectorAll(".chip");
  const cards = document.querySelectorAll("#grid .card");
  const noResults = document.getElementById("no-results");

  let activeCategory = "all";


  function filterProjects() {

    const query =
      (search.value || "")
        .trim()
        .toLowerCase();

    let visible = 0;


    cards.forEach(function(card) {

      const category =
        (card.dataset.cat || "")
          .toLowerCase();

      const searchable =
        card.textContent
          .toLowerCase();

      const categoryMatch =
        activeCategory === "all" ||
        category === activeCategory;

      const searchMatch =
        query === "" ||
        searchable.includes(query);

      const show =
        categoryMatch && searchMatch;

      card.style.display =
        show ? "" : "none";

      if (show) visible++;

    });


    if (noResults) {
      noResults.style.display =
        visible === 0 ? "block" : "none";
    }

  }


  chips.forEach(function(chip) {

    chip.addEventListener("click", function() {

      chips.forEach(function(c) {
        c.classList.remove("active");
      });

      chip.classList.add("active");

      activeCategory =
        chip.dataset.cat || "all";

      filterProjects();

    });

  });


  search.addEventListener(
    "input",
    filterProjects
  );

});
</script>
