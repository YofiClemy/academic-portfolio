
(function(){
  const q = document.getElementById('q');
  const chips = [...document.querySelectorAll('.chip')];
  const cards = [...document.querySelectorAll('.card')];
  function applyFilter(){
    const text=(q&&q.value||'').toLowerCase().trim();
    const activeChip=document.querySelector('.chip.active');
    const active=activeChip?activeChip.dataset.cat:'all';
    cards.forEach(card=>{
      const catOk=(active==='all')||(card.dataset.cat===active);
      const txt=(card.dataset.title+' '+card.dataset.sub).toLowerCase();
      const textOk=!text||txt.includes(text);
      card.style.display=(catOk&&textOk)?'':'';
    });
  }
  chips.forEach(c=>c.addEventListener('click',()=>{chips.forEach(x=>x.classList.remove('active'));c.classList.add('active');applyFilter();}));
  if(q) q.addEventListener('input',applyFilter);
})();
