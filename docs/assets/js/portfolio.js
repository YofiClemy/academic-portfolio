
document.addEventListener('DOMContentLoaded', () => {
  const q = document.getElementById('q');
  const chips = Array.from(document.querySelectorAll('.chip'));
  const cards = Array.from(document.querySelectorAll('.card'));
  function active(){ const el=document.querySelector('.chip.active'); return (el&&el.dataset?el.dataset.cat:'all').toLowerCase(); }
  function match(card,text,cat){
    const c=(card.dataset.cat||'').toLowerCase();
    const hay=((card.dataset.title||'')+' '+(card.dataset.sub||'')).toLowerCase();
    return ((cat==='all')||(c===cat)) && (!text || hay.includes(text));
  }
  function apply(){
    const t=(q&&q.value||'').toLowerCase().trim(), c=active();
    cards.forEach(card => { card.style.display = match(card,t,c) ? '' : 'none'; });
  }
  chips.forEach(ch => ch.addEventListener('click', () => { chips.forEach(x=>x.classList.remove('active')); ch.classList.add('active'); apply(); }));
  if(q) q.addEventListener('input', apply);
  apply();
});
