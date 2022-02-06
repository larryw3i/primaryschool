

import importlib
import os

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.widgets import *

from primaryschool.locale import _
from primaryschool.resource import font_path
from primaryschool.subjects import get_subjects


def default_menu(win, title, **kwargs):

    theme = pygame_menu.themes.THEME_BLUE.copy()
    theme.title_font = font_path
    return pygame_menu.Menu(title, win.w_width, win.w_height,
                            theme=theme, **kwargs)


class AboutMenu():

    def __init__(self, win):

        self.win = win
        self.title = _('Play Game')
        self._menu = default_menu(self.win, self.title)


class PlayMenu():
    def __init__(self, win):

        self.win = win
        self.title = _('Play Game')

        self._menu = default_menu(self.win, self.title)

        self.difficulty = self.win.difficulty
        self.subject = self.win.subject

        self.subjects = self.win.subjects
        self.difficulties = self.win.difficulties

        self.add_widgets()

    def add_widgets(self):
        self._menu.add.text_input(
            _('Name :'), default=_('_name_'),
            font_name=font_path)
        self._menu.add.dropselect(
            title=_('Subject :'),
            items=[(name, index) for index, name in enumerate(
                self.subjects)],
            font_name=font_path,
            default=self.subject,
            placeholder=_('Select an Subject'),
            onchange=self.set_subject
        )
        self._menu.add.dropselect(
            title=_('Difficulty :'),
            items=[(d, index) for index, d in enumerate(
                self.difficulties)],
            font_name=font_path,
            default=self.difficulty,
            placeholder=_('Select an difficulty'),
            onchange=self.set_difficulty
        )
        self._menu.add.button(
            _('Play'),
            self.start_the_game,
            font_name=font_path)
        self._menu.add.button(
            _('Return to main menu'),
            pygame_menu.events.BACK,
            font_name=font_path)

    def start_the_game(self):
        _subject = self.subjects[self.subject]
        _subject_ = importlib.import_module(
            'primaryschool.subjects.' + _subject)
        _subject_.start(self.win)
        pass

    def set_difficulty(self, value, difficulty):
        self.difficulty = difficulty

    def set_subject(self, value, subject):
        self.subject = subject


class MainMenu():
    def __init__(self, win):
        self.win = win
        self.title = _('Primary School')
        self._menu = default_menu(self.win, self.title)
        self.play_menu = PlayMenu(self.win)
        self.about_menu = AboutMenu(self.win)
        

        self.add_widgets()

    def add_widgets(self):
        self._menu.add.button('Play', self.play_menu._menu)
        self._menu.add.button('About', self.about_menu._menu)
        self._menu.add.button('Quit', pygame_menu.events.EXIT)


class Win():
    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.running = True

        self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w_width, self.w_height = self.surface.get_size()


        self.difficulty = 2
        self.subject = 0


        self.subjects = get_subjects()
        self.difficulties = [ _('Crazy'), _('Hard'), _('Middle'), _('Easy')]

        self.main_menu = MainMenu(self)

    def clear_screen(self):
        self.surface.fill((255, 255, 255))
        pygame.display.update()
    
    def get_difficulty_by_index(self,index=-1):
        index = self.difficulty if index == -1 else index
        return self.difficulties[index]

    def get_subject_by_index(self,index=-1):
        index = self.subject if index == -1 else index
        return self.subjects[index]

    def run(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        if self.main_menu._menu.is_enabled():
            self.main_menu._menu.mainloop(self.surface)
        pygame.display.flip()


def go():
    Win().run()
    pass
