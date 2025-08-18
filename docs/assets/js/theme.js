
(function(){
  // Choose initial theme: localStorage > prefers-color-scheme > dark default
  const stored = localStorage.getItem('theme');
  let theme = stored || (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  document.documentElement.setAttribute('data-theme', theme);

  function apply(next){
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    btn.textContent = next === 'light' ? '☾ Dark' : '☀︎ Light';
    btn.setAttribute('aria-label', 'Switch to ' + (next === 'light' ? 'dark' : 'light') + ' theme');
  }

  // Inject button into the header
  function insertButton(){
    const header = document.querySelector('.site-header .wrapper') || document.querySelector('.site-header');
    if(!header) return;
    window.btn = document.createElement('button');
    btn.className = 'theme-toggle';
    btn.type = 'button';
    btn.textContent = theme === 'light' ? '☾ Dark' : '☀︎ Light';
    btn.addEventListener('click', function(){
      theme = (document.documentElement.getAttribute('data-theme') === 'light') ? 'dark' : 'light';
      apply(theme);
    });
    header.appendChild(btn);
  }

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', insertButton);
  } else {
    insertButton();
  }
})();
