(function(){
  const stored = localStorage.getItem('theme');
  const prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
  let theme = stored || (prefersLight ? 'light' : 'dark');

  function setButtonLabel(){
    const btn = document.getElementById('theme-toggle');
    if(!btn) return;
    const next = (document.documentElement.getAttribute('data-theme') === 'light') ? 'dark' : 'light';
    btn.textContent = next === 'light' ? '☀︎ Light' : '☾ Dark';       // label shows TARGET theme
    btn.setAttribute('aria-label', 'Switch to ' + next + ' theme');
  }

  function apply(next){
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    setButtonLabel();
  }

  function ready(fn){ document.readyState==='loading' ? document.addEventListener('DOMContentLoaded', fn) : fn(); }

  ready(function(){
    apply(theme);
    const btn = document.getElementById('theme-toggle');
    if(btn){ btn.addEventListener('click', () => { theme = (theme==='light' ? 'dark' : 'light'); apply(theme); }); }
  });
})();