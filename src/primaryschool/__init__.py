import argparse
import importlib
import os
import sys
import tkinter
from pathlib import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, ttk

import toml
from toml import *
from babel.messages import frontend as babel

from primaryschool.pscopy import *
from primaryschool.psdep import *
from primaryschool.psdirs import *
from primaryschool.psl10n import _
from primaryschool.pssettings import *
from primaryschool.pstest import *

__version__ = "20231225.22.14"

t = T = trans = Trans = tr = Tr = fanyi = FanYi = _

project_path = str(Path(__file__).parent.parent.absolute())

if not project_path in sys.path:
    sys.path.append(project_path)


def get_verbose():
    verbose = os.environ.get(f"{app_name}_verbose", "0")
    verbose = verbose == "1"
    return verbose


def hey_cli():
    print("Hey CLI!")


def hey_gui():
    print("Hey GUI!")


verbose = get_verbose
pass
