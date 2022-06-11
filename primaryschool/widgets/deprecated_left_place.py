import importlib
import os
import pickle
import subprocess
import sys
import threading
import tkinter as tk
import uuid
import webbrowser
from functools import partial
from importlib import import_module
from itertools import zip_longest
from tkinter import *
from tkinter import ttk

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu._scrollarea import ScrollArea
from pygame_menu.baseimage import BaseImage
from pygame_menu.locals import *
from pygame_menu.widgets import *

from primaryschool.dirs import *
from primaryschool.dirs import user_screenshot_dir_path
from primaryschool.locale import _
from primaryschool.resource import (
    default_font,
    default_font_path,
    get_default_font,
    get_resource_path,
)
from primaryschool.settings import *
from primaryschool.settings_t import *
from primaryschool.subjects import subjects
from primaryschool.widgets.abc import WidgetABC


class LeftPlace(WidgetABC):
    def __init__(
        self,
        ps,
    ):
        super().__init__(ps)
        self.treeview = ttk.Treeview(
            self.root, columns=("game", "author", "DOU"), show="headings"
        )
        self.yscrollbar = tk.Scrollbar(self.root, orient=VERTICAL)
        self.xscrollbar = tk.Scrollbar(self.root, orient=HORIZONTAL)
        self.treeview.config(
            yscrollcommand=self.yscrollbar.set,
            xscrollcommand=self.xscrollbar.set,
        )
        self.yscrollbar.config(command=self.treeview.yview)
        self.xscrollbar.config(command=self.treeview.xview)

        self.set_treeview_columns()
        self.set_treeview_heading()
        self.set_treeview_data()

    def set_treeview_columns(self):
        root_widthof_6 = int(self.ps.get_root_width() / 9)
        self.treeview.column(
            "game", width=root_widthof_6, anchor="w", stretch=True
        )
        self.treeview.column(
            "author", width=root_widthof_6, anchor=CENTER, stretch=True
        )
        self.treeview.column(
            "DOU", width=root_widthof_6, anchor=CENTER, stretch=True
        )

    def set_treeview_data(self):
        for subject in subjects:
            _subject = self.treeview.insert(
                "", "end", values=(subject.name_t), open=True
            )
            for game in subject.get_games():
                _game = self.treeview.insert(
                    _subject,
                    "end",
                    values=(
                        "  " + game.name_t,
                        getattr(game, "author", "NULL"),
                        getattr(game, "DOU", "NULL"),
                    ),
                )

    def set_treeview_heading(self):
        self.treeview.heading("game", text=_("Game"))
        self.treeview.heading("author", text=_("Author"))
        self.treeview.heading("DOU", text=_("Updating date"))

    def get_yscrollbar_w(self):
        return self.yscrollbar.winfo_reqwidth()

    def get_xscrollbar_w(self):
        return self.xscrollbar.winfo_reqwidth()

    def get_xscrollbar_h(self):
        return self.xscrollbar.winfo_reqheight()

    def get_treeview_x(self):
        return 0

    def get_treeview_y(self):
        return 0

    def get_treeview_h(self):
        return self.ps.get_root_height() - self.get_xscrollbar_h()

    def get_treeview_reqw(self):
        return self.treeview.winfo_reqwidth()

    def get_treeview_w(self):
        root_width_of_3 = self.ps.get_root_width() / 3
        reqw = self.get_treeview_reqw()
        return reqw > root_width_of_3 and root_width_of_3 or reqw

    def place(self):
        self.treeview.place(
            x=0,
            y=0,
            height=self.get_treeview_h(),
            width=self.get_treeview_w(),
        )
        self.xscrollbar.place(
            x=0, y=self.get_treeview_h(), width=self.get_treeview_w()
        )
        self.yscrollbar.place(
            x=self.get_treeview_w(), y=0, height=self.get_treeview_h()
        )
