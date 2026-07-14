#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор каталога для сайта Южный Ветер."""

import json
import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_DIR = os.path.join(BASE_DIR, 'catalog')
JS_DIR = os.path.join(BASE_DIR, 'js')


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def js_str(value):
    return json.dumps(value, ensure_ascii=False)


def generate_categories_js(categories):
    lines = ["const CATEGORIES = ["]
    for cat in categories:
        lines.append("  {")
        lines.append(f'    slug: {js_str(cat["slug"])},')
        lines.append(f'    name: {js_str(cat["name"])},')
        lines.append(f'    title: {js_str(cat["title"])},')
        lines.append(f'    description: {js_str(cat["description"])},')
        lines.append(f'    image: {js_str(cat["image"])}')
        lines.append("  },")
    lines.append("];")
    lines.append("")
    lines.append("if (typeof module !== 'undefined' && module.exports) { module.exports = { CATEGORIES }; }")
    return "\n".join(lines)


def product_to_js(product):
    lines = ["    {"]
    lines.append(f'      slug: {js_str(product["slug"])},')
    lines.append(f'      name: {js_str(product["name"])},')
    lines.append(f'      category: {js_str(product.get("category", ""))},')
    lines.append(f'      brand: {js_str(product["brand"])},')
    lines.append(f'      image: {js_str(product.get("image", ""))},')
    lines.append(f'      description: {js_str(product["description"])},')
    lines.append("      specs: [")
    for spec in product.get("specs", []):
        lines.append(f'        {{ param: {js_str(spec["param"])}, value: {js_str(spec["value"])} }},')
    lines.append("      ],")
    lines.append("      advantages: [")
    for adv in product.get("advantages", []):
        lines.append(f'        {js_str(adv)},')
    lines.append("      ],")
    lines.append("      applications: [")
    for app in product.get("applications", []):
        lines.append(f'        {js_str(app)},')
    lines.append("      ]")
    lines.append("    }")
    return "\n".join(lines)


def _generate_products_body(categories, products):
    body_lines = []
    for cat in categories:
        slug = cat["slug"]
        prods = products.get(slug, [])
        if not prods:
            continue
        body_lines.append(f'  {js_str(slug)}: [')
        for i, p in enumerate(prods):
            if i > 0:
                body_lines[-1] += ","
            p_copy = dict(p)
            p_copy["category"] = slug
            body_lines.append(product_to_js(p_copy))
        body_lines.append("  ],")
    return body_lines


def generate_products_js(categories, products, include_helpers=True):
    body = _generate_products_body(categories, products)
    if include_helpers:
        lines = ["const PRODUCTS = {"]
        lines.extend(body)
        lines.append("};")
        lines.append("")
        lines.append("function getCategory(slug) { return CATEGORIES.find(c => c.slug === slug); }")
        lines.append("function getProductsByCategory(slug) { return PRODUCTS[slug] || []; }")
        lines.append("function getProduct(category, slug) { return (PRODUCTS[category] || []).find(p => p.slug === slug); }")
        lines.append("function getAllProducts() { return Object.values(PRODUCTS).flat(); }")
        lines.append("function generateBreadcrumb(items) { return items.map((item, i) => i === items.length - 1 ? `<span>${item.name}</span>` : `<a href=\"${item.url}\">${item.name}</a>`).join(' <span>/</span> '); }")
        lines.append("if (typeof module !== 'undefined' && module.exports) { module.exports = { CATEGORIES, PRODUCTS, getCategory, getProductsByCategory, getProduct, getAllProducts }; }")
        return "\n".join(lines)
    else:
        lines = ["Object.assign(PRODUCTS, {"]
        lines.extend(body)
        lines.append("});")
        return "\n".join(lines)


def generate_category_page(category, products_list, extra_scripts=""):
    slug = category["slug"]
    product_links = "\n".join([
        f'          <li><a href="/catalog/{slug}/{p["slug"]}/">{p["name"]}</a></li>'
        for p in products_list
    ])
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{category["title"]} купить с доставкой | Южный Ветер</title>
  <meta name="description" content="{category["description"]} Прямые поставки от производителей. Доставка по РФ.">
  <link rel="icon" type="image/x-icon" href="/favicon/favicon.ico">
  <link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png">
  <link rel="canonical" href="/catalog/{slug}/">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/variables.css">
  <link rel="stylesheet" href="/css/base.css">
  <link rel="stylesheet" href="/css/components.css">
  <link rel="stylesheet" href="/css/layout.css">
  <script src="/js/categories.js" defer></script>
  <script src="/js/products-data.js" defer></script>
{extra_scripts}
  <script src="/js/components.js" defer></script>
  <script src="/js/category-page.js" defer></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Главная", "item": "/"}},
      {{"@type": "ListItem", "position": 2, "name": "Продукция", "item": "/catalog/"}},
      {{"@type": "ListItem", "position": 3, "name": "{category["name"]}", "item": "/catalog/{slug}/"}}
    ]
  }}
  </script>
</head>
<body>
  <div id="site-header"></div>
  <main>
    <div class="breadcrumbs"><div class="container"><a href="/">Главная</a> <span>/</span> <a href="/catalog/">Продукция</a> <span>/</span> <span>{category["name"]}</span></div></div>
    <section class="section">
      <div class="container">
        <h1>{category["title"]} — купить с доставкой</h1>
        <p style="color: var(--color-text-secondary); line-height: var(--line-height-relaxed); margin: var(--space-6) 0;">{category["description"]}</p>
        <div id="products-grid" class="grid grid-sm-2 grid-md-3" style="margin: var(--space-10) 0;"></div>
        <div style="margin-top: var(--space-16);">
          <h2>Виды оборудования</h2>
          <ul style="color: var(--color-text-secondary); line-height: var(--line-height-relaxed); padding-left: var(--space-6);">
{product_links}
          </ul>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer"></div>
  <script>document.addEventListener('DOMContentLoaded', () => {{ if (typeof initCategoryPage === 'function') initCategoryPage('{slug}', '{category["name"]}', '{category["title"]}', '{category["description"]}'); }});</script>
</body>
</html>
'''


def generate_product_page(category, product, extra_scripts=""):
    cat_slug = category["slug"]
    p = product
    image = p.get("image", "")
    image_html = f'<div class="product-hero-image"><img src="{image}" alt="{p["name"]}"></div>' if image else ""
    specs_rows = "\n".join([f'              <tr><td>{s["param"]}</td><td>{s["value"]}</td></tr>' for s in p.get("specs", [])])
    adv_items = "\n".join([f'            <li>{a}</li>' for a in p.get("advantages", [])])
    app_items = "\n".join([f'            <li>{a}</li>' for a in p.get("applications", [])])
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p["name"]} купить с доставкой | Южный Ветер</title>
  <meta name="description" content="{p["description"][:160]}">
  <link rel="icon" type="image/x-icon" href="/favicon/favicon.ico">
  <link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png">
  <link rel="canonical" href="/catalog/{cat_slug}/{p["slug"]}/">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/variables.css">
  <link rel="stylesheet" href="/css/base.css">
  <link rel="stylesheet" href="/css/components.css">
  <link rel="stylesheet" href="/css/layout.css">
  <script src="/js/categories.js" defer></script>
  <script src="/js/products-data.js" defer></script>
  <script src="/js/products-extra.js" defer></script>
  <script src="/js/components.js" defer></script>
</head>
<body>
  <div id="site-header"></div>
  <main>
    <div class="breadcrumbs"><div class="container"><a href="/">Главная</a> <span>/</span> <a href="/catalog/">Продукция</a> <span>/</span> <a href="/catalog/{cat_slug}/">{category["name"]}</a> <span>/</span> <span>{p["name"]}</span></div></div>
    <section class="section">
      <div class="container">
        <div class="product-hero">
          {image_html}
          <div class="product-hero-body">
            <h1>{p["name"]} — купить с доставкой</h1>
            <div class="tag">{p["brand"]}</div>
            <p style="color: var(--color-text-secondary); line-height: var(--line-height-relaxed); margin: var(--space-6) 0;">{p["description"]}</p>
            <a href="/pages/contacts.html" class="btn btn-primary btn-large">Получить коммерческое предложение</a>
          </div>
        </div>
        <h2>Технические характеристики</h2>
        <div class="table-wrap">
          <table class="table">
            <tr><th>Параметр</th><th>Значение</th></tr>
{specs_rows}
          </table>
        </div>
        <h2 style="margin-top: var(--space-10);">Преимущества</h2>
        <ol style="color: var(--color-text-secondary); line-height: var(--line-height-relaxed); padding-left: var(--space-6);">
{adv_items}
        </ol>
        <h2 style="margin-top: var(--space-10);">Области применения</h2>
        <ul style="color: var(--color-text-secondary); line-height: var(--line-height-relaxed); padding-left: var(--space-6);">
{app_items}
        </ul>
      </div>
    </section>
  </main>
  <div id="site-footer"></div>
</body>
</html>
'''


def main():
    data_path = os.path.join(os.path.dirname(__file__), 'catalog_data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = data["categories"]
    products = data["products"]

    # Backup
    for src in [os.path.join(JS_DIR, 'categories.js'), os.path.join(JS_DIR, 'products-data.js')]:
        if os.path.exists(src):
            shutil.copy(src, src + '.bak')

    # Write JS split into files to stay under 600 lines each
    with open(os.path.join(JS_DIR, 'categories.js'), 'w', encoding='utf-8') as f:
        f.write(generate_categories_js(categories))

    # Determine number of product files needed (roughly < 600 lines each)
    total_cats = len(categories)
    cats_per_file = 6
    product_parts = []
    for i in range(0, total_cats, cats_per_file):
        product_parts.append(categories[i:i + cats_per_file])

    # Main data file includes helpers
    with open(os.path.join(JS_DIR, 'products-data.js'), 'w', encoding='utf-8') as f:
        f.write(generate_products_js(product_parts[0], products, include_helpers=True))

    # Extra data files extend PRODUCTS
    extra_files = ['products-extra.js', 'products-extra-2.js']
    for idx, part in enumerate(product_parts[1:], start=0):
        fname = extra_files[idx] if idx < len(extra_files) else f'products-extra-{idx + 1}.js'
        with open(os.path.join(JS_DIR, fname), 'w', encoding='utf-8') as f:
            f.write(generate_products_js(part, products, include_helpers=False))

    # Remove old category dirs
    for item in os.listdir(CATALOG_DIR):
        item_path = os.path.join(CATALOG_DIR, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)

    # Generate script tags for extra product files
    extra_scripts = "\n".join([
        f'  <script src="/js/{fname}" defer></script>'
        for fname in sorted(os.listdir(JS_DIR))
        if fname.startswith('products-extra') and fname.endswith('.js')
    ])

    # Generate pages
    for cat in categories:
        cat_dir = os.path.join(CATALOG_DIR, cat["slug"])
        ensure_dir(cat_dir)
        with open(os.path.join(cat_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(generate_category_page(cat, products.get(cat["slug"], []), extra_scripts))
        for prod in products.get(cat["slug"], []):
            prod_dir = os.path.join(cat_dir, prod["slug"])
            ensure_dir(prod_dir)
            with open(os.path.join(prod_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(generate_product_page(cat, prod, extra_scripts))

    print("Catalog generated successfully.")
    print(f"Categories: {len(categories)}")
    print(f"Products: {sum(len(v) for v in products.values())}")


if __name__ == '__main__':
    main()
