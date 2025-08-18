document.addEventListener('DOMContentLoaded', () => {
  const q = document.getElementById('q');
  const chips = Array.from(document.querySelectorAll('.chip'));
  const cards = Array.from(document.querySelectorAll('.card'));

  function activeCat(){
    const el = document.querySelector('.chip.active');
    return (el && el.dataset && el.dataset.cat ? el.dataset.cat : 'all').toLowerCase();
  }
  function match(card, text, cat){
    const ccat = (card.dataset && card.dataset.cat ? card.dataset.cat : '').toLowerCase();
    const hay  = ((card.dataset.title||'') + ' ' + (card.dataset.sub||'')).toLowerCase();
    const catOK = (cat === 'all') || (ccat === cat);
    const textOK = !text || hay.includes(text);
    return catOK && textOK;
  }
  function apply(){
    const text = (q && q.value ? q.value : '').toLowerCase().trim();
    const cat  = activeCat();
    cards.forEach(card => { card.style.display = match(card, text, cat) ? '' : 'none'; });
  }
  chips.forEach(c => c.addEventListener('click', () => {
    chips.forEach(x => x.classList.remove('active'));
    c.classList.add('active'); apply();
  }));
  if (q) q.addEventListener('input', apply);
  apply();
});