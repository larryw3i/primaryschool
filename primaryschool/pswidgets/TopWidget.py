

from tkinter import *
from tkinter import ttk

from abc import ABC

from primaryschool import *


class WidgetABC(ABC):
    pass


class TopWidget(WidgetABC):
    def __init__(self, root=None, frame=None):
        self.root = root or Tk()
        self.frame_padding = 8
        self.frame = frame or ttk.Frame(self.root, padding=self.frame_padding)
        self.pscp_root_width_key = "rootw_width"
        self.pscp_root_height_key = "rootw_height"
        pass

    def set_frame_padding(self, padding=8):
        self.frame_padding = padding
        sef.frame.config(padding=self.frame_padding)
        pass

    def get_frame_padding(self):
        return self.frame_padding
        pass

    def get_root_height(self):
        root_h = pscp.get(self.pscp_root_height_key, None)
        if not root_h:
            root_h = self.root.winfo_screenheight()
            pscp.set(self.pscp_root_height_key, root_h)
        return root_h
        pass

    def get_root_width(self):
        root_w = pscp.get(self.pscp_root_width_key, None)
        if not root_w:
            root_w = self.root.winfo_screenwidth()
            pscp.set(self.pscp_root_width_key, root_w)
        return root_w
        pass


    def set_root_height(self, height = None):
        if not height:
            return False
        pass

    def set_root_width(self,width = None):
        if not width:
            return False
        pass

    def place_widgets(self):
        self.frame.pack()
        pass

    def mainloop(self):
        self.place_widgets()
        self.root.mainloop()

        pass

    pass

pass
