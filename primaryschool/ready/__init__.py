

import importlib
import os
import pickle
import threading

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.baseimage import BaseImage
from pygame_menu.widgets import *

from primaryschool.dirs import *
from primaryschool.locale import _
from primaryschool.resource import (default_font, default_font_path,
                                    get_default_font, get_resource_path)
from primaryschool.settings import *
from primaryschool.ready.resource import resource_dir_path
from primaryschool.subjects import subjects
import tkinter as tk
from tkinter import ttk
import webbrowser

app_description_t = _("app_description_t")

translator = _

class SaveMenu():
    def __init__(self, ps):
        self.ps = ps
        self.surface = self.ps.surface
        self.title = _('Save game?')
        self._menu = self.ps.get_default_menu(self.title)
        self.save = False

    def add_widgets(self):

        self._menu.add.button(
            _('Save and return'),
            self.save_the_game,
            font_name=self.ps.font_path)
        self._menu.add.button(
            _('Continue'),
            self.continue_the_game,
            font_name=self.ps.font_path)
        self._menu.add.button(
            _('Return to main menu'),
            self.to_main_menu,
            font_name=self.ps.font_path)

    def to_main_menu(self):
        self.ps.main_menu._menu.full_reset()
        self.ps.main_menu._menu.enable()
        self.ps.main_menu._menu.mainloop(self.surface)

    def save_the_game(self):
        self.ps.subject_game.save(self.ps)
        self._menu.disable()
        self.to_main_menu()

    def continue_the_game(self):
        self._menu.disable()


class AboutMenu():
    def __init__(self, ps):

        self.ps = ps
        self.title = _('About')
        self._menu = self.ps.get_default_menu(self.title)
        self.app_name_font = get_default_font(50)
        self.app_version_font = get_default_font(20)
        self.app_description_font = get_default_font(22)
        self.app_url_font = get_default_font(20)
        self.app_author_font = get_default_font(22)
        self.app_contributors_font = self.app_author_font

    def add_widgets(self):
        self._menu.add.label(app_name, max_char=-1,
                             font_name=self.app_name_font)
        self._menu.add.label(app_version, max_char=-1,
                             font_name=self.app_version_font)
        self._menu.add.label(app_description_t, max_char=-1,
                             font_name=self.app_description_font)
        self._menu.add.url(app_url, font_name=self.app_url_font)
        self._menu.add.label(_('Author'), max_char=-1,
                             font_name=get_default_font(32))
        self._menu.add.label(app_author, max_char=-1,
                             font_name=self.app_author_font)
        self._menu.add.label(_('Contributors'), max_char=-1,
                             font_name=get_default_font(32))
        self._menu.add.label('\n'.join(app_contributors[1:]),
                             max_char=-1, font_name=self.app_contributors_font)
        self._menu.add.button(
            _('Return to main menu'),
            pygame_menu.events.BACK,
            font_name=self.ps.font_path)


class PlayMenu():
    def __init__(self, ps):
        self.ps = ps
        self.title = _('Play Game')
        self._menu = self.ps.get_default_menu(self.title)
        self.subjects = self.ps.subjects
        self.subject_games = self.ps.subject_games
        self.subject_index = self.ps.subject_index = 0
        self.subject_game_index = self.ps.subject_game_index
        self.difficulty_index = self.ps.difficulty_index
        self.subject = self.ps.subject
        self.subject_game = self.ps.subject_game
        self.subject_dropselect = None
        self.subject_game_dropselect = None
        self.difficulty_dropselect = None
        self.continue_button = None
        self.selection_box_bgcolor = (255, 255, 255)

    def add_widgets(self):
        self._menu.add.text_input(
            title=_('Name :'),
            default=_('_name_'),
            font_name=self.ps.font_path)

        self.subject_dropselect = self._menu.add.dropselect(
            title=_('Subject :'),
            items=[(s.name_t, index)for index, s in enumerate(self.subjects)],
            font_name=self.ps.font_path,
            default=0,
            selection_box_bgcolor=self.selection_box_bgcolor,
            placeholder=_('Select a Subject'),
            onchange=self.on_subject_dropselect_change
        )
        self.subject_game_dropselect = self._menu.add.dropselect(
            title=_('Game :'),
            items=[(g.name_t, index) for index, g in enumerate(
                self.subject_games)],
            font_name=self.ps.font_path,
            default=0,
            selection_box_bgcolor=self.selection_box_bgcolor,
            placeholder=_('Select a game'),
            onchange=self.on_subject_game_dropselect_change
        )

        self.difficulty_dropselect = self._menu.add.dropselect(
            title=_('Difficulty :'),
            items=[(d, index) for index, d in
                   enumerate(self.subject_games[0].difficulties)],
            font_name=self.ps.font_path,
            default=0,
            selection_box_bgcolor=self.selection_box_bgcolor,
            placeholder=_('Select a difficulty'),
            onchange=self.on_difficulty_dropselect_change
        )
        self.update_selection_box_width()

        self._menu.add.button(
            _('Play'),
            self.play_btn_onreturn,
            font_name=self.ps.font_path)
        self.continue_button = self._menu.add.button(
            _('Continue'),
            self.continue_btn_onreturn,
            font_name=self.ps.font_path)
        self.update_continue_button()
        self._menu.add.button(
            _('Return to main menu'),
            pygame_menu.events.BACK,
            font_name=self.ps.font_path)

    def update_selection_box_width(self):
        for ds in [
                self.subject_dropselect,
                self.subject_game_dropselect,
                self.difficulty_dropselect]:
            ds._selection_box_width = max(
                [b.get_width() for b in ds._option_buttons]
            ) + ds._selection_box_inflate[0]
            ds._make_selection_drop()
            ds.render()

    def play_btn_onreturn(self):
        self.start_the_game()

    def continue_btn_onreturn(self):
        self.start_copied_game()

    def update_continue_button(self):
        if self.subject_game.has_copy():
            self.continue_button.show()
        else:
            self.continue_button.hide()

    def update_subject_game_dropselect(self):
        self.subject_game_dropselect.update_items(
            [(g.name_t, index) for index, g in enumerate(
                self.subject.games)])
        self.subject_game_dropselect.set_value(self.subject_game_index)

    def update_difficulty_dropselect(self):
        self.difficulty_dropselect.update_items(
            [(d, index) for index, d in enumerate(
                self.subject_game.difficulties)])
        self.difficulty_dropselect.set_value(self.difficulty_index)

    def start_copied_game(self):
        self.subject_game.load(self.ps)

    def start_the_game(self):
        self.subject_game.play(self.ps)

    def on_difficulty_dropselect_change(self, value, index):
        self.set_difficulty_index(index)

    def on_subject_dropselect_change(self, item, index):
        self.set_subject_index(index)

    def on_subject_game_dropselect_change(self, item, index):
        self.set_subject_game_index(index)

    def set_subject_index(self, index=0):
        self.subject_index = self.ps.subject_index = index
        self.subject = self.ps.subject = self.subjects[self.subject_index]
        self.subject_games = self.ps.subject_games = self.subject.games
        self.set_subject_game_index()
        self.update_subject_game_dropselect()
        self.update_selection_box_width()

    def set_subject_game_index(self, index=0):
        self.subject_game_index = self.ps.subject_game_index = index
        self.subject_game = self.ps.subject_game = \
            self.subject.games[self.subject_game_index]
        self.update_continue_button()
        self.set_difficulty_index()

    def set_difficulty_index(self, index=0):
        self.difficulty_index = self.ps.difficulty_index = index
        self.update_difficulty_dropselect()


class MainMenu():
    def __init__(self, ps):
        self.ps = ps
        self.title = _('Primary School')
        self._menu = self.ps.get_default_menu(self.title)
        self.play_menu = self.ps.play_menu
        self.about_menu = self.ps.about_menu

    def add_widgets(self):
        self._menu.add.button(
            _('Play'), self.ps.play_menu._menu,
            font_name=self.ps.font_path,)
        self._menu.add.button(
            _('About'), self.ps.about_menu._menu,
            font_name=self.ps.font_path,)
        self._menu.add.button(
            _('Quit'), pygame_menu.events.EXIT,
            font_name=self.ps.font_path,)


class PrimarySchool_():
    def __init__(self):
        pygame.init()
        self.running = True
        self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w_width, self.w_height = self.surface.get_size()
        self.w_width_of_2, self.w_height_of_2 = self.w_width / 2, \
            self.w_height / 2
        self.w_centrex_y = [self.w_width_of_2, self.w_height]
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.subjects = subjects
        self.subject_games = self.subjects[0].games
        self.subject_index = 0
        self.subject_game_index = 0
        self.difficulty_index = 0
        self.subject = self.subjects[0]
        self.subject_game = self.subject_games[0]
        self.font_path = default_font_path
        self.font = default_font
        self.bg_img = None
        self.play_menu = PlayMenu(self)
        self.about_menu = AboutMenu(self)
        self.save_menu = SaveMenu(self)
        self.main_menu = MainMenu(self)

    def add_widgets(self):
        self.play_menu.add_widgets()
        self.about_menu.add_widgets()
        self.save_menu.add_widgets()
        self.main_menu.add_widgets()

    def set_bg_img(self, src_name='0x1.png'):
        self.bg_img = BaseImage(
            get_resource_path(src_name),
            pygame_menu.baseimage.IMAGE_MODE_FILL)

    def get_bg_img(self):
        if not self.bg_img:
            self.set_bg_img()
        return self.bg_img

    def get_default_menu(self, title, **kwargs):
        theme = pygame_menu.themes.THEME_BLUE.copy()
        theme.title_font = theme.widget_font = self.font
        theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        theme.background_color = self.get_bg_img()
        return pygame_menu.Menu(title, self.w_width, self.w_height,
                                theme=theme, **kwargs)

    def clear_screen(self):
        self.surface.fill((255, 255, 255))
        pygame.display.update()

    def run(self):

        self.add_widgets()

        while self.running:
            self.clock.tick(self.FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if self.main_menu._menu.is_enabled():
                self.main_menu._menu.mainloop(self.surface)

            pygame.display.flip()



class MainFrame:
    def __init__(self,master,ps):
        self.ps = ps
        self.master = master 
        self.widget = ttk.Frame(self.master)
        self.listbox_frame = ttk.Frame(self.widget)
        self.subject_frame = ttk.Frame(self.listbox_frame)
        self.game_frame = ttk.Frame(self.listbox_frame)
        self.difficulty_frame = ttk.Frame(self.listbox_frame)
        self.subject_scrollbar = tk.Scrollbar(self.subject_frame)
        self.game_scrollbar = tk.Scrollbar(self.game_frame)
        self.difficulty_scrollbar = tk.Scrollbar(self.difficulty_frame)
        self.subject_listbox=tk.Listbox(self.subject_frame)
        self.game_listbox=tk.Listbox(self.game_frame)
        self.difficulty_listbox=tk.Listbox(self.difficulty_frame)
        self.game_listboxs = [
            (self.subject_frame,self.subject_listbox,self.subject_scrollbar),
            (self.game_frame,self.game_listbox,self.game_scrollbar),
            (self.difficulty_frame, self.difficulty_listbox,\
                self.difficulty_scrollbar)
        ]
    
    def set_widgets(self):
        for _,l,s in self.game_listboxs:
            l.config(yscrollcommand=s.set)
            s.config(command=l.yview)        
        
    
    def set_layout(self):
        for f,l, s in self.game_listboxs:
            l.pack(side = tk.LEFT, fill = tk.BOTH)
            s.pack(side = tk.RIGHT, fill = tk.BOTH)
            f.pack(side = tk.LEFT)
        self.listbox_frame.pack()
        self.set_widgets()

class AboutFrame:
    def __init__(self,master ,ps):
        self.ps = ps
        self.master = master 
        self.widget = ttk.Frame(self.master)
        self.app_name_label = ttk.Label(
            self.widget,text = app_name,font=("", 50),foreground= '#ed0ed7')
        self.app_version_label = ttk.Label(
            self.widget,text = app_version,font=("", 20),foreground= '#ed330e')
        self.app_url_label = ttk.Label(
            self.widget,text = app_url,font=("", 15),foreground= '#0e2bed',
            cursor= "hand2",)
        self.app_contributors_frame = ttk.Frame(self.widget)
        self.app_contributors_text = tk.Text(self.app_contributors_frame,bd=0,
            height = 9,width = 35)
        self.app_contributors_scrollbar = tk.Scrollbar(
            self.app_contributors_frame)
        
    def set_commands(self):
        self.app_url_label.bind(
            "<Button-1>",lambda e:webbrowser.open(app_url))
    
    def set_widgets(self):
        self.app_contributors_text.insert(
            tk.END, 'Author:'+'\n'+app_contributors[0]+'\n'+\
            'Contributors:'+('\n'.join(app_contributors[1:]))+'\n'+\
            'Sponsors:'+('\n'.join(app_sponsors)))
        self.app_contributors_text.config(
            yscrollcommand =self.app_contributors_scrollbar.set,
            state="disabled",font = ('',15),foreground= '#d80eed')
        self.app_contributors_text.tag_configure(\
            "contributors", justify=tk.CENTER)
        self.app_contributors_text.tag_add("contributors", "1.0", tk.END)
        self.app_contributors_scrollbar.config( \
            command= self.app_contributors_text.yview)


    def set_layout(self):
        self.set_widgets()
        self.set_commands()
        self.app_contributors_text.pack(side = tk.LEFT)
        self.app_contributors_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)
        self.app_name_label.pack()
        self.app_version_label.pack()
        self.app_url_label.pack()
        self.app_contributors_frame.pack( )
        


class MainNotebook:
    def __init__(self,master,ps):
        self.ps = ps
        self.master = master 
        self.widget= ttk.Notebook(master)
        self.main_frame = MainFrame(self.widget,ps)
        self.about_frame = AboutFrame(self.widget,ps)
    
    def add(self):
        self.widget.add(self.main_frame.widget,text = app_name )
        self.widget.add(self.about_frame.widget,text = _('About'))
    
    def set_widgets(self):
        self.add()

    def set_layout(self):
        self.set_widgets()
        self.main_frame.set_layout()
        self.about_frame.set_layout()
        self.widget.pack(expand = True, fill=tk.BOTH)

class PrimarySchool:
    def __init__(self):
        self.master = tk.Tk()
        self.app_name_version = app_name+'('+app_version+')'
        self.scr_w =self.scr_width =  self.master.winfo_screenwidth()
        self.scr_h =self.scr_height =  self.master.winfo_screenheight()
        self.m_w =self.master_width =  self.get_scr_w_x()
        self.m_h =self.master_height =  self.get_scr_h_x()
        self.main_notebook = MainNotebook(self.master,self)   

    
    def get_scr_w_times(self,num=0.7):
        return self.get_scr_w_x(num)

    def get_scr_h_times(self,num=0.7):
        return self.get_scr_h_x(num)   
    
    def get_scr_w_x(self,num=0.7):
        return int(self.scr_w*num)

    def get_scr_h_x(self,num=0.7):
        return int(self.scr_h*num)    
    
    def get_master_geometry(self):
        _x = int((self.scr_w-self.m_w)/2)
        _y = int((self.scr_h-self.m_h)/2)
        return '%sx%s+%s+%s'%(self.m_w,self.m_h,_x,+_y)
    
    def set_widgets(self):
        self.master.title(self.app_name_version)
        self.master.geometry(self.get_master_geometry())
        self.master.resizable(0,0)
        self.main_notebook.widget.pack(
            fill = tk.BOTH,
        )
        self.main_notebook.set_layout()

    def _mainloop(self):
        pass

    def mainloop(self):
        self._mainloop()
        self.set_widgets()
        self.master.mainloop()


def go():
    PrimarySchool().mainloop()
    pass

