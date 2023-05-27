# /bin/python3
import abc
from abc import ABC
from tkinter import *
from tkinter import ttk

import pygubu
from pygubu.widgets.scrolledframe import *

import primaryschool
from primaryschool import *
from primaryschool.psgames import *
from primaryschool.pswidgets import *
from primaryschool.pswidgets.WidgetABC import *


class PsGameListWidget(PsSubWidget):
    def __init__(self, top_widget=None):
        super().__init__(top_widget)

        self.frame = self.top_widget.sclframe

        pass

    def get_game_list(self):
        game_list = get_game_list()
        return game_list

    def get_game_names(self):
        game_names = get_game_names()
        return game_names

    def get_game_difficulties(self):
        game_difficulties = get_game_difficulties()
        return game_difficulties

    def get_frame_x(self):
        _x = 0
        return _x
        pass

    def get_frame_y(self):
        _y = 0
        return _y
        pass

    def get_frame_width(self):
        _width = self.top_widget.get_root_width()
        return _width
        pass

    def get_frame_height(self):
        _height = self.top_widget.get_root_height()
        return _height
        pass

    def place(self):
        if self.frame:
            self.frame.place(
                x=self.get_frame_x(),
                y=self.get_frame_y(),
                width=self.get_frame_width(),
                height=self.get_frame_height(),
            )
        pass

    pass


pass
