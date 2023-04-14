from abc import ABC

from primaryschool import *


class PsWidget(ABC):
    def __init__(self):
        self.set_ps_cp = self.set_ps_copy = set_ps_copy
        self.pscp = pscp
        pass

    def save_ps_cp(self):
        self.set_ps_cp(self.pscp)
        pass

    def save_ps_copy(self, *args, **kwargs):
        self.save_ps_cp(*args, **kwargs)
        pass

    pass


pass
