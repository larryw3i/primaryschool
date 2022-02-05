

import importlib
import os

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.widgets import *

from primaryschool.locale import _
from primaryschool.resource import font_path
from primaryschool.subjects import list_subjects


class Menu():
    def __init__(self, win):

        self.win = win
        self.menu_theme = pygame_menu.themes.THEME_BLUE
        self.menu_theme.title_font = font_path

        self.menu = pygame_menu.Menu(
            _('Primary School'), win.w_width, win.w_height,
            theme=pygame_menu.themes.THEME_BLUE)
        self.menu_display = False

        self.menu_loop = False

    def set_widgets(self):

        self.menu.add.text_input(
            _('Name :'), default=_('_name_'),
            font_name=font_path)
        self.menu.add.dropselect(
            title=_('Subject :'),
            items=[(name, index) for index, name in enumerate(
                self.win.subjects_t)],
            font_name=font_path,
            default=self.win.subject_index,
            placeholder=_('Select an Subject'),
            onchange=self.set_subject
        )
        self.menu.add.dropselect(
            title=_('Difficulty :'),
            items=[(d, index) for index, d in enumerate(
                self.win.difficulties_t)],
            font_name=font_path,
            default=self.win.difficulty_index,
            placeholder=_('Select an difficulty'),
            onchange=self.set_difficulty
        )
        self.menu.add.button(
            _('Play'),
            self.win.start_the_game,
            font_name=font_path)
        self.menu.add.button(
            _('Quit'),
            pygame_menu.events.EXIT,
            font_name=font_path)

    def trigger(self):
        if not self.menu_loop:
            self.menu.mainloop(self.win.win)
            self.menu_loop = True
        else:
            self.menu.mainloop(self.win.win)
            self.menu_loop = False

    def set_difficulty(self, value, difficulty):
        self.win.difficulty_index = difficulty
        pass

    def set_subject(self, value, subject):
        self.win.subject_index = subject
        pass


class Win():
    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w_width, self.w_height = self.win.get_size()

        self.difficulty_index = 2
        self.subject_index = 2

        self.subjects_t, self.subjects = list_subjects()
        self.difficulties = ['Crazy', 'Hard', 'Middle', 'Easy']
        self.difficulties_t = [_(d) for d in self.difficulties]

        self.running = True

        self.menu = Menu(self)

    def render(self):
        self.win.fill((255, 255, 255))
        self.menu.set_widgets()

    def start_the_game(self):
        _subject = self.subjects[self.subject_index]
        _subject_ = importlib.import_module(
            'primaryschool.subjects.' + _subject)
        _subject_.start(self)
        pass

    def update(self):
        self.render()
        self.menu.trigger()
        pygame.display.update()
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.K_ESCAPE:
                    self.menu.trigger()


def go():
    Win().update()
    pass
