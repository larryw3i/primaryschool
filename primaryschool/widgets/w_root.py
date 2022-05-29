import os
import sys
import tkinter as tk
from importlib import import_module
from tkinter import *
from tkinter import ttk

from primaryschool.dirs import *
from primaryschool.locale import _


class PSWidget:
    def __init__(self):
        self.root = Tk()

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

    def get_default_x():
        return self.get_screenwidth(of=4)

    def get_default_y():
        return self.get_screenheight(of=4)

    def get_default_width():
        return self.get_screenwidth(of=2)

    def get_default_height():
        return self.get_screenheight(of=2)

    def place(self):
        pass

    def set_bind(self):
        self.root.bind("<Configure>", self.root_bind_configure)

    def root_bind_configure(self, *args):
        pass

    def set_widgets(self):
        pass

    def mainloop(self):
        self.set_title()
        self.set_geometry()
        self.set_widgets()
        self.set_bind()
        self.place()
        self.root.mainloop()
