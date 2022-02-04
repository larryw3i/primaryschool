

import importlib
import os

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.widgets import *

from primaryschool.locale import _
from primaryschool.resource import font_path
from primaryschool.subjects import list_subjects

class Win():
    def __init__(self):
                
        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w_width, self.w_height = self.win.get_size()
        self.menu_theme = pygame_menu.themes.THEME_BLUE

        self.menu = pygame_menu.Menu(
            _('Primary School'), self.w_width, self.w_height,
            theme=pygame_menu.themes.THEME_BLUE)

        self.difficulty_index = 0
        self.subject_index=0
        self.subjects_t,self.subjects = list_subjects() 
        self.difficulties = ['Crazy','Hard', 'Middle', 'Easy']
        self.difficulties_t = [_(d) for d in self.difficulties]

        self.render()
   

    def render(self):

        self.win.fill((255, 255, 255))
        self.menu_theme.title_font = font_path
        self.menu.add.text_input(
            _('Name :'), default=_('_name_'),
            font_name=font_path)
        self.menu.add.dropselect(
            title=_('Subject :'),
            items=[(name, index) for index, name in enumerate(self.subjects_t)],
            font_name=font_path,
            default=self.subject_index,
            placeholder=_('Select an Subject'),
            onchange = self.set_subject
        )
        self.menu.add.dropselect(
            title=_('Difficulty :'),
            items=[(d, index) for index, d in enumerate(self.difficulties_t)],
            font_name=font_path,
            default=self.difficulty_index,
            placeholder=_('Select an difficulty'),
            onchange = self.set_difficulty
        )
        self.menu.add.button(
            _('Play'), 
            self.start_the_game,
            font_name=font_path)
        self.menu.add.button(
            _('Quit'), 
            pygame_menu.events.EXIT,
            font_name=font_path)        

    def set_difficulty(self,value, difficulty):
        self.difficulty_index = difficulty
        pass


    def set_subject(self,value, subject):
        self.subject_index = subject
        pass


    def start_the_game(self):
        _subject= self.subjects[self.subject_index]
        _subject_=importlib.import_module('primaryschool.subjects.'+_subject)
        _subject_.start(self)
        pass
    def display(self):
        self.menu.mainloop(self.win)
        pygame.display.update()
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    
        pygame.quit()



def go():    
    Win().display()
    pass
