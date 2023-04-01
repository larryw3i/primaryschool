
import sys
import argparse

import primaryschool
from primaryschool.l10n import _
from primaryschool.requirements import *



parser = argparse.ArgumentParser(
    prog=_("primaryschool's requirements"),
    add_help=True,
    description=_("The requirements of primaryschool."),
)

parser.add_argument(
    '--prn',
    action='store_true',
    help=_("Print the latest requirements' name for PYPI."))

args = parser.parse_args()
print_requirements = args.prn

if print_requirements:
    print_latest_requirements_name_for_pypi()

pass

