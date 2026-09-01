#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Реструктуризация каталога под структуру «Текст для сайта 1.docx»: 10 разделов.

Разделы docx:
 1. КТПБ (комплектные трансформаторные подстанции)
 2. Оборудование для трансформаторных подстанций до 500 кВ (2.1–2.3)
 3. КРУЭ до 500 кВ (3.1–3.6)
 4. Трансформаторы до 220 кВ (4.1–4.3)
 5. КРУ до 35 кВ (5.1–5.3)
 6. РУ 0,4 кВ (6.1)
 7. Токопроводы и шинопроводы (7.1–7.3)
 8. Релейная защита и автоматика (8.1)
 9. Собственное производство
10. Блочно-модульные здания (10.1–10.3)

Прежние 19 категорий растворяются в этих 10 как подкатегории (продукты).
"""
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'catalog_data.json')

with open(DATA_PATH, encoding='utf-8') as f:
    data = json.load(f)

old_cats = {c['slug']: c for c in data['categories']}
old_prods = data['products']

# Порядок и оформление 10 разделов
CATEGORIES = [
    {
        'slug': 'ktp-bktp-rtp',
        'name': 'КТП / БКТП / КТПБ / РТП',
        'title': 'Комплектные трансформаторные подстанции',
        'description': 'КТПБ блочного типа 35/110/220 кВ, киосковые, мачтовые, блочные (БКТП), распределительные (РТП, РП) и мобильные модульные (ММПС) подстанции для сетей 6/10/20/0,4 кВ и до 220 кВ',
        'image': '/images/suppliers/moselectroshield/img1.png',
    },
    {
        'slug': 'oborudovanie-tp-do-500-kv',
        'name': 'Оборудование для ТП до 500 кВ',
        'title': 'Оборудование для трансформаторных подстанций до 500 кВ',
        'description': 'Элегазовые выключатели LTB/DTB 110–220 кВ, разъединители SDF и GW 110–500 кВ, измерительные трансформаторы тока и напряжения, вводы с RIP-изоляцией, шинные опоры, БСК/ФКУ и ОПН',
        'image': '/images/suppliers/energyh/vyklyuchateli.jpg',
    },
    {
        'slug': 'krue-110-500',
        'name': 'КРУЭ до 500 кВ',
        'title': 'Комплектные распределительные устройства элегазовые (КРУЭ)',
        'description': 'КРУЭ серии LZ на 110, 220, 330 и 500 кВ, КРУЭ-Моноблоки К-131-Э и К-134 «ПРИЗМА» для сетей 6/10/20 кВ',
        'image': '/images/suppliers/lzvo/krue.jpg',
    },
    {
        'slug': 'silovye-transformatory',
        'name': 'Трансформаторы до 220 кВ',
        'title': 'Силовые трансформаторы до 220 кВ',
        'description': 'Силовые масляные трансформаторы до 220 кВ, масляные ТМГ и сухие трансформаторы до 35 кВ, трансформаторы собственных нужд',
        'image': '/images/suppliers/moselectroshield/img2.png',
    },
    {
        'slug': 'kru-kso-6-35',
        'name': 'КРУ / КСО до 35 кВ',
        'title': 'Комплектные распределительные устройства (КРУ) до 35 кВ',
        'description': 'Ячейки КРУ (КСО) 6/10 кВ, КРУ 20 кВ и 35 кВ: КСО-298/366/393, серии К-125, К-128, К-129, К-133, К-130, К-131, дугогасящие устройства, ТСН и реклоузеры для сетей 6–35 кВ',
        'image': '/images/suppliers/moselectroshield/nku2.png',
    },
    {
        'slug': 'nku-vru-grshch',
        'name': 'РУ 0,4 кВ (НКУ / ВРУ / ГРЩ)',
        'title': 'Распределительные устройства 0,4 кВ',
        'description': 'Шкафы НКУ 0,4 кВ серии QUBE, ВРУ-1/2/3, главные распределительные щиты (ГРЩ), щиты освещения ЩО-70 и ОЩВ',
        'image': '/images/suppliers/moselectroshield/nku1.png',
    },
    {
        'slug': 'tokoprovody-shinoprovody',
        'name': 'Токопроводы и шинопроводы',
        'title': 'Токопроводы средневольтные и шинопроводы',
        'description': 'Токопроводы генераторного напряжения ТЭНЕ/ТЭНП, закрытые ТЗК/ТЗКР/ТЗКЭП, с литой изоляцией Betobar-r и ГИЛ 6–35 кВ, шинопроводы ШЗК и ЭФИБАР 0,4–1,2 кВ',
        'image': '/images/suppliers/moselectroshield/nku3.png',
    },
    {
        'slug': 'shkafy-avtomatiki-rza',
        'name': 'РЗА и автоматика',
        'title': 'Релейная защита и автоматика',
        'description': 'Продукция ООО НТЦ «Механотроника»: микропроцессорные устройства БМРЗ, шкафы РЗА ШЭ-МТ, дуговая защита ДУГА-МТ, БАВР/АВР, системы оперативного тока СОПТ-МТ, ШОТ-МТ, щиты переменного тока, панели АИИСКУЭ, ПО',
        'image': '/images/suppliers/mtrele/shkafy.jpg',
    },
    {
        'slug': 'sistemy-svyazi',
        'name': 'Собственное производство',
        'title': 'Собственное производство: связь, безопасность, электропитание',
        'description': 'Шкафы ВЧ-связи, ЦСПИ, внутриобъектовой связи, РРЛ, ВОЛС, информационная безопасность, видеонаблюдение, СКУД, бесперебойное гарантированное электропитание и автономное электроснабжение',
        'image': '/images/suppliers/energyh/svyaz.jpg',
    },
    {
        'slug': 'blokirovannye-zdaniya-bmz',
        'name': 'Блочно-модульные здания (БМЗ)',
        'title': 'Блочно-модульные здания и решения на их основе',
        'description': 'Блочно-модульные ЗРУ, КТП 6(10)/0,4 кВ, РТП 6(10)/0,4 кВ, НКУ и общеподстанционные пункты управления (ОПУ) полной заводской готовности',
        'image': '/images/suppliers/moselectroshield/bktp.png',
    },
]

# Какие прежние категории в какой новый раздел входят (порядок = порядок продуктов)
MERGE = {
    'ktp-bktp-rtp': ['ktp-bktp-rtp'],
    'oborudovanie-tp-do-500-kv': [
        'vysokovoltnye-vyklyuchateli', 'razediniteli-zazemliteli', 'izmeritelnye-transformatory',
        'vysokovoltnye-vvody', 'shinnye-opory', 'bsk-fku', 'opn-ogranichiteli',
    ],
    'krue-110-500': ['krue-110-500'],
    'silovye-transformatory': ['silovye-transformatory'],
    'kru-kso-6-35': ['kru-kso-6-35', 'reklouzery'],
    'nku-vru-grshch': ['nku-vru-grshch'],
    'tokoprovody-shinoprovody': ['tokoprovody-shinoprovody'],
    'shkafy-avtomatiki-rza': ['shkafy-avtomatiki-rza', 'shot-sopt'],
    'sistemy-svyazi': ['sistemy-svyazi', 'sistemy-bezopasnosti'],
    'blokirovannye-zdaniya-bmz': ['blokirovannye-zdaniya-bmz'],
}

new_products = {}
used = set()
for cat in CATEGORIES:
    slug = cat['slug']
    items = []
    for old_slug in MERGE[slug]:
        for p in old_prods.get(old_slug, []):
            p = dict(p)
            p['category'] = slug
            items.append(p)
            used.add((old_slug, p['slug']))
    new_products[slug] = items

# Страховка: продукты, не попавшие в маппинг
leftover = []
for old_slug, items in old_prods.items():
    for p in items:
        if (old_slug, p['slug']) not in used:
            leftover.append(f"{old_slug}/{p['slug']}")
if leftover:
    raise SystemExit('Продукты вне маппинга: ' + ', '.join(leftover))

data['categories'] = CATEGORIES
data['products'] = new_products

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Категорий:', len(CATEGORIES))
print('Продуктов:', sum(len(v) for v in new_products.values()))
for c in CATEGORIES:
    print(f"  {c['slug']}: {len(new_products[c['slug']])} шт.")
