import sys
import getopt
import argparse

import primaryschool
from primaryschool import *
from primaryschool.psl10n import _
from primaryschool.psdep import *

def test():
    print_nl(
        'req_names_pypi',
        req_names_pypi,
        'req_names_with_version_pypi',
        req_names_with_version_pypi
    )

parser = argparse.ArgumentParser(
    prog=_("primaryschool's requirements"),
    add_help=True,
    description=_("The requirements of primaryschool."),
)

parser.add_argument(
    "--prn",
    action="store_true",
    help=_("print the latest requirements' name for pypi."),
)

parser.add_argument(
    "--test",
    action="store_true",
    help=_("Run the testings."),
)


argv = sys.argv[1:]
if len(argv) < 1:
    parser.print_help()
    exit()

args = parser.parse_args()
print_requirements = args.prn
run_test = args.test

if print_requirements:
    print_latest_requirements_name_for_pypi()
    exit()

if run_test:
    test()
    exit()

pass
