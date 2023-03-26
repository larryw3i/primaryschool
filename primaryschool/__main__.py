import importlib
import os
import sys
import argparse
from pathlib import *

project_path = Path(__file__).parent.absolute()

if not project_path in sys.path:
    sys.path.append(project_path)

from primaryschool.l10n import _
from primaryschool.settings import app_version,app_name


parser = argparse.ArgumentParser(
    prog=app_name, description=_(f"Have fun with {app_name}.")
)

parser.add_argument(
    "-s", "--start", action="store_true", help=_("Start main program.")
)


parser.add_argument("--verbose", "-v", action="count", default=0)


parser.add_argument(
    "-V",
    "--version",
    action="version",
    version="%(prog)s " + app_version,
    help=_("Print version."),
)
args = parser.parse_args()

start_signal = args.start
verbose = args.verbose

if len(sys.argv[1:]) <1 or start_signal:
    print(f"Have fun with {app_name} {app_version}.")



pass
