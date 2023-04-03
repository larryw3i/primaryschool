import argparse
import getopt
import sys

import primaryschool
from primaryschool import *
from primaryschool.psdep import *
from primaryschool.psl10n import _


def test():
    print_nl(
        "req_names_pypi",
        req_names_pypi,
        "req_names_with_version_pypi",
        req_names_with_version_pypi,
        "setup_reqs",
        setup_reqs,
    )

def update_pyproject_toml():
    pass

parser = argparse.ArgumentParser(
    prog=_("primaryschool.py"),
    add_help=True,
    description=_("Some unitls for primaryschool."),
)


parser.add_argument(
    "-t",
    "--test",
    action="store_true",
    help=_("Run the testings."),
)


argv = sys.argv[1:]
if len(argv) < 1:
    pass

args = parser.parse_args()
run_test = args.test


if run_test:
    test()
    exit()

pass
