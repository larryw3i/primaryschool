import importlib
import os
import sys
import argparse
from pathlib import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from primaryschool.l10n import _

project_path = os.path.abspath(os.path.dirname(__file__))

parser = argparse.ArgumentParser(
    prog="primaryschool", description=_("Have fun with primaryschool.")
)

parser.add_argument(
    "-s", "--start", action="store_true", help=_("Start main program.")
)
parser.add_argument("-v", "--verbose", help=_("Show verbose information."))

args = parser.parse_args()


