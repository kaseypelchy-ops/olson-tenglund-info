/* Avoid broken image icons when remote product photo hosts block third-party requests. */
document.addEventListener('DOMContentLoaded', () => {
 for(const img of document.querySelectorAll('.promo-card-image img')) {
  const showFallback=()=>{
   if(img.dataset.failed==='1') return; img.dataset.failed='1';
   const title=img.dataset.productTitle||'Product';
   const source=img.dataset.productSource;
   const holder=document.createElement('div'); holder.className='promo-photo-unavailable';
   const icon=document.createElement('strong');icon.textContent=title;
   const msg=document.createElement('span');msg.textContent='Photo temporarily unavailable — view item details below.';
   holder.append(icon,msg);
   if(source){const a=document.createElement('a');a.href=source;a.rel='noopener noreferrer';a.target='_blank';a.textContent='View product reference';holder.append(a);}
   img.replaceWith(holder);
  };
  img.addEventListener('error',showFallback);
  if(img.complete&&img.naturalWidth===0) showFallback();
 }
});
