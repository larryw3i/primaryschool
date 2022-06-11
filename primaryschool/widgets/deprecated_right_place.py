import os
import sys
import tkinter as tk
import uuid
import webbrowser
from importlib import import_module
from tkinter import *
from tkinter import ttk

from primaryschool.dirs import *
from primaryschool.locale import _
from primaryschool.settings import *
from primaryschool.settings_t import *
from primaryschool.widgets.abc import WidgetABC


class RightPlace(WidgetABC):
    def __init__(
        self,
        ps,
    ):
        super().__init__(ps)
        self.text = tk.Text(self.root)
