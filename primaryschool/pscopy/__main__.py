import sys

from primaryschool import *
from primaryschool.pscopy import *


def test():
    print(ps_cp_path)
    pass


parser = argparse.ArgumentParser(
    prog=_("primaryschool.pscopy"),
    description=_("The `pscopy` module of primaryschool."),
    add_help=True,
)

parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()

mk_test = args.test

if mk_test:
    test()
    exit()
