from tkinter import *
from tkinter import ttk

from abc import ABC

import primaryschool
from primaryschool import *


class WidgetABC(ABC):
    pass


class TopWidget(WidgetABC):
    def __init__(self, root=None, frame=None, mainloop=True):
        self.root_widget = self.rootw = self.root = root or Tk()
        self.frame_padding = 8
        self.frame = frame or ttk.Frame(self.root, padding=self.frame_padding)
        self.pscp_root_width_key = "rootw_width"
        self.pscp_root_height_key = "rootw_height"
        self.subwidgets = []

        if mainloop:
            self.mainloop()

        pass

    def add_subwidgets(self, widgets=None):
        if not widgets:
            return False
        if not isinstance(widgets, list):
            self.subwidgets.append(widget)
        else:
            self.subwidgets += widgets
        return True
        pass

    def add_subwidget(self, widget=None):
        return self.add_subwidgets(widgets=widget)
        pass

    def remove_subwidgets(self, indexes=None, widgets=None):
        if not (indexes and widgets):
            return False
        if indexes:
            if isinstance(indexes, list):
                for i in indexes:
                    if i < len(self.subwidgets):
                        del self.subwidgets[i]
            elif isinstance(indexes, int):
                if indexes < len(self.subwidgets):
                    del self.subwidgets[indexes]
        if widgets:
            if isinstance(widgets, list):
                for w in widgets:
                    if w in self.subwidgets:
                        self.subwidgets.remove(w)
            else:
                if widgets in self.subwidgets:
                    self.subwidgets.remove(widgets)
        return True
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

    def set_root_width_height(self, width=None, height=None):
        if not (width and height):
            return False

        if height:
            pscp.set(self.pscp_root_height_key, height)

        if width:
            pscp.set(self.pscp_root_width_key, width)

        if not height:
            height = self.get_root_height()

        if not width:
            width = self.get_root_width()

        geo_str = f"{width}x{height}"
        self.root.geometry(geo_str)

        return True
        pass

    def set_root_width(self, width=None):
        if not width:
            return False
        return self.set_root_width_height(width=width)
        pass

    def set_root_height(self, height=None):
        if not height:
            return False
        return self.set_root_width_height(height=height)
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
