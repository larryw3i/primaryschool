from abc import ABC
from tkinter import *
from tkinter import ttk

import primaryschool
from primaryschool import *


class GameList(SubWidgetABC):
    def __init__(
        self, game_name_list=None, min_width_plb=None, min_height_plb=None
    ):
        super().__init__()
        self.game_name_list = self.gname_list = game_name_list
        self.min_width_plb = self.min_width_for_per_listbox = min_width_p
        self.min_height_plb = self.min_height_for_per_listbox = min_height_plb

        pass

    def get_game_name_list(self):
        pass

    def get_gname_list(self, *args, **kwargs):
        return self.get_game_name_list(args, kwargs)
        pass

    def get_min_width_for_per_listbox(self):
        pass

    def get_minwidth_plistbox(self):
        return self.get_min_width_for_per_listbox()
        pass

    def get_min_height_for_per_listbox(self):
        pass

    def get_minheight_plistbox(self):
        return self.get_min_height_for_per_listbox()
        pass

    pass


pass
