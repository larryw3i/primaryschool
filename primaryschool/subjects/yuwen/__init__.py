
import os
import sys
import pygame
from pygame.locals import *
import pygame_menu
from pygame_menu.widgets import *

from primaryschool.locale import _
from primaryschool.subjects import *

from pygame_menu._widgetmanager import WidgetManager
name = _('Yuwen')


class YuwenGame(SubjectGame):
    def __init__(self, win):
        super().__init__(win)
        self.win=win
        self.menu = self.win.menu
        self.menu.set_title(_('Yuwen'))
        self.menu.clear()
        
        self.s_width,self.s_height = self.menu.get_size(inner=True)
        self.surface = pygame.Surface((self.s_width, self.s_height))
        self.surface.fill((0,0,255))

        self.menu.add.surface(self.surface,border_width=0,padding=(0,0))



def start(win):
    YuwenGame(win)
    pass
