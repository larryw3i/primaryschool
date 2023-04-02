import primaryschool
from primaryschool import *


def print_nl(*argv):
    ptab = False
    for a in argv:
        if ptab:
            print("    ", a)
        else:
            print(a)
        ptab = not ptab
