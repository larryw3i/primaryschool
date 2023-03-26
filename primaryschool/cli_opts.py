
import getopt
from primaryschool.locale import _

# https://docs.python.org/3/library/getopt.html


def get_shortopts_with_comment():
    shortopts = [
        ("s", _("Run/Start this application.")),
        ("h", _("Shows help information.")),
        ("v", _("Shows version.")),
        ("t", _("Print tests information."))
    ]
    return shortopts


def get_shortopts():
    shortopts = get_shortopts_with_comment()
    shortopts = [s[0] for s in shortopts]
    shortopts = ''.join(shortopts)
    return shortopts


def get_longopts_with_comment():
    longopts = [
        ("hello", _("Say hello to you."))
    ]
    return longopts


def get_longopts():
    longopts = get_longopts_with_comment()
    longopts = [o[0] for o in longopts]
    return longopts


def print_opts_comment():
    shortopts = get_shortopts_with_comment()
    longopts = get_longopts_with_comment()
    opts = shortopts + longopts
    max_opt_len = max([len(o[0]) for o in opts])
    max_opt_len += max_opt_len % 4

    for o in opts:
        print(f"{o:{max_opt_len}.<}") 
    pass
