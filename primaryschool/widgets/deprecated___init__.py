from primaryschool.widgets.wroot import PSWidget


class PrimarySchool:
    def __init__(self, surface=None):
        if not pygame.get_init():
            pygame.init()
        self.running = True
        self.surface = (
            surface
            or getattr(self, "surface", None)
            or pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        )
        self.w_width, self.w_height = self.surface.get_size()
        self.w_width_of_2 = self.w_width / 2
        self.w_height_of_2 = self.w_height / 2
        self.w_centrex_y = [self.w_width_of_2, self.w_height]
        self.FPS = 30
        self.player_name = _("default_name")
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

    def set_bg_img(self, src_name="0x1.png"):
        self.bg_img = BaseImage(
            get_resource_path(src_name), pygame_menu.baseimage.IMAGE_MODE_FILL
        )

    def get_bg_img(self):
        if not self.bg_img:
            self.set_bg_img()
        return self.bg_img

    def get_default_menu(self, title, **kwargs):
        theme = pygame_menu.themes.THEME_BLUE.copy()
        theme.title_font = theme.widget_font = self.font
        theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        theme.background_color = self.get_bg_img()
        return pygame_menu.Menu(
            title, self.w_width, self.w_height, theme=theme, **kwargs
        )

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


def show():
    PSWidget().mainloop()
    pass
