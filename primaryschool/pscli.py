import getopt
from abc import ABC
from primaryschool.locale import _

# https://docs.python.org/3/library/getopt.html

cli_options = []


class CliOption(ABC):
    def __init__(
        self,
        shortopt=None,
        longopt=None,
        comment=None,
        _help=None,
        require_argument=False,
        _run=None,
    ):
        if not self in cli_options:
            cli_options.append(self)
        self.shortopt = None
        self.longopt = None
        self.comment = None
        self._help = None

    def print_help(self):
        print(self.help)


def get_shortopts_with_comment():
    shortopts = [
        ("s", _("Run/Start this application.")),
        ("h", _("Show help information.")),
        ("V", _("Print version.")),
        ("v", _("Show verbose information.")),
    ]
    return shortopts


def get_shortopts_deprecated():
    shortopts = get_shortopts_with_comment()
    shortopts = [s[0] for s in shortopts]
    shortopts = "".join(shortopts)
    return shortopts


def get_longopts_with_comment():
    longopts = [("hello", _("Print Hello."))("version", _("Print version."))]
    return longopts


def get_longopts_deprecated():
    longopts = get_longopts_with_comment()
    longopts = [o[0] for o in longopts]
    return longopts


def get_shortopts():
    shortopts = "".join(
        (o.shortopt + ":") if o.require_argument else o.shortopt
        for o in cli_options
    )
    pass


def get_longopts():
    longopt = "".join(
        (o.longopt + "=") if o.require_argument else o.longopt
        for o in cli_options
    )
    pass


def print_opts_comment():
    opts = [
        (
            ("-" + o.shortopt if shortopt else "")
            + ("--" + o.longopt if longopt else ""),
            o.comment,
        )
        for o in cli_options
    ]
    max_opt_len = max([len(o[0]) for o in opts])
    max_opt_len += max_opt_len % 4

    for opt, comment in opts:
        print(f"{opt:<{max_opt_len}}:{comment}")
    pass
