
import os
import sys

from primaryschool.locale import _

from primaryschool.subjects import *

name = _('Yuwen')



class YuwenGame(SubjectGame):
    pass



def start(win):
    YuwenGame(win)
    pass
