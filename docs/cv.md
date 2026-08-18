---
layout: page
title: "CV"
permalink: /cv/
---

{% assign cv_en = '/assets/CV English.pdf' | relative_url %}
{% assign cv_es = '/assets/CV spanish.pdf' | relative_url %}

<div class="cv-section">

  <div class="cv-language-selector" aria-label="CV language">
    <button
      type="button"
      class="cv-lang active"
      data-pdf="{{ cv_en }}"
      data-label="Download English PDF">
      English
    </button>

    <button
      type="button"
      class="cv-lang"
      data-pdf="{{ cv_es }}"
      data-label="Descargar CV en español">
      Español
    </button>
  </div>

  <div class="pdf-embed">
    <iframe
      id="cv-frame"
      src="{{ cv_en }}#view=Fit"
      title="Curriculum Vitae"
      loading="lazy">
    </iframe>
  </div>

  <p class="pdf-download">
    <a id="cv-download" href="{{ cv_en }}" target="_blank">
      Download English PDF
    </a>
  </p>

</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".cv-lang");
  const frame = document.getElementById("cv-frame");
  const download = document.getElementById("cv-download");

  buttons.forEach(button => {
    button.addEventListener("click", function () {
      const pdf = this.dataset.pdf;
      const label = this.dataset.label;

      frame.src = pdf + "#view=Fit";
      download.href = pdf;
      download.textContent = label;

      buttons.forEach(btn => btn.classList.remove("active"));
      this.classList.add("active");
    });
  });
});
</script>
