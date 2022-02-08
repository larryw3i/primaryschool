import copy
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
from primaryschool.subjects.yuwen.words import cn_ps_c

name = _('pinyin missile')


pinyin = Pinyin()
default_font = get_font(50)


class Word():

    def __init__(self):
        pass

    def get_cn_ps_words(self, n: Tuple[int, int, int] = (0, 0, 0)):
        return cn_ps_c[n[0]][n[1]] if n[2] == 0 else zh_c[n[0]][n[1]][0:n[2]]

    def get_rand_word(self, n):
        return [chr(random.randint(0x4e00, 0x9fbf)) for i in range(0, n)]


class InputSurface():
    def __init__(self, win):
        self.win = win
        self.font = default_font
        self.font_color = (200, 22, 98)
        self.surface = None
        self.frame_counter = 0

    def _update(self):
        self.surface = self.font.render(
            self.win._input, False, self.font_color)

    def blit(self):
        if self.surface is None:
            return
        w, h = self.surface.get_size()
        self.win.surface.blit(
            self.surface,
            (self.win.w_width_of_2 - w / 2,
             self.win.w_height - h))


class WallSurface():
    def __init__(self, win):
        self.win = win
        self.h = self.win.w_height / 20
        self.surface = pygame.Surface((self.win.w_width, self.h))
        self.color = (255, 200, 99)

    def blit(self):
        self.surface.fill(self.color)
        self.win.surface.blit(self.surface, (0, self.win.w_height - self.h))


class WordSurfacesManager():
    def __init__(self, win, frame_counter=0):
        self.win = win
        self.surfaces = self.get_surfaces()
        self.count = self.count()
        self.moving_surfaces = []
        self.frame_counter = frame_counter
        self.interval = 1.2 * self.win.FPS
        self.moving_speed = 1

    def get_surfaces(self):
        assert len(self.win.words) > 0
        return [WordSurface(self.win, w) for w in self.win.words]

    def count(self):
        return len(self.surfaces)

    def get_random_surface(self):
        random_ws = self.surfaces[
            random.randint(0, self.count - 1)]
        return random_ws.copy()

    def blit(self):
        if self.frame_counter % self.interval == 0:
            ws = self.get_random_surface()
            self.moving_surfaces.append(ws)
            self.frame_counter = 0

        for w in self.moving_surfaces:
            w.add_dest((0, self.moving_speed))

            if w.arrived():
                self.moving_surfaces.remove(w)
                continue

            if w.intercept(self.win._input):
                self.win._input = ''
                self.win.input_surface._update()
                self.moving_surfaces.remove(w)
                continue

            self.win.surface.blit(w.surface, w.dest)

        self.frame_counter += 1


class WordSurface():
    def __init__(self, win, word):
        self.win = win
        self.word = word
        self.font = default_font
        self.font_color = (200, 22, 98)
        self.surface = self.get_surface()
        self.size = self.get_size()
        self.dest = self.get_random_dest()
        self.pinyin = self.get_pinyin()

    def arrived(self):
        return self.get_y() + self.get_h() >= \
            self.win.w_height - self.win.wall_surface.h

    def get_surface(self):
        return self.font.render(self.word, False, self.font_color)

    def set_dest(self, dest):
        self.dest = dest

    def get_x(self):
        return self.dest[0]

    def get_y(self):
        return self.dest[1]

    def get_w(self):
        return self.size[0]

    def get_h(self):
        return self.size[1]

    def add_dest(self, _add):
        self.dest[0] += _add[0]
        self.dest[1] += _add[1]

    def intercept(self, _pinyin):
        return _pinyin == self.pinyin

    def get_pinyin(self):
        return pinyin.get_pinyin(self.word, '')

    def get_size(self):
        return self.surface.get_size()

    def set_random_dest(self):
        self.dest = self.get_random_dest()

    def get_random_dest(self):
        return [random.randint(0, self.win.w_width - self.get_w()), 0]

    def copy(self):
        _new = copy.copy(self)
        _new.surface = self.surface.copy()
        _new.set_random_dest()
        return _new


class PinyinMissile(SubjectGame):
    def __init__(self, win):
        super().__init__(win)
        self.win = win

        # window
        self.w_width = self.win.w_width
        self.w_height = self.win.w_height
        self.w_height_of_2 = self.win.w_height_of_2
        self.w_width_of_2 = self.win.w_width_of_2
        self.running = True
        self.FPS = self.win.FPS
        self.clock = self.win.clock

        self.main_menu = self.win.main_menu

        self.surface = self.win.surface

        self.wall_surface = WallSurface(self)

        self._input = ''
        self.input_surface = InputSurface(self)

        # word surface
        self.word = Word()
        self.words = self.word.get_cn_ps_words((5, 0, 0))
        self.wordsurfaces_manager = WordSurfacesManager(self)
        self.word_surfaces = self.wordsurfaces_manager.get_surfaces()

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
                    self.input_surface._update()
                    return
                elif self.ascii_not_symbol(e.key):
                    self._input += pygame.key.name(e.key)
                    self.input_surface._update()
                    return

    def run(self):

        while self.running:
            self.clock.tick(self.FPS)

            self.surface.fill((0, 0, 0))

            events = pygame.event.get()
            self.handle_events(events)
            if self.main_menu._menu.is_enabled():
                self.main_menu._menu.update(events)

            self.wall_surface.blit()
            self.wordsurfaces_manager.blit()
            self.input_surface.blit()

            pygame.display.flip()


def play(win):
    PinyinMissile(win).run()
    pass
