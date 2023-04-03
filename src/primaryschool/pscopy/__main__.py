import sys

from primaryschool import *
from primaryschool.pscopy import *


def test():
    print_nl(
        _("Get `ps_cp_path`."),
        ps_cp_path,
        "Testing get_ps_copy().",
        get_ps_copy(),
        "Testing set_ps_copy().",
        set_ps_copy({"Test": "Hello, World!"}),
    )
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
