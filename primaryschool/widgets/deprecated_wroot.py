import os
import sys
import tkinter as tk
from importlib import import_module
from tkinter import *
from tkinter import ttk

from primaryschool.dirs import *
from primaryschool.locale import _
from primaryschool.widgets.left_place import LeftPlace
from primaryschool.widgets.menubar import PSMenubar


class PSWidget:
    def __init__(self):
        self.root = Tk()
        self.menubar = PSMenubar(self)
        self.leftplace = LeftPlace(self)

    def set_title(self, title=_("Primary School")):
        self.root.title(title)

    def set_geometry(self, geometry=None):
        geometry = geometry or (
            f"{self.get_default_width()}"
            + f"x{self.get_default_height()}"
            + f"+{self.get_default_x()}"
            + f"+{self.get_default_y()}"
        )
        self.root.geometry(geometry)

    def get_screenwidth(self, of=1):
        return int(self.root.winfo_screenwidth() / of)

    def get_screenheight(self, of=1):
        return int(self.root.winfo_screenheight() / of)

    def get_default_x(self):
        return self.get_screenwidth(of=4)

    def get_default_y(self):
        return self.get_screenheight(of=4)

    def get_default_width(self):
        return self.get_screenwidth(of=2)

    def get_menubar_width(self):
        return self.menubar.menu.winfo_reqheight()

    def get_default_height(self):
        return self.get_screenheight(of=2)

    def get_root_width(self):
        root_width = self.root.winfo_width()
        return root_width > 1 and root_width or self.get_default_width()

    def get_root_height(self):
        root_height = self.root.winfo_height()
        return root_height > 1 and root_height or self.get_default_height()

    def place(self):
        self.menubar.place()
        self.leftplace.place()

    def set_bind(self):
        self.root.bind("<Configure>", self.root_bind_configure)

    def root_bind_configure(self, *args):
        self.menubar.config()
        self.place()

    def config(self):
        pass

    def set_widgets(self):
        pass

    def mainloop(self):
        self.set_title()
        self.set_geometry()
        self.set_widgets()
        self.config()
        self.set_bind()
        self.place()
        self.root.mainloop()
