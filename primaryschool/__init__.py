import importlib
import os
from pathlib import *

project_path = os.path.abspath(os.path.dirname(__file__))


def victory():
    from primaryschool import ready

    ready.go()
    pass
