(function(){
  const stored = localStorage.getItem('theme');
  let theme = stored || (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  document.documentElement.setAttribute('data-theme', theme);

  function apply(next){
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    const btn = document.getElementById('theme-toggle');
    if(btn){
      btn.textContent = next === 'light' ? '☾ Dark' : '☀︎ Light';
      btn.setAttribute('aria-label', 'Switch to ' + (next === 'light' ? 'dark' : 'light') + ' theme');
    }
  }

  function insertButton(){
    // Prefer putting the toggle inside the nav links container
    const target = document.querySelector('.site-nav .trigger');
    const header = document.querySelector('.site-header .wrapper') || document.querySelector('.site-header');
    const parent = target || header;
    if(!parent) return;

    // Avoid duplicates
    if(document.getElementById('theme-toggle')) return;

    const btn = document.createElement('button');
    btn.id = 'theme-toggle';
    btn.className = 'theme-toggle page-link'; // page-link keeps Minima spacing
    btn.type = 'button';
    btn.textContent = theme === 'light' ? '☾ Dark' : '☀︎ Light';
    btn.addEventListener('click', function(){
      theme = (document.documentElement.getAttribute('data-theme') === 'light') ? 'dark' : 'light';
      apply(theme);
    });
    parent.appendChild(btn);
  }

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', insertButton);
  } else {
    insertButton();
  }
})();