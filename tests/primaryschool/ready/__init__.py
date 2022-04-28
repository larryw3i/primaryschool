
import pygame
from primaryschool.ready import PrimarySchool

class PrimarySchoolTest(PrimarySchool):
    def __init__(self):
        self.surface = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        super().__init__()