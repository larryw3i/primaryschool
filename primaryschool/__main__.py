import importlib
import os
import sys
import argparse
from pathlib import *

project_path = str(Path(__file__).parent.parent.absolute())
if not project_path in sys.path:
    sys.path.append(project_path)

from primaryschool.l10n import _
from primaryschool.settings import app_version, app_name

help_text = _("show this help message and exit")

parser = argparse.ArgumentParser(
    prog=app_name,
    description=_("Have fun with {app_name}.").format(app_name=app_name),
    epilog=_("\(^_^)/Yea!"),
)

parser.add_argument(
    "-s", "--start", action="store_true", help=_("Start main program.")
)


parser.add_argument(
    "-v",
    "--verbose",
    action="count",
    default=0,
    help=_("Show verbose messages."),
)


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

if len(sys.argv[1:]) < 1 or start_signal:
    print(
        _("Have fun with {app_name} {app_version}.").format(
            app_name=app_name, app_version=app_version
        )
    )
    if verbose > 0:
        print(f"Start program with verbose={verbose}.")


pass
