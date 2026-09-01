// Category page renderer
function initCategoryPage(categorySlug, categoryName, categoryTitle, categoryDescription, seoText) {
  document.title = `${categoryTitle} купить с доставкой | Южный Ветер`;
  
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) metaDesc.content = `${categoryTitle} — цена, характеристики, сроки поставки. Соответствие ГОСТ. Доставка по РФ. Закажите расчет!`;

  const products = getProductsByCategory(categorySlug);
  const grid = document.getElementById('products-grid');
  
  if (grid && products.length) {
    grid.innerHTML = products.map(p => {
      const imgHtml = p.image ?
        `<img src="${p.image}" alt="${p.name}" loading="lazy" style="width:100%;height:100%;object-fit:cover;">` :
        `<div class="img-placeholder"><span class="img-placeholder-name">${p.name}</span><span class="img-placeholder-note">Фото скоро появится</span></div>`;
      return `
      <a href="/catalog/${categorySlug}/${p.slug}/" class="product-card">
        <div class="product-card-img">${imgHtml}</div>
        <div class="product-card-body">
          <div class="tag mb-4">${p.brand}</div>
          <h3 class="product-card-title">${p.name}</h3>
          <p class="product-card-text">${p.description.substring(0, 120)}...</p>
        </div>
      </a>
    `}).join('');
  }

  const faqContainer = document.getElementById('faq-container');
  if (faqContainer && products.length) {
    const allFaq = products.flatMap(p => p.faq || []).slice(0, 6);
    if (allFaq.length) {
      faqContainer.innerHTML = allFaq.map((f, i) => `
        <div class="accordion-item ${i === 0 ? 'active' : ''}">
          <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
            ${f.q}
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="accordion-body"><div class="accordion-content">${f.a}</div></div>
        </div>
      `).join('');
    }
  }
}

function toggleAccordion(el) {
  el.parentElement.classList.toggle('active');
}
