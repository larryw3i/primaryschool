import os
import sys
import tkinter as tk
from importlib import import_module
from tkinter import *
from tkinter import ttk

from primaryschool.dirs import *
from primaryschool.locale import _
from primaryschool.widgets.abc import WidgetABC
from primaryschool.widgets.about_toplevel import AboutToplevel


class PSMenubar(WidgetABC):
    def __init__(self, ps):
        super().__init__(ps)
        self.menu = Menu(
            self.root,
        )
        self.about_toplevel = None
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label=_("About"), command=self.about)
        self.menu.add_cascade(label=_("Help"), menu=self.help_menu)

    def config(self):
        self.root.config(menu=self.menu)

    def place(self):
        pass

    def about(self):
        if not self.about_toplevel:
            self.about_toplevel = AboutToplevel(self.ps)
            return
        self.about_toplevel.ok()
