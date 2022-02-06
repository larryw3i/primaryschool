
import os
import random
import sys

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu._widgetmanager import WidgetManager
from pygame_menu.widgets import *
from xpinyin import Pinyin

from primaryschool.locale import _
from primaryschool.subjects import *

name = _('Yuwen')


class YuwenGame(SubjectGame):
    def __init__(self, win):
        super().__init__(win)
        self.win = win
        self.menu = self.win.menu._menu
        self.menu.set_title(_('Yuwen'))
        self.menu.clear()

        self.s_width, self.s_height = self.menu.get_size(inner=True)
        self.surface = pygame.Surface((self.s_width, self.s_height))
        self.surface.fill((0, 0, 255))

        self.p = Pinyin()

        self.menu.add.surface(self.surface, border_width=0, padding=(0, 0))

    def get_pinyin(self, zh_str):
        return self.p.get_pinyin(zh_str, '')

    def get_rand_zh_str(self, n):
        return [chr(random.randint(0x4e00, 0x9fbf)) for i in range(0, n)]

    def get_rand_by_grade(self, n):
        pass


def start(win):
    YuwenGame(win)
    pass
