(function(){
  const stored = localStorage.getItem('theme');
  let theme = stored || (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  document.documentElement.setAttribute('data-theme', theme);

  function apply(next){
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.textContent = next === 'light' ? '☾ Dark' : '☀︎ Light';
      btn.setAttribute('aria-label', 'Switch to ' + (next === 'light' ? 'dark' : 'light') + ' theme');
    }
  }

  function ensureButton(container){
    if (!container || document.getElementById('theme-toggle')) return;
    const btn = document.createElement('button');
    btn.id = 'theme-toggle';
    btn.className = 'theme-toggle page-link';
    btn.type = 'button';
    btn.textContent = theme === 'light' ? '☾ Dark' : '☀︎ Light';
    btn.addEventListener('click', () => {
      theme = (document.documentElement.getAttribute('data-theme') === 'light') ? 'dark' : 'light';
      apply(theme);
    });
    container.appendChild(btn); // last item => right side (with CSS below)
  }

  function start(){
    const trg = document.querySelector('.site-nav .trigger');
    if (trg) { ensureButton(trg); return; }
    const obs = new MutationObserver(() => {
      const t = document.querySelector('.site-nav .trigger');
      if (t) { ensureButton(t); obs.disconnect(); }
    });
    obs.observe(document.documentElement, { childList:true, subtree:true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();