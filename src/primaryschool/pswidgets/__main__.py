import sys

from primaryschool import *
from primaryschool.pswidgets import *


def test_scrolledframe():
    top_widget = PsGameListWidget(mainloop=False)
    root_widget = top_widget.rootw
    mainframe = top_widget.mainframe

    buttons_l = []
    for i in range(20):
        buttons_l.append(ttk.Button(mainframe, text=str(i) * 5))
        pass
    
    buttons_t = []
    for i in range(20):
        buttons_t.append(ttk.Button(mainframe, text=str(i) * 5))
        pass

    for bl in buttons_l:
        bl.pack(side="left")

    for bt in buttons_t:
        bt.pack(side="top")

    for bt in buttons_t:
        bt.forget()
        bt.destroy()


    for bl in buttons_l:
        bl.forget()
        bl.destroy()


    top_widget.mainloop()   

    pass


def test():
    test_scrolledframe()


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
