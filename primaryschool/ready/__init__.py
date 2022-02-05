

import importlib
import os

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.widgets import *

from primaryschool.locale import _
from primaryschool.resource import font_path
from primaryschool.subjects import list_subjects


class Menu(pygame_menu.Menu):
    def __init__(self, win):
        self.win = win
        self.menu_theme = pygame_menu.themes.THEME_BLUE
        self.menu_theme.title_font = font_path
        self.title = _('Primary School')


        super().__init__(self.title,self.win.w_width, self.win.w_height,
            theme=self.menu_theme,
            onclose=pygame_menu.events.BACK)
        
        self.add_widgets()
    
    def add_widgets(self):
        self.add.text_input(
            _('Name :'), default=_('_name_'),
            font_name=font_path)
        self.add.dropselect(
            title=_('Subject :'),
            items=[(name, index) for index, name in enumerate(
                self.win.subjects_t)],
            font_name=font_path,
            default=self.win.subject_index,
            placeholder=_('Select an Subject'),
            onchange=self.set_subject
        )
        self.add.dropselect(
            title=_('Difficulty :'),
            items=[(d, index) for index, d in enumerate(
                self.win.difficulties_t)],
            font_name=font_path,
            default=self.win.difficulty_index,
            placeholder=_('Select an difficulty'),
            onchange=self.set_difficulty
        )
        self.add.button(
            _('Play'),
            self.win.start_the_game,
            font_name=font_path)
        self.add.button(
            _('Quit'),
            pygame_menu.events.EXIT,
            font_name=font_path)
    


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

        self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w_width, self.w_height = self.surface.get_size()

        self.difficulty_index = 2
        self.subject_index = 0

        self.subjects_t, self.subjects = list_subjects()
        self.difficulties = ['Crazy', 'Hard', 'Middle', 'Easy']
        self.difficulties_t = [_(d) for d in self.difficulties]

        self.menu = Menu(self)
        self.menu.mainloop(self.surface)

    def clear_screen(self):
        self.surface.fill((255, 255, 255))
        pygame.display.update()


    def start_the_game(self):
        _subject = self.subjects[self.subject_index]
        _subject_ = importlib.import_module(
            'primaryschool.subjects.' + _subject)
        _subject_.start(self)
        pass
    

def go():
    Win()
    pass
