
import os
import random
import sys
from typing import Any, List, Optional, Sequence, Text, Tuple, Union, overload

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu._widgetmanager import WidgetManager
from pygame_menu.widgets import *
from xpinyin import Pinyin

from primaryschool.locale import _
from primaryschool.resource import font_path, get_font
from primaryschool.subjects import *
from primaryschool.subjects.yuwen.words import c as zh_c

name = _('Yuwen')
