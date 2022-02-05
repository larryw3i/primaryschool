
import os
import sys

from primaryschool.locale import _
from primaryschool.subjects import *

name = _('Yuwen')


class YuwenGame(SubjectGame):
    def __init__(self, win):
        super().__init__(win)

    pass


def start(win):
    YuwenGame(win)
    pass
