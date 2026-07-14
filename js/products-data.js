const PRODUCTS = {
  "ktp-bktp-rtp": [
    {
      slug: "bktp-40-3150",
      name: "БКТП 40–3150 кВА",
      category: "ktp-bktp-rtp",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/bktp.png",
      description: "Комплектные трансформаторные подстанции в бетонном корпусе мощностью от 40 до 3150 кВА для сетей 6/10/20/0,4 кВ. Полная заводская готовность, модульный принцип, срок службы более 25 лет.",
      specs: [
        { param: "Мощность, кВА", value: "40 – 3150" },
        { param: "Напряжение ВН, кВ", value: "6; 10; 20" },
        { param: "Напряжение НН, кВ", value: "0,4" },
        { param: "Ток сборных шин НН, А", value: "до 6300" },
      ],
      advantages: [
        "Полная заводская готовность",
        "Модульный принцип",
        "Возможность применения сухих и масляных трансформаторов",
      ],
      applications: [
        "Промышленность",
        "ЖКХ",
        "Нефтегаз",
        "Коттеджные посёлки",
      ]
    },
    {
      slug: "rtp-rp-400-3150",
      name: "РТП / РП 400–3150 кВА",
      category: "ktp-bktp-rtp",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/rtp.png",
      description: "Распределительные трансформаторные подстанции и распределительные пункты в блочном исполнении для приёма и распределения электроэнергии 6–20 кВ.",
      specs: [
        { param: "Мощность, кВА", value: "400 – 3150" },
        { param: "Напряжение, кВ", value: "6/10/20" },
        { param: "Ток сборных шин НН, А", value: "160 – 6300" },
      ],
      advantages: [
        "Полная заводская готовность",
        "Сокращение сроков монтажа",
        "Высокая надёжность",
      ],
      applications: [
        "Промышленные объекты",
        "ЖКХ",
        "Нефтегаз",
      ]
    },
    {
      slug: "mmps-do-220-kv",
      name: "ММПС до 220 кВ",
      category: "ktp-bktp-rtp",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/mmps.png",
      description: "Мобильные модульные подстанции в контейнерном исполнении для быстрого развёртывания энергообъектов. 1- и 2-трансформаторные ПС 220/110/35 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "до 220" },
        { param: "Исполнение", value: "контейнерное" },
      ],
      advantages: [
        "Быстрый монтаж",
        "Мобильность",
        "Максимальная заводская готовность",
      ],
      applications: [
        "Аварийное электроснабжение",
        "Временные схемы",
        "Реконструкция ПС",
      ]
    },
    {
      slug: "ktp-kioskovye",
      name: "Киосковые КТП",
      category: "ktp-bktp-rtp",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/img1.png",
      description: "Киосковые подстанции для открытых площадок и специальных помещений. Мощность от 25 до 2500 кВА.",
      specs: [
        { param: "Мощность, кВА", value: "25 – 2500" },
        { param: "Напряжение ВН, кВ", value: "6; 10" },
      ],
      advantages: [
        "Универсальность установки",
        "Широкий диапазон мощностей",
      ],
      applications: [
        "Промышленность",
        "Жилые микрорайоны",
      ]
    },
    {
      slug: "ktp-machtovye",
      name: "Мачтовые КТП",
      category: "ktp-bktp-rtp",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/img1.png",
      description: "Мачтовые подстанции для установки на опорных столбах. Мощность от 25 до 250 кВА.",
      specs: [
        { param: "Мощность, кВА", value: "25 – 250" },
        { param: "Напряжение ВН, кВ", value: "6; 10" },
      ],
      advantages: [
        "Компактные габариты",
        "Быстрый монтаж",
      ],
      applications: [
        "Сельские населённые пункты",
        "Насосные станции",
      ]
    }
  ],
  "kru-kso-6-35": [
    {
      slug: "kso-298",
      name: "КСО-298",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Классическая серия камер сборных одностороннего обслуживания с масляными или вакуумными выключателями для подстанций 6–10 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10" },
        { param: "Номинальный ток, А", value: "до 1000" },
        { param: "Ток отключения, кА", value: "до 20" },
      ],
      advantages: [
        "Проверенная конструкция",
        "Возможность модернизации",
      ],
      applications: [
        "Подстанции 6–10 кВ",
      ]
    },
    {
      slug: "kso-366",
      name: "КСО-366",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Модернизированная серия камер с улучшенными характеристиками для подстанций 6–10 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10" },
        { param: "Номинальный ток, А", value: "до 1250" },
        { param: "Ток отключения, кА", value: "до 31,5" },
      ],
      advantages: [
        "Увеличенный ток отключения",
        "Компактные габариты",
      ],
      applications: [
        "Реконструкция",
      ]
    },
    {
      slug: "kso-393",
      name: "КСО-393",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Современная серия камер с вакуумными выключателями и микропроцессорной защитой.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10" },
        { param: "Номинальный ток, А", value: "до 1600" },
      ],
      advantages: [
        "Поддержка IEC 61850",
        "Интеграция в АСУ ТП",
      ],
      applications: [
        "Современные подстанции",
      ]
    },
    {
      slug: "kru-k125",
      name: "КРУ К-125 «Трансформер»",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Ячейки с воздушной изоляцией для подстанций 6–10 кВ. Классическая серия с масляными или вакуумными выключателями.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10" },
      ],
      advantages: [
        "Проверенная конструкция",
        "Простота ремонта",
      ],
      applications: [
        "Подстанции 6–10 кВ",
      ]
    },
    {
      slug: "kru-k128",
      name: "КРУ К-128 «Классик»",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Ячейки с улучшенными характеристиками для подстанций 6–10 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10" },
        { param: "Номинальный ток, А", value: "до 1250" },
      ],
      advantages: [
        "Компактные габариты",
        "Современная защита",
      ],
      applications: [
        "Подстанции",
      ]
    },
    {
      slug: "kru-k129",
      name: "КРУ К-129 «Оптима» / «Новатор»",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Оптимальное соотношение цены и качества для подстанций 6–10 кВ. «Новатор» — компактная замена КСО-2001.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10" },
        { param: "Номинальный ток, А", value: "до 1600" },
      ],
      advantages: [
        "Надёжность",
        "Простота обслуживания",
        "Компактные габариты",
      ],
      applications: [
        "Подстанции",
        "Промышленность",
      ]
    },
    {
      slug: "kru-k133",
      name: "КРУ К-133 «Компакт»",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Шкафы с твёрдой изоляцией для подстанций 6–10 кВ. Минимальные габариты, отсутствие масла.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10" },
        { param: "Изоляция", value: "твёрдая" },
      ],
      advantages: [
        "Экологичность",
        "Минимальное обслуживание",
      ],
      applications: [
        "Подстанции с ограниченным пространством",
      ]
    },
    {
      slug: "kru-k131-20-kv",
      name: "КРУ К-131 «Прогресс» 20 кВ",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Комплектные распределительные устройства для сетей 20 кВ с отечественными вакуумными выключателями.",
      specs: [
        { param: "Напряжение, кВ", value: "20" },
        { param: "Номинальный ток, А", value: "630 – 2500" },
      ],
      advantages: [
        "Сейсмостойкость до 9 баллов",
        "Возможность применения ВВ BB/TEL-20",
      ],
      applications: [
        "Энергетика",
        "Транспорт",
      ]
    },
    {
      slug: "kru-k130-35-kv",
      name: "КРУ К-130 «Гарант» 35 кВ",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Шкафы для приёма и распределения электроэнергии в сетях 35 кВ. Жёсткая металлическая конструкция, модульная сборка.",
      specs: [
        { param: "Напряжение, кВ", value: "35" },
        { param: "Номинальный ток, А", value: "до 1600" },
      ],
      advantages: [
        "Выкатные элементы",
        "Визуальный контроль положения",
      ],
      applications: [
        "Подстанции 220/35/6(10)",
        "Распределительные пункты 35 кВ",
      ]
    },
    {
      slug: "dugogasyashchie-ustroystva",
      name: "Дугогасящие устройства",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/img2.png",
      description: "Дугогасящие реакторы и устройства компенсации ёмкостного тока однофазного замыкания на землю в сетях 6–35 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "6 – 35" },
        { param: "Регулирование", value: "Плавное / ступенчатое" },
      ],
      advantages: [
        "Снижение токов КЗ",
        "Повышение надёжности",
        "Автоматический подбор режима",
      ],
      applications: [
        "Сети 6–35 кВ",
        "Подстанции",
        "Распределительные устройства",
      ]
    },
    {
      slug: "transformatory-sobstvennyx-nuzhd",
      name: "Трансформаторы собственных нужд",
      category: "kru-kso-6-35",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/img2.png",
      description: "Трансформаторы собственных нужд (ТСН) для питания вспомогательных цепей подстанций и распределительных устройств 6–35 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "6 / 10 / 35" },
        { param: "Мощность, кВА", value: "25 – 2500" },
      ],
      advantages: [
        "Компактность",
        "Высокая надёжность",
        "Соответствие ГОСТ",
      ],
      applications: [
        "Подстанции",
        "РП",
        "Энергообъекты",
      ]
    }
  ],
  "krue-110-500": [
    {
      slug: "krue-lz-110",
      name: "КРУЭ-LZ 110",
      category: "krue-110-500",
      brand: "ЛЗВО",
      image: "/images/suppliers/lzvo/krue.jpg",
      description: "Комплектное распределительное устройство с элегазовой изоляцией на номинальное напряжение 110 кВ.",
      specs: [
        { param: "Номинальное напряжение, кВ", value: "110" },
        { param: "Ток КЗ, кА", value: "40/50" },
        { param: "Номинальный ток, А", value: "2000/3150/4000" },
      ],
      advantages: [
        "Элегазовая изоляция",
        "Высокая надёжность",
        "Контейнерное исполнение",
      ],
      applications: [
        "Подстанции 110 кВ",
      ]
    },
    {
      slug: "krue-lz-220",
      name: "КРУЭ-LZ 220",
      category: "krue-110-500",
      brand: "ЛЗВО",
      image: "/images/suppliers/lzvo/krue.jpg",
      description: "КРУЭ на номинальное напряжение 220 кВ. Трёхфазное и однофазное исполнение.",
      specs: [
        { param: "Номинальное напряжение, кВ", value: "220" },
        { param: "Ток КЗ, кА", value: "50/63" },
        { param: "Номинальный ток, А", value: "3150/4000/5000/6000" },
      ],
      advantages: [
        "Высокие токи КЗ",
        "Гибкость исполнения",
      ],
      applications: [
        "Подстанции 220 кВ",
      ]
    },
    {
      slug: "krue-lz-330",
      name: "КРУЭ-LZ 330",
      category: "krue-110-500",
      brand: "ЛЗВО",
      image: "/images/suppliers/lzvo/krue.jpg",
      description: "КРУЭ на номинальное напряжение 330 кВ. Однофазное исполнение для внутренней установки.",
      specs: [
        { param: "Номинальное напряжение, кВ", value: "330" },
        { param: "Ток КЗ, кА", value: "50/63" },
      ],
      advantages: [
        "Однофазное исполнение",
        "Внутренняя установка",
      ],
      applications: [
        "Подстанции 330 кВ",
      ]
    },
    {
      slug: "krue-lz-500",
      name: "КРУЭ-LZ 500",
      category: "krue-110-500",
      brand: "ЛЗВО",
      image: "/images/suppliers/lzvo/krue.jpg",
      description: "КРУЭ на номинальное напряжение 500 кВ. Однофазное исполнение для внутренней установки.",
      specs: [
        { param: "Номинальное напряжение, кВ", value: "500" },
        { param: "Ток КЗ, кА", value: "63/80" },
        { param: "Номинальный ток, А", value: "4000/5000/6300" },
      ],
      advantages: [
        "Высокий ток КЗ до 80 кА",
        "Собственные компоненты",
      ],
      applications: [
        "Магистральные подстанции 500 кВ",
      ]
    },
    {
      slug: "monoblok-k131-e",
      name: "КРУЭ-Моноблок К-131-Э",
      category: "krue-110-500",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "Компактное элегазовое устройство для сетей 6/10/20 кВ. Номинальный ток 630 А.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10; 20" },
        { param: "Номинальный ток, А", value: "630" },
      ],
      advantages: [
        "Расширяемые конфигурации",
        "Не требует закачки элегаза",
      ],
      applications: [
        "Радиальные и магистральные сети",
      ]
    },
    {
      slug: "monoblok-k134-prizma",
      name: "КРУЭ-Моноблок К-134 «ПРИЗМА»",
      category: "krue-110-500",
      brand: "Мосэлектрощит",
      image: "/images/suppliers/moselectroshield/nku2.png",
      description: "КРУЭ с элегазовой изоляцией для сетей 6/10/20 кВ с вакуумным выключателем.",
      specs: [
        { param: "Напряжение, кВ", value: "6; 10; 20" },
        { param: "Номинальный ток, А", value: "630" },
      ],
      advantages: [
        "Вакуумный выключатель",
        "Срок службы 30 лет",
      ],
      applications: [
        "Вторичное распределение",
      ]
    }
  ],
  "vysokovoltnye-vyklyuchateli": [
    {
      slug: "ltb-110-220",
      name: "Высоковольтные выключатели LTB",
      category: "vysokovoltnye-vyklyuchateli",
      brand: "Energy-H",
      image: "/images/suppliers/energyh/vyklyuchateli.jpg",
      description: "Колонковые элегазовые выключатели серии LTB для сетей 110–220 кВ. Время отключения не более 50 мс.",
      specs: [
        { param: "Напряжение, кВ", value: "110 – 220" },
        { param: "Стандарт", value: "ГОСТ Р 52565-2006" },
        { param: "Время отключения, мс", value: "≤ 50" },
      ],
      advantages: [
        "Надёжная коммутация",
        "Минимум повторных пробоев",
        "Пружинные приводы",
      ],
      applications: [
        "Цепи трансформаторов",
        "Линии",
        "Конденсаторные батареи",
        "Шунтирующие реакторы",
      ]
    },
    {
      slug: "dtb-110-220",
      name: "Высоковольтные выключатели DTB",
      category: "vysokovoltnye-vyklyuchateli",
      brand: "Energy-H",
      image: "/images/suppliers/energyh/vyklyuchateli.jpg",
      description: "Баковые элегазовые выключатели серии DTB для сетей 110–220 кВ с пружинно-гидравлическими приводами.",
      specs: [
        { param: "Напряжение, кВ", value: "110 – 220" },
        { param: "Привод", value: "пружинно-гидравлический" },
      ],
      advantages: [
        "Баковое исполнение",
        "Минимальное обслуживание",
      ],
      applications: [
        "Цепи трансформаторов",
        "Линии",
        "Конденсаторные батареи",
      ]
    }
  ],
  "razediniteli-zazemliteli": [
    {
      slug: "sdf-110-500",
      name: "Разъединители SDF",
      category: "razediniteli-zazemliteli",
      brand: "Energy-H",
      image: "/images/suppliers/energyh/razediniteli.jpg",
      description: "Горизонтально-поворотные разъединители типа SDF для сетей 110–500 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "110 – 500" },
        { param: "Номинальный ток, А", value: "до 4000" },
      ],
      advantages: [
        "Сварные алюминиевые токопроводы",
        "Блокировка «мёртвой точки»",
        "Работа при обледенении до 20 мм",
      ],
      applications: [
        "ОРУ 110–500 кВ",
      ]
    },
    {
      slug: "gw-330-500",
      name: "Полупантографные разъединители GW",
      category: "razediniteli-zazemliteli",
      brand: "Energy-H",
      image: "/images/suppliers/energyh/razediniteli.jpg",
      description: "Полупантографные разъединители типа GW для сетей 330–500 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "330 – 500" },
        { param: "Номинальный ток, А", value: "4000" },
      ],
      advantages: [
        "Компактная пантографная схема",
        "Высокая механическая прочность",
      ],
      applications: [
        "ОРУ 330–500 кВ",
      ]
    }
  ],
  "izmeritelnye-transformatory": [
    {
      slug: "tt-tg",
      name: "Трансформаторы тока TG",
      category: "izmeritelnye-transformatory",
      brand: "Energy-H",
      image: "/images/suppliers/energyh/transformatory.jpg",
      description: "Элегазовые измерительные трансформаторы тока серии TG для сетей 110–220 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "110 – 220" },
        { param: "Первичный ток, А", value: "5 – 3000" },
        { param: "Вторичный ток, А", value: "1 / 5" },
      ],
      advantages: [
        "Элегазовая изоляция",
        "Взрывобезопасность",
        "Не требуют обслуживания",
      ],
      applications: [
        "Подстанции 110–220 кВ",
      ]
    },
    {
      slug: "tn-tng",
      name: "Трансформаторы напряжения ТНГ",
      category: "izmeritelnye-transformatory",
      brand: "Energy-H",
      image: "/images/suppliers/energyh/transformatory.jpg",
      description: "Элегазовые измерительные трансформаторы напряжения серии ТНГ для сетей 110–220 кВ.",
      specs: [
        { param: "Напряжение, кВ", value: "110 – 220" },
        { param: "Частота, Гц", value: "50" },
      ],
      advantages: [
        "Сухая изоляция",
        "Взрывобезопасность",
        "Минимальное обслуживание",
      ],
      applications: [
        "Подстанции 110–220 кВ",
      ]
    }
  ],
};

function getCategory(slug) { return CATEGORIES.find(c => c.slug === slug); }
function getProductsByCategory(slug) { return PRODUCTS[slug] || []; }
function getProduct(category, slug) { return (PRODUCTS[category] || []).find(p => p.slug === slug); }
function getAllProducts() { return Object.values(PRODUCTS).flat(); }
function generateBreadcrumb(items) { return items.map((item, i) => i === items.length - 1 ? `<span>${item.name}</span>` : `<a href="${item.url}">${item.name}</a>`).join(' <span>/</span> '); }
if (typeof module !== 'undefined' && module.exports) { module.exports = { CATEGORIES, PRODUCTS, getCategory, getProductsByCategory, getProduct, getAllProducts }; }