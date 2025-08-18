(function(){
  const stored = localStorage.getItem('theme');
  const prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
  let theme = stored || (prefersLight ? 'light' : 'dark');

  function apply(next){
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    const btn = document.getElementById('theme-toggle');
    if(btn){
      btn.textContent = next === 'light' ? '☾ Dark' : '☀︎ Light';
      btn.setAttribute('aria-label', 'Switch to ' + (next === 'light' ? 'dark' : 'light') + ' theme');
    }
  }

  function ready(fn){ document.readyState==='loading' ? document.addEventListener('DOMContentLoaded', fn) : fn(); }

  ready(function(){
    apply(theme);
    const btn = document.getElementById('theme-toggle');
    if(btn){ btn.addEventListener('click', () => { theme = (theme==='light' ? 'dark' : 'light'); apply(theme); }); }
  });
})();