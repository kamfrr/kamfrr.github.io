#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор каталога для сайта Южный Ветер."""

import json
import os
import shutil
from datetime import date

from inline_components import inline_components

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_DIR = os.path.join(BASE_DIR, 'catalog')
JS_DIR = os.path.join(BASE_DIR, 'js')

SITE_URL = 'https://swind.su'
SITE_NAME = 'Южный Ветер'
# JPG on purpose: messengers do not reliably render WebP link previews
OG_IMAGE = '/images/og-cover.jpg'
FONT_PRELOADS = '''  <link rel="preload" as="font" type="font/woff2" href="/fonts/inter-cyrillic.woff2" crossorigin>
  <link rel="preload" as="font" type="font/woff2" href="/fonts/inter-latin.woff2" crossorigin>'''
HERO_SIZES = '(min-width: 768px) 50vw, 100vw'
STATIC_PAGES = [
    ('/pages/about.html', '0.7'),
    ('/pages/otraslevye-resheniya.html', '0.7'),
    ('/pages/klientam.html', '0.6'),
    ('/pages/sertifikaty.html', '0.6'),
    ('/pages/contacts.html', '0.7'),
]


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def js_str(value):
    return json.dumps(value, ensure_ascii=False)


def thumb_for(image):
    """Path of the 800px version of an image, if one was generated next to it."""
    if not image or not image.endswith('.webp'):
        return ""
    thumb = image[:-len('.webp')] + '-800.webp'
    return thumb if os.path.exists(os.path.join(BASE_DIR, thumb.lstrip('/'))) else ""


def srcset_attr(image, sizes):
    thumb = thumb_for(image)
    return f' srcset="{thumb} 800w, {image} 1600w" sizes="{sizes}"' if thumb else ""


def abs_url(path):
    return SITE_URL + path


def canonical_og_tags(title, description, path):
    def attr(value):
        return value.replace('"', '&quot;')

    lines = [
        f'  <link rel="canonical" href="{abs_url(path)}">',
        '  <meta property="og:type" content="website">',
        f'  <meta property="og:site_name" content="{SITE_NAME}">',
        '  <meta property="og:locale" content="ru_RU">',
        f'  <meta property="og:title" content="{attr(title)}">',
    ]
    if description:
        lines.append(f'  <meta property="og:description" content="{attr(description)}">')
    lines.append(f'  <meta property="og:url" content="{abs_url(path)}">')
    lines.append(f'  <meta property="og:image" content="{abs_url(OG_IMAGE)}">')
    return "\n".join(lines)


def json_ld(data):
    body = json.dumps(data, ensure_ascii=False, indent=2).replace('</', '<\\/')
    body = "\n".join("  " + line for line in body.split("\n"))
    return f'  <script type="application/ld+json">\n{body}\n  </script>'


def breadcrumb_ld(items):
    """items: list of (name, path) from the site root to the current page."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": abs_url(path)}
            for i, (name, path) in enumerate(items, start=1)
        ],
    }


def product_ld(category, product):
    images = product.get("images") or ([product["image"]] if product.get("image") else [])
    data = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": product["name"],
        "description": product["description"],
        "url": abs_url(f'/catalog/{category["slug"]}/{product["slug"]}/'),
        "category": category["name"],
    }
    if images:
        data["image"] = [abs_url(img) for img in images]
    if product.get("brand"):
        data["brand"] = {"@type": "Brand", "name": product["brand"]}
    return data


def generate_sitemap(categories, products):
    today = date.today().isoformat()
    entries = [('/', '1.0'), ('/catalog/', '0.9')]
    for cat in categories:
        entries.append((f'/catalog/{cat["slug"]}/', '0.8'))
        for prod in products.get(cat["slug"], []):
            entries.append((f'/catalog/{cat["slug"]}/{prod["slug"]}/', '0.7'))
    entries += STATIC_PAGES
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, priority in entries:
        lines.append(f'  <url><loc>{abs_url(path)}</loc><lastmod>{today}</lastmod><priority>{priority}</priority></url>')
    lines.append('</urlset>')
    return "\n".join(lines) + "\n"


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
    if product.get("brand"):
        lines.append(f'      brand: {js_str(product["brand"])},')
    lines.append(f'      image: {js_str(product.get("image", ""))},')
    if thumb_for(product.get("image", "")):
        lines.append(f'      thumb: {js_str(thumb_for(product["image"]))},')
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
    if product.get("details"):
        lines[-1] += ","
        lines.append("      details: [")
        for d in product["details"]:
            lines.append(f'        {js_str(d)},')
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
    cat_image = category.get("image", "")
    hero_style = f' style="background-image: url(\'{cat_image}\');"' if cat_image and "placeholder" not in cat_image else ""
    product_links = "\n".join([
        f'          <li><a href="/catalog/{slug}/{p["slug"]}/">{p["name"]}</a></li>'
        for p in products_list
    ])
    path = f'/catalog/{slug}/'
    title = f'{category["title"]} купить с доставкой | Южный Ветер'
    description = f'{category["description"]} Прямые поставки от производителей. Доставка по РФ.'
    head_seo = canonical_og_tags(title, description, path)
    ld = json_ld(breadcrumb_ld([("Главная", "/"), ("Продукция", "/catalog/"), (category["name"], path)]))
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" type="image/x-icon" href="/favicon/favicon.ico">
  <link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png">
{head_seo}
{FONT_PRELOADS}
  <link rel="stylesheet" href="/css/variables.css">
  <link rel="stylesheet" href="/css/base.css?v=2">
  <link rel="stylesheet" href="/css/components.css">
  <link rel="stylesheet" href="/css/layout.css">
  <script src="/js/products-data.js" defer></script>
{extra_scripts}
  <script src="/js/components.js" defer></script>
  <script src="/js/category-page.js" defer></script>
{ld}
</head>
<body>
  <div id="site-header"></div>
  <main>
    <div class="breadcrumbs"><div class="container"><a href="/">Главная</a> <span>/</span> <a href="/catalog/">Продукция</a> <span>/</span> <span>{category["name"]}</span></div></div>
    <section class="page-hero"{hero_style}>
      <div class="container">
        <h1>{category["title"]} — купить с доставкой</h1>
        <p class="page-hero-sub">{category["description"]}</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div id="products-grid" class="grid grid-sm-2 grid-md-3" style="margin-bottom: var(--space-10);"></div>
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


def generate_product_page(category, product):
    cat_slug = category["slug"]
    p = product
    images = p.get("images") or ([p["image"]] if p.get("image") else [])
    if len(images) > 1:
        imgs_json = json.dumps(images, ensure_ascii=False)
        image_html = (
            f'<div class="product-hero-image carousel" data-carousel=\'{imgs_json}\' data-i="0">'
            f'<img src="{images[0]}" alt="{p["name"]}">'
            f'<button type="button" class="carousel-btn carousel-prev" onclick="carouselMove(this, -1)" aria-label="Предыдущее фото">&#8249;</button>'
            f'<button type="button" class="carousel-btn carousel-next" onclick="carouselMove(this, 1)" aria-label="Следующее фото">&#8250;</button>'
            f'<div class="carousel-counter">1 / {len(images)}</div>'
            f'</div>'
        )
    elif images:
        image_html = f'<div class="product-hero-image"><img src="{images[0]}"{srcset_attr(images[0], HERO_SIZES)} alt="{p["name"]}"></div>'
    else:
        image_html = f'<div class="product-hero-image"><div class="img-placeholder"><span class="img-placeholder-name">{p["name"]}</span><span class="img-placeholder-note">Фото скоро появится</span></div></div>'
    specs_rows = "\n".join([f'              <tr><td>{s["param"]}</td><td>{s["value"]}</td></tr>' for s in p.get("specs", [])])
    adv_items = "\n".join([f'            <li>{a}</li>' for a in p.get("advantages", [])])
    app_items = "\n".join([f'            <li>{a}</li>' for a in p.get("applications", [])])
    details_html = ""
    if p.get("details"):
        detail_paras = "\n".join([f'        <p style="color: var(--color-text-secondary); line-height: var(--line-height-relaxed); margin: var(--space-4) 0;">{d}</p>' for d in p["details"]])
        details_html = f'''        <h2 style="margin-top: var(--space-10);">Описание</h2>
{detail_paras}
'''
    path = f'/catalog/{cat_slug}/{p["slug"]}/'
    title = f'{p["name"]} купить с доставкой | Южный Ветер'
    description = p["description"][:160]
    head_seo = canonical_og_tags(title, description, path)
    ld = "\n".join([
        json_ld(breadcrumb_ld([("Главная", "/"), ("Продукция", "/catalog/"),
                               (category["name"], f'/catalog/{cat_slug}/'), (p["name"], path)])),
        json_ld(product_ld(category, p)),
    ])
    brand_html = f'\n            <div class="tag">{p["brand"]}</div>' if p.get("brand") else ""
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" type="image/x-icon" href="/favicon/favicon.ico">
  <link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png">
{head_seo}
{FONT_PRELOADS}
  <link rel="stylesheet" href="/css/variables.css">
  <link rel="stylesheet" href="/css/base.css?v=2">
  <link rel="stylesheet" href="/css/components.css">
  <link rel="stylesheet" href="/css/layout.css">
  <script src="/js/components.js" defer></script>
{ld}
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
            <h1>{p["name"]} — купить с доставкой</h1>{brand_html}
            <p style="color: var(--color-text-secondary); line-height: var(--line-height-relaxed); margin: var(--space-6) 0;">{p["description"]}</p>
            <a href="/pages/contacts.html" class="btn btn-primary btn-large">Получить коммерческое предложение</a>
          </div>
        </div>
{details_html}        <h2>Технические характеристики</h2>
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
            f.write(inline_components(generate_category_page(cat, products.get(cat["slug"], []), extra_scripts)))
        for prod in products.get(cat["slug"], []):
            prod_dir = os.path.join(cat_dir, prod["slug"])
            ensure_dir(prod_dir)
            with open(os.path.join(prod_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(inline_components(generate_product_page(cat, prod)))

    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(generate_sitemap(categories, products))

    print("Catalog generated successfully.")
    print(f"Categories: {len(categories)}")
    print(f"Products: {sum(len(v) for v in products.values())}")


if __name__ == '__main__':
    main()
