#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вшивает components/header.html и components/footer.html во все страницы сайта.

Запускать после любой правки шапки или подвала: python scripts/inline_components.py
Повторный запуск безопасен — содержимое между маркерами просто заменяется.
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPONENTS = {'site-header': 'header', 'site-footer': 'footer'}
SKIP_DIRS = {'.git', '.claude', 'components', 'scripts', 'images', 'fonts', 'docs', 'инфа', 'фото для каталога'}


def load_component(name):
    with open(os.path.join(BASE_DIR, 'components', f'{name}.html'), encoding='utf-8') as f:
        return f.read().strip()


def inline_components(html):
    for container_id, name in COMPONENTS.items():
        pattern = re.compile(
            rf'<div id="{container_id}">(?:<!--inc:{name}-->.*?<!--/inc:{name}-->)?</div>', re.S)
        block = f'<div id="{container_id}"><!--inc:{name}-->\n{load_component(name)}\n<!--/inc:{name}--></div>'
        html = pattern.sub(lambda _: block, html, count=1)
    return html


def main():
    changed = 0
    for dirpath, dirnames, filenames in os.walk(BASE_DIR):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            if not filename.endswith('.html'):
                continue
            path = os.path.join(dirpath, filename)
            with open(path, encoding='utf-8', newline='') as f:
                raw = f.read()
            newline = '\r\n' if '\r\n' in raw else '\n'
            result = inline_components(raw.replace('\r\n', '\n')).replace('\n', newline)
            if result != raw:
                with open(path, 'w', encoding='utf-8', newline='') as f:
                    f.write(result)
                changed += 1
    print(f'Components inlined, pages updated: {changed}')


if __name__ == '__main__':
    main()
