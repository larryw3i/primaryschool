
import os
import sys
import tkinter as tk
from importlib import import_module
from tkinter import *
from tkinter import ttk

from primaryschool.dirs import *
from primaryschool.locale import _
from w_abc import SubWidgetABC

class PSMenubar(SubWidgetABC):
    def __init__(self,ps):
        super().__init__(ps)
        self.menu = Menu(, background='#ff8000', foreground='black', 
            activebackground='white', activeforeground='black')  
        self.help_menu = self.Menu(self.menu, tearoff=0)  
        self.help_menu.add_command(label="About", command=self.about)  
        self.menu.add_cascade(label="Help", menu=self.help_menu)  
        self.root.config(menu=self.menu)

    def about(self):
        about_toplevel = TopLevel(self.root)
        