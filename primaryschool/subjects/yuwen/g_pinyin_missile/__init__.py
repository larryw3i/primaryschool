import os
import random
import sys
from typing import Any, List, Optional, Sequence, Text, Tuple, Union, overload

import pygame
import pygame_menu
from pygame.key import key_code
from pygame.locals import *
from pygame_menu._widgetmanager import WidgetManager
from pygame_menu.widgets import *
from xpinyin import Pinyin

from primaryschool.locale import _
from primaryschool.resource import font_path, get_font
from primaryschool.subjects import *
from primaryschool.subjects.yuwen.words import c as zh_c

name = _('pinyin missile')


class WordSurface():
    def __init__(self, surface, dest):
        self.surface = surface
        self.dest = dest
        self.pinyin

    def set_dest(self, dest):
        self.dest = dest

    def add_dest(self, _add):
        self.dest[0] += _add[0]
        self.dest[1] += _add[1]


class PinyinMissile(SubjectGame):
    def __init__(self, win):
        super().__init__(win)
        self.win = win

        # window
        self.w_width = self.win.w_width
        self.w_width_of_2 = self.win.w_width / 2
        self.w_height = self.win.w_height
        self.w_height_of_2 = self.win.w_height / 2

        self.main_menu = self.win.main_menu

        self.surface = self.win.surface
        self.wall_surface = pygame.Surface((self.w_width, self.w_height / 20))
        self.wall_surface_size = self.wall_surface.get_size()

        self.running = self.win.running
        self.FPS = self.win.FPS
        self.clock = self.win.clock

        self.input = ''
        self.input_font = get_font(25)
        self.input_font_color = (200, 22, 98)
        self.input_surface = self.input_font.render(
            _('input pinyin'), True, self.input_font_color)

        self.m_speed = 1

        self.scale_size = 1.5

        # word surface
        self.ws_interval = 1.2 * self.FPS
        self.ws_font = get_font(50)
        self.words = self.get_w_by_index((5, 0, 0))
        self.ws = self.get_word_surfaces()
        self.ws_len = len(self.get_word_surfaces())
        self.m_ws = []

        self.frame_counter = 0

        self.run()

    def get_word_surfaces(self) -> List[pygame.Surface]:
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

    def update_ws(self):
        if self.frame_counter >= self.ws_interval:
            w = self.ws[random.randint(0, self.ws_len - 1)]
            size = w.get_size()
            dest = [
                random.randint(0, self.w_width - size[0]), 0]

            self.m_ws.append(WordSurface(w, dest))
            self.surface.blit(w, dest)

            self.frame_counter = 0

        for w in self.m_ws:
            w.add_dest((0, self.m_speed))
            size = w.surface.get_size()

            if w.dest[1] + size[1] >= self.w_height:
                self.m_ws.remove(w)
                continue

            self.surface.blit(w.surface, w.dest)

        self.frame_counter += 1

    def update_wall(self):
        self.wall_surface.fill((255, 200, 99))
        self.surface.blit(self.wall_surface,
                          (0, self.w_height - self.wall_surface_size[1]))

    def _update_input(self, _input):
        self.input += _input
        self.input_surface = self.input_font.render(
            self.input, True, self.input_font_color)

    def update_input_blit(self):
        size = self.wall_surface.get_size()
        self.surface.blit(
            self.input_surface,
            (self.w_width_of_2 - size[0] / 2,
             self.w_height - size[1]))
    
    def ascii_not_symbol(self,code):
        return 48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122
    
    def 

    def run(self):

        while self.running:
            self.clock.tick(self.FPS)

            self.surface.fill((0, 0, 0))
            self.update_wall()
            self.update_ws()

            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.main_menu._menu.enable()
                        return
                    if self.ascii_not_symbol(e.key):
                        self._update_input(pygame.key.name(e.key))

            if self.main_menu._menu.is_enabled():
                self.main_menu._menu.update(events)

            self.update_input_blit()

            pygame.display.flip()


def play(win):
    PinyinMissile(win)
    pass
