from tkinter import *
from tkinter import ttk

from abc import ABC


class WidgetABC(ABC):
    pass


class TopWidget(WidgetABC):
    def __init__(self, root=None, frame=None):
        self.root = root or Tk()
        self.frame_padding = 8
        self.frame = frame or ttk.Frame(self.root, padding=self.frame_padding)
        pass

    def set_frame_padding(self, padding=8):
        self.frame_padding = padding
        sef.frame.config(padding=self.frame_padding)
        pass

    def get_frame_padding(self):
        return self.frame_padding
        pass

    def place_widgets(self):
        self.frame.pack()
        pass

    def mainloop(self):
        self.place_widgets()
        self.root.mainloop()

        pass

    pass
