

import importlib
import os

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.widgets import *

from primaryschool.locale import _
from primaryschool.resource import font_path
from primaryschool.subjects import list_subjects

def default_menu(win,title,**kwargs):

    theme = pygame_menu.themes.THEME_BLUE.copy()
    theme.title_font = font_path
    return pygame_menu.Menu(title, win.w_width, win.w_height,
                        theme=theme,**kwargs)


class AboutMenu():

    def __init__(self,win):

        self.win = win
        self.title = _('Play Game')
        self._menu = default_menu(self.win,self.title)

class PlayMenu():
    def __init__(self,win):

        self.win = win
        self.title = _('Play Game')
        
        self._menu = default_menu(self.win, self.title)

        self.difficulty_index = 2
        self.subject_index = 0

        self.subjects_t, self.subjects = list_subjects()
        self.difficulties = ['Crazy', 'Hard', 'Middle', 'Easy']
        self.difficulties_t = [_(d) for d in self.difficulties]

    
        self.add_widgets()

    def add_widgets(self):
        self._menu.add.text_input(
            _('Name :'), default=_('_name_'),
            font_name=font_path)
        self._menu.add.dropselect(
            title=_('Subject :'),
            items=[(name, index) for index, name in enumerate(
                self.subjects_t)],
            font_name=font_path,
            default=self.subject_index,
            placeholder=_('Select an Subject'),
            onchange=self.set_subject
        )
        self._menu.add.dropselect(
            title=_('Difficulty :'),
            items=[(d, index) for index, d in enumerate(
                self.difficulties_t)],
            font_name=font_path,
            default=self.difficulty_index,
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
        _subject = self.subjects[self.subject_index]
        _subject_ = importlib.import_module(
            'primaryschool.subjects.' + _subject)
        _subject_.start(self)
        pass

    def set_difficulty(self, value, difficulty):
        self.win.difficulty_index = difficulty

    def set_subject(self, value, subject):
        self.win.subject_index = subject


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

        self.main_menu = MainMenu(self)
        

    def clear_screen(self):
        self.surface.fill((255, 255, 255))
        pygame.display.update()
    
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
