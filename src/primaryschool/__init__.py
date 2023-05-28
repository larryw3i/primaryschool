import argparse
import importlib
import os
import sys
import tkinter
from pathlib import *
from tkinter import *
from tkinter import messagebox, ttk
from pathlib import Path

import toml
from toml import *

from primaryschool.pscopy import *
from primaryschool.psdep import *
from primaryschool.psdirs import *
from primaryschool.psl10n import _
from primaryschool.pssettings import *
from primaryschool.pstest import *

t = T = trans = Trans = tr = Tr = fanyi = FanYi = _

project_path = str(Path(__file__).parent.parent.absolute())

if not project_path in sys.path:
    sys.path.append(project_path)


def get_verbose():
    verbose = os.environ.get(f"{app_name}_verbose", "0")
    verbose = verbose == "1"
    return verbose


verbose = get_verbose
pass
