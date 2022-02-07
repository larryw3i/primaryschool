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
import copy
from primaryschool.subjects.yuwen.words import c as zh_c

name = _('pinyin missile')


class WordSurface():
    def __init__(self, word, surface, dest=(0, 0), pinyin=''):
        self.word = word
        self.surface = surface
        self.dest = dest
        self.pinyin = pinyin

    def set_dest(self, dest):
        self.dest = dest
    
    def get_w(self):
        return self.dest[0]

    def get_h(self):
        return self.dest[1]

    def add_dest(self, _add):
        self.dest[0] += _add[0]
        self.dest[1] += _add[1]

    def compare_pinyin(self, _pinyin):
        return _pinyin == self.pinyin
        
    def copy(self):
        new_word_surface = copy.copy(self)
        new_word_surface.surface = self.surface.copy()
        return new_word_surface


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
        self.p=Pinyin()

        self.surface = self.win.surface
        self.wall_surface = pygame.Surface((self.w_width, self.w_height / 20))
        self.wall_surface_size = self.wall_surface.get_size()

        self.running = True
        self.FPS = self.win.FPS
        self.clock = self.win.clock

        self._input = ''
        self.input_font = get_font(50)
        self.input_font_color = (200, 22, 98)
        self.input_surface = self.input_font.render(
            '', 1, self.input_font_color)

        self.m_speed = 1

        self.scale_size = 1.5

        # word surface
        self.word_surface_interval = 1.2 * self.FPS
        self.word_surface_font = get_font(50)
        self.word_surface_font_color = (255, 255, 255)
        self.words = self.get_w_by_index((5, 0, 0))
        self.word_surfaces = self.get_word_surfaces()
        self.word_surfaces_len = len(self.word_surfaces)
        self.used_word_surfaces = []

        self.frame_counter = 0

        self.run()

    def get_random_word_surface_dest(self,word_surface):
        w,_ = word_surface.get_size()
        return [random.randint(0, self.w_width - w), 0]

    def get_word_surfaces(self):
        word_surfaces=[]
        for w in self.words:
            _surface = self.word_surface_font.render(
                w, True, self.word_surface_font_color)
            dest = self.get_random_word_surface_dest(_surface)
            pinyin = self.get_pinyin(w)
            word_surfaces.append(
                WordSurface(w, _surface, dest, pinyin))
        return word_surfaces

    def get_pinyin(self, zh_str):
        return self.p.get_pinyin(zh_str, '')
    
    def get_rand_word(self, n):
        return [chr(random.randint(0x4e00, 0x9fbf)) for i in range(0, n)]

    def get_w_by_index(self, n: Tuple[int, int, int] = (0, 0, 0)):
        return zh_c[n[0]][n[1]] if n[2] == 0 else zh_c[n[0]][n[1]][0:n[2]]
    
    def get_random_word_surface(self):
        random_ws = self.word_surfaces[
            random.randint(0, self.word_surfaces_len - 1)]
        _random_ws = random_ws.copy()
        _random_ws.set_dest(\
        self.get_random_word_surface_dest(_random_ws.surface))
        return _random_ws

    def update_word_surface(self):
        if self.frame_counter >= self.word_surface_interval:
            ws = self.get_random_word_surface()
            self.used_word_surfaces.append(ws)
            self.frame_counter = 0

        for w in self.used_word_surfaces:
            w.add_dest((0, self.m_speed))
            _,h = w.surface.get_size()

            if w.get_h() + h >= self.w_height:
                self.used_word_surfaces.remove(w)
                continue

            if w.pinyin == self._input:
                self._input = ''
                self._update_input()
                self.used_word_surfaces.remove(w)
                continue

            self.surface.blit(w.surface, w.dest)

        self.frame_counter += 1

    def update_wall(self):
        self.wall_surface.fill((255, 200, 99))
        self.surface.blit(self.wall_surface,
                          (0, self.w_height - self.wall_surface_size[1]))

    def _update_input(self, _input=''):
        self._input += _input
        self.input_surface = self.input_font.render(
            self._input, True, self.input_font_color)

    def update_input(self):
        w,h = self.input_surface.get_size()
        self.surface.blit(
            self.input_surface,
            (self.w_width_of_2 - w / 2,
             self.w_height - h))

    def ascii_not_symbol(self, code):
        return 48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.main_menu._menu.enable()
                    self.running = not self.running
                    return
                elif e.key == pygame.K_BACKSPACE:
                    self._input = self._input[0:-1]
                    self._update_input()
                    return
                elif self.ascii_not_symbol(e.key):
                    self._update_input(pygame.key.name(e.key))
                    return

    def run(self):

        while self.running:
            self.clock.tick(self.FPS)

            self.surface.fill((0, 0, 0))

            events = pygame.event.get()
            self.handle_events(events)
            if self.main_menu._menu.is_enabled():
                self.main_menu._menu.update(events)
                
            self.update_wall()
            self.update_word_surface()


            self.update_input()

            pygame.display.flip()


def play(win):
    PinyinMissile(win)
    pass
