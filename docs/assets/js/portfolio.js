document.addEventListener('DOMContentLoaded', () => {
  const q = document.getElementById('q');
  const chips = Array.from(document.querySelectorAll('.chip'));
  const cards = Array.from(document.querySelectorAll('.card'));
  if (!cards.length) return;  // nothing to do on pages without the grid

  function activeCat(){
    const el = document.querySelector('.chip.active');
    return (el && el.dataset && el.dataset.cat ? el.dataset.cat : 'all').toLowerCase();
  }
  function match(card, text, cat){
    const c = (card.dataset.cat || '').toLowerCase();
    const hay = ((card.dataset.title||'') + ' ' + (card.dataset.sub||'')).toLowerCase();
    return ((cat === 'all') || (c === cat)) && (!text || hay.includes(text));
  }
  function apply(){
    const text = (q && q.value || '').toLowerCase().trim();
    const cat = activeCat();
    cards.forEach(card => { card.style.display = match(card, text, cat) ? '' : 'none'; });
  }

  chips.forEach(ch => ch.addEventListener('click', () => {
    chips.forEach(x => x.classList.remove('active'));
    ch.classList.add('active');
    apply();
  }));
  if (q) q.addEventListener('input', apply);
  apply();
});