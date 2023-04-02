import importlib
import os
import sys
import argparse
import toml
from toml import *
from pathlib import *
from primaryschool.psl10n import _
from primaryschool.psdirs import *

project_path = str(Path(__file__).parent.parent.absolute())

if not project_path in sys.path:
    sys.path.append(project_path)
