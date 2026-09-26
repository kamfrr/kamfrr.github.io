function initProductPage(categorySlug, productSlug) {
  const product = getProduct(categorySlug, productSlug);
  if (!product) return;

  document.title = `${product.name} купить от производителя | Южный Ветер`;
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) metaDesc.content = `${product.name} — цена, характеристики, срок изготовления. Производство по ГОСТ. Доставка по РФ. Закажите расчет!`;

  const h1 = document.querySelector('h1');
  if (h1) h1.textContent = `${product.name} — купить от производителя`;

  const desc = document.getElementById('product-description');
  if (desc) desc.innerHTML = `<p>${product.description}</p>`;

  // Product image
  const imgContainer = document.querySelector('.product-card-img, [style*="aspect-ratio: 16/9"]');
  if (imgContainer && product.image) {
    imgContainer.innerHTML = `<img src="${product.image}" alt="${product.name}" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-xl);">`;
  }

  const specsTable = document.getElementById('product-specs');
  if (specsTable && product.specs) {
    specsTable.innerHTML = product.specs.map(s => `<tr><td>${s.param}</td><td>${s.value}</td></tr>`).join('');
  }

  const advList = document.getElementById('product-advantages');
  if (advList && product.advantages) {
    advList.innerHTML = product.advantages.map(a => `<li>${a}</li>`).join('');
  }

  const appList = document.getElementById('product-applications');
  if (appList && product.applications) {
    appList.innerHTML = product.applications.map(a => `<li>${a}</li>`).join('');
  }

  const faqContainer = document.getElementById('product-faq');
  if (faqContainer && product.faq) {
    faqContainer.innerHTML = product.faq.map((f, i) => `
      <div class="accordion-item ${i === 0 ? 'active' : ''}">
        <button class="accordion-header" onclick="this.parentElement.classList.toggle('active')">
          ${f.q}
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
        </button>
        <div class="accordion-body"><div class="accordion-content">${f.a}</div></div>
      </div>
    `).join('');
  }

  // Related products
  const related = getProductsByCategory(categorySlug).filter(p => p.slug !== productSlug).slice(0, 3);
  const relatedGrid = document.getElementById('related-products');
  if (relatedGrid && related.length) {
    relatedGrid.innerHTML = related.map(p => {
      const imgHtml = p.image ?
        `<img src="${p.image}" alt="${p.name}" loading="lazy" style="width:100%;height:100%;object-fit:cover;">` :
        `<div class="img-placeholder"><span class="img-placeholder-name">${p.name}</span><span class="img-placeholder-note">Фото скоро появится</span></div>`;
      return `
      <a href="/catalog/${categorySlug}/${p.slug}/" class="product-card">
        <div class="product-card-img">${imgHtml}</div>
        <div class="product-card-body">
          ${p.brand ? `<div class="tag mb-4">${p.brand}</div>` : ''}
          <h3 class="product-card-title">${p.name}</h3>
        </div>
      </a>
    `}).join('');
  }
}
