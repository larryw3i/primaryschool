import abc
from abc import ABC
from tkinter import *
from tkinter import ttk

import pygubu
from pygubu.widgets.scrolledframe import *

import primaryschool
from primaryschool import *


class WidgetABC(ABC):
    def __init__(self):
        self.set_ps_cp = self.set_ps_copy = set_ps_copy
        self.pscp = pscp
        self.subwidgets = []
        pass

    def save_ps_cp(self):
        self.set_ps_cp(self.pscp)
        pass

    def save_ps_copy(self, *args, **kwargs):
        self.save_ps_cp(*args, **kwargs)
        pass

    pass


class SubWidget(WidgetABC):
    def __init__(self, parent_widget=None):
        if not parent_widget:
            print(_("'parent_widget' is None."))
        super().__init__()
        self.parent_widget = parent_widget
        self.psubwidgets = (
            self.parent_subwidgets
        ) = self.parent_widget.subwidgets
        if not self in self.psubwidgets:
            self.psubwidgets.append(self)
            pass

        pass

    @abc.abstractmethod
    def place(self):
        pass

    @abc.abstractmethod
    def config(self):
        pass

    pass


class TopWidget(WidgetABC):
    def __init__(
        self, root=None, frame=None, mainloop=True, title=None, menubar=None
    ):
        super().__init__()
        self.root_widget = self.rootw = self.root = root or Tk()

        self.menubar = menubar or Menu(self.root_widget)
        self.helpmenu = None

        self.frame_padding = 8
        self.main_sclframe = (
            self.mainsclframe
        ) = self.sclframe = frame or ScrolledFrame(
            self.root_widget, scrolltype="both", usemousewheel=True
        )
        self.main_frame = (
            self.mainframe
        ) = self.frame = self.main_sclframe.innerframe
        self.pscp_root_width_key = "rootw_width"
        self.pscp_root_height_key = "rootw_height"
        self.title = title or f"{app_name} ({app_version})"
        self.about_messagebox = None

        self.bind_config = False

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
            pscp[self.pscp_root_height_key] = root_h
        return root_h
        pass

    def get_root_width(self):
        root_w = pscp.get(self.pscp_root_width_key, None)
        if not root_w:
            root_w = self.root.winfo_screenwidth()
            pscp[self.pscp_root_width_key] = root_w
        return root_w
        pass

    def set_root_width_height(
        self, width=None, height=None, update_widget=True
    ):
        if height:
            pscp.set(self.pscp_root_height_key, height)

        if width:
            pscp.set(self.pscp_root_width_key, width)

        if not height:
            height = self.get_root_height()

        if not width:
            width = self.get_root_width()

        if update_widget:
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

    def set_rootw_width(self, *args, **kwargs):
        self.set_root_width(*args, **kwargs)
        pass

    def set_rootw_height(self, *args, **kwargs):
        self.set_root_height(*args, **kwargs)
        pass

    def set_root_widget_width(self, *args, **kwargs):
        self.set_root_width(*args, **kwargs)
        pass

    def set_root_widget_height(self, *args, **kwargs):
        self.set_root_height(*args, **kwargs)
        pass

    def get_mainsclframe_x(self):
        return 0
        pass

    def get_mainsclframe_y(self):
        return 0
        pass

    def get_mainsclframe_width(self):
        return self.get_root_width()
        pass

    def get_mainsclframe_height(self):
        return self.get_root_height()
        pass

    def on_rootw_closing(self):
        self.save_ps_cp()
        if messagebox.askokcancel(
            _("Quit"),
            _("Do you want to quit?"),
            parent=self.root_widget,
        ):
            self.root_widget.destroy()
        pass

    def set_rootw_width_height_cp(self, event=None, width=None, height=None):
        if event:
            self.pscp[self.pscp_root_width_key] = event.width
            self.pscp[self.pscp_root_height_key] = event.height
            return
        if width and width > 0:
            self.pscp[self.pscp_root_width_key] = width

        if height and height > 0:
            self.pscp[self.pscp_root_height_key] = height

        pass

    def set_rootw_wh_cp(self, *args, **kwargs):
        self.set_rootw_width_height_cp(*args, **kwargs)
        pass

    def cmd_get_help(self):
        pass

    def show_about_message(self):
        tk.messagebox.showinfo(
            parent=self.root_widget,
            title=_("About"),
            message=_("Funing:\n" + "The primary school knowledge games."),
        )

        pass

    def cmd_about(self):
        self.show_about_message()
        pass

    def set_menubar_cascades(self):
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(
            label=_("Get Help"), command=self.cmd_get_help
        )
        self.helpmenu.add_command(label=_("About..."), command=self.cmd_about)
        self.menubar.add_cascade(label=_("Help"), menu=self.helpmenu)
        self.root_widget.config(menu=self.menubar)
        pass

    def place_widgets(self):
        if self.mainsclframe:
            self.mainsclframe.place(
                x=self.get_mainsclframe_x(),
                y=self.get_mainsclframe_y(),
                width=self.get_mainsclframe_width(),
                height=self.get_mainsclframe_height(),
            )

        for sw in self.subwidgets:
            sw.place()
        pass

    def get_root_x(self):
        return self.root_widget.winfo_x()

    def get_root_y(self):
        return self.root_widget.winfo_y()

    def get_rootw_winfo_width(self):
        if not self.root_widget:
            return None
        return self.root_widget.winfo_width()
        pass

    def get_rootw_winfo_height(self):
        if not self.root_widget:
            return None
        return self.root_widget.winfo_height()
        pass

    def on_rootw_configuring(self, event=None):
        if event:
            self.set_rootw_width_height_cp(
                width=self.get_rootw_winfo_width(),
                height=self.get_rootw_winfo_height(),
            )

        self.place_widgets()
        pass

    def bind_rootw_enter(self, event=None):
        if not event:
            return

        if not self.bind_config:
            self.root_widget.bind("<Configure>", self.on_rootw_configuring)
            self.bind_config = True
        pass

    def close(self, *args, **kwargs):
        self.on_rootw_closing(*args, **kwargs)
        pass

    def config(self, *args, **kwargs):
        self.on_rootw_configuring(*args, **kwargs)
        pass

    def mainloop(self):
        self.root_widget.title(self.title)
        self.set_menubar_cascades()
        self.set_root_width_height()
        self.place_widgets()
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.root_widget.bind("<Configure>", self.config)
        self.root_widget.mainloop()

        pass

    pass


pass
