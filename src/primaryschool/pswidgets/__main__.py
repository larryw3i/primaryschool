import sys

from primaryschool import *
from primaryschool.pswidgets import *


def test():
    top_widget = TopWidget(mainloop=False)
    root_widget = top_widget.rootw
    mainframe = top_widget.mainframe
    for i in range(20):
        ttk.Button(mainframe, text=str(i) * 5).pack(side=LEFT)
        pass

    for i in range(20):
        ttk.Button(mainframe, text=str(i) * 5).pack(side=TOP)
        pass

    top_widget.mainloop()
    print_nl()
    pass


parser = argparse.ArgumentParser(
    prog=_("primaryschool.pswidgets"),
    description=_("The `pswidgets` module of primaryschool."),
    add_help=True,
)

parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()

mk_test = args.test

if mk_test:
    test()
    exit()
