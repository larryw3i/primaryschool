from abc import ABC
from tkinter import *
from tkinter import ttk

import primaryschool
from primaryschool import *


class GameListWidget(SubWidgetABC):
    def __init__(
        self,
        parent_widget=None,
        min_width_plb=None,
        min_height_plb=None,
        place=False,
    ):
        super().__init__()
        self.game_name_dict = self.gname_dict = None
        self.game_name_list0 = None
        self.game_name_list1 = None
        self.game_name_list2 = None
        self.min_width_plb = self.min_width_for_per_listbox = min_width_p
        self.min_height_plb = self.min_height_for_per_listbox = min_height_plb
        self.game_listbox0 = self.glistbox0 = None
        self.game_listbox1 = self.glistbox1 = None
        self.game_listbox2 = self.glistbox2 = None

        if place:
            self.place()

        pass

    def get_game_name_dict(self):
        if not self.game_name_dict:
            self.game_name_dict = None
            pass
        pass

    def get_game_name_list1(self):
        pass

    def get_gnames1(self, *args, **kwargs):
        return self.get_game_name_list1(args, kwargs)
        pass

    def get_game_name_list2(self):
        pass

    def get_gnames2(self, *args, **kwargs):
        return self.get_game_name_list2(args, kwargs)
        pass

    def get_game_name_list0(self):
        pass

    def get_gnames0(self, *args, **kwargs):
        return self.get_game_name_list0(args, kwargs)
        pass

    def set_game_name_dict(self, gdict=None):
        if not gdict:
            return
        self.game_name_dict = self.gname_dict = gdict
        pass

    def set_gname_dict(self, *args, **kwargs):
        self.set_game_name_dict(args, kwargs)
        pass

    def get_game_listbox1(self):
        if not self.game_listbox1:
            pass

        pass

    def get_game_listbox0(self):
        if not self.game_listbox1:
            pass
        pass

    def get_game_listbox2(self, listbox=None):
        if not self.game_listbox2:
            pass
        pass

    def set_game_listbox1(self, listbox=None):
        if not listbox:
            return
        self.game_listbox1 = self.glistbox1 = listbox
        pass

    def set_game_listbox0(self, listbox=None):
        if not listbox:
            return
        self.game_listbox0 = self.glistbox0 = listbox
        pass

    def set_game_listbox2(self, listbox=None):
        if not listbox:
            return
        self.game_listbox2 = self.glistbox2 = listbox
        pass

    def get_game_name_dict(self):
        pass

    def get_gname_dict(self, *args, **kwargs):
        return self.get_game_name_list(args, kwargs)
        pass

    def get_min_width_for_per_listbox(self):
        pass

    def get_minwidth_plistbox(self, *args, **kwargs):
        return self.get_min_width_for_per_listbox(args, kwargs)
        pass

    def get_min_height_for_per_listbox(self):
        pass

    def get_minheight_plistbox(self, *args, **kwargs):
        return self.get_min_height_for_per_listbox(args, kwargs)
        pass

    def place(self):
        listbox0 = self.get_game_name_list1()

    pass


pass
