
import os
import sys

import pygame

from primaryschool import project_path
from primaryschool.locale import sys_lang_code

resource_path = os.path.abspath(os.path.dirname(__file__))

material_dir_names = ['imgs', 'audios', 'fonts']
material_filess = []
for root, _, files in os.walk(project_path, topdown=False):
    for n in material_dir_names:
        if root.endswith(n):
            for name in files:
                material_filess.append(os.path.join(root, name))

material_filess = sorted(material_filess, key=len)

_font_path = os.path.join(resource_path, 'fonts')
default_font_path = os.path.join(_font_path, 'NotoSansCJK-Light.ttc')

locale_fonts = {
    'zh_CN': default_font_path
}


def get_font_path():
    for k, v in locale_fonts.items():
        if sys_lang_code == k:
            return v
    return default_font_path


font_path = get_font_path()


def get_font(size=30):
    return pygame.font.Font(font_path, size)


def get_material(name):
    for f in material_filess:
        locale_material = f'{sys_lang_code}/{name}'
        if f.endswith(locale_material):
            return f
