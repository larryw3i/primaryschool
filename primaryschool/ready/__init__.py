

import importlib
import os

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.widgets import *

from primaryschool.locale import _
from primaryschool.resource import font_path
from primaryschool.subjects import list_subjects


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game():
    # Do the job here !
    pass


def go():
    pygame.init()
    pygame.font.init()

    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w_width, w_height = win.get_size()

    win.fill((255, 255, 255))

    subjects = list_subjects()

    menu_theme = pygame_menu.themes.THEME_BLUE
    menu_theme.title_font = font_path

    menu = pygame_menu.Menu(
        _('Primary School'), w_width, w_height,
        theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input(
        _('Name :'), default=_('_name_'),
        font_name=font_path)
    menu.add.dropselect(
        title=_('Subject :'),
        items=[(name, index) for index, name in enumerate(subjects)],
        max_selected=1,
        font_name=font_path,
        default=1,
        placeholder=_('Select an Subject'),
    )
    menu.add.dropselect(
        title=_('Difficulty :'),
        items=[(_('Crazy'), 0), (_('Hard'), 1),
               (_('Middle'), 2), (_('Easy'), 3)],
        font_name=font_path,
        default=3,
        placeholder=_('Select an difficulty'),
    )
    menu.add.button(
        _('Play'), start_the_game,
        font_name=font_path)
    menu.add.button(
        _('Quit'), pygame_menu.events.EXIT,
        font_name=font_path)

    menu.mainloop(win)

    pygame.display.update()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

    pygame.quit()

    pass
