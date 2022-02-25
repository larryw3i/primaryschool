
import copy
import os
import pickle
import random
import sys
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Any, List, Optional, Sequence, Text, Tuple, Union, overload

import pygame
import pygame_menu
from pygame.key import key_code
from pygame.locals import *
from xpinyin import Pinyin

from primaryschool._abc_ import GameBase
from primaryschool.dirs import *
from primaryschool.locale import _, sys_lang_code
from primaryschool.resource import (default_font, default_font_path,
                                    get_default_font, get_font_path)
from primaryschool.subjects import *


class Target(self):
    def __init__(self, content, key):
        self.content = content
        self.key = key


class TargetManager(self):
    def __init__(self):
        ...


class ShootingBase(GameBase):
    def __init__(self, module_str,):
        self.module_str = module_str
        ...

    def load(self):
        ...

    def save(self):
        ...

    def play(self):
        ...

    def start(self):
        ...

    def _start(self):
        ...
