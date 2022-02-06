
import os
import random
import sys
from typing import Any, List, Optional, Sequence, Text, Tuple, Union, overload

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu._widgetmanager import WidgetManager
from pygame_menu.widgets import *
from xpinyin import Pinyin

from primaryschool.locale import _
from primaryschool.resource import font_path, get_font
from primaryschool.subjects import *
from primaryschool.subjects.yuwen.words import c as zh_c

name = _('Yuwen')


class YuwenGame(SubjectGame):
    def __init__(self, win):
        super().__init__(win)
        self.win = win
        self.main_menu = self.win.main_menu

        self.surface = self.win.surface
        self.running = self.win.running
        self.FPS = self.win.FPS
        self.clock = self.win.clock

        # window
        self.w_width = self.win.w_width
        self.w_height = self.win.w_height

        self.m_speed = 1/self.w_height

        # word surface
        self.ws_interval = 1.2 * self.FPS
        self.ws_font = get_font(50)
        self.words = self.get_w_by_index((5, 0, 0))
        self.ws = self.get_word_surfaces()
        self.ws_len = len(self.get_word_surfaces())
        self.m_ws = []
        self.m_ws_rects = []

        self.frame_counter = 0

        self.run()
        print("A")

    def get_word_surfaces(self):
        f_color = (255, 255, 255)
        return [
            f for f in [
                self.ws_font.render(w, True, f_color) for w in self.words
            ]
        ]

    def get_pinyin(self, zh_str):
        return self.p.get_pinyin(zh_str, '')

    def get_rand_w(self, n):
        return [chr(random.randint(0x4e00, 0x9fbf)) for i in range(0, n)]

    def get_w_by_index(self, n: Tuple[int, int, int] = (0, 0, 0)):
        return zh_c[n[0]][n[1]] if n[2] == 0 else zh_c[n[0]][n[1]][0:n[2]]

    def run(self):

        while self.running:
            self.clock.tick(self.FPS)
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

            self.surface.fill((0,0,0))

            if self.frame_counter >= self.ws_interval:
                w = self.ws[random.randint(0, self.ws_len-1)]
                rect = w.get_rect()
                rect.x= random.randint(0, self.w_width)
                rect.y= 1
                self.m_ws.append(w)
                self.m_ws_rects.append(rect)

                self.surface.blit(w, rect)

                self.frame_counter = 0
            index = 0
            for s in self.m_ws:
                rect = self.m_ws_rects[index]
                rect.y +=3
                self.surface.blit(s,rect)
                index +=1


            self.frame_counter += 1

            pygame.display.flip()


def start(win):
    YuwenGame(win)
    pass
