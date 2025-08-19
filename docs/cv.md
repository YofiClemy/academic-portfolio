---
layout: page
title: "CV"
permalink: /cv/
---

{% assign cv = '/assets/CV.pdf' | relative_url %}

<div class="pdf-embed">
  <object data="{{ cv }}" type="application/pdf" width="100%" height="100%">
    <!-- Fallback if the browser blocks <object>: -->
    <iframe src="{{ cv }}" width="100%" height="100%"></iframe>
  </object>
</div>

<p><a href="{{ cv }}">Download PDF</a></p>
