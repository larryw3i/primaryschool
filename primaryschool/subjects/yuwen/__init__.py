
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
        self.main_menu = self.win.main_menu

        self.surface = self.win.surface
        self.running = True

        self.run()

    def get_pinyin(self, zh_str):
        return self.p.get_pinyin(zh_str, '')

    def get_rand_zh_str(self, n):
        return [chr(random.randint(0x4e00, 0x9fbf)) for i in range(0, n)]

    def get_rand_by_grade(self, n):
        pass

    def run(self):

        while self.running:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.main_menu._menu.enable()
                        return
            if self.main_menu._menu.is_enabled():
                self.main_menu._menu.update(events)
            self.surface.fill((0, 0, 0))
            pygame.display.flip()


def start(win):
    YuwenGame(win)
    pass
