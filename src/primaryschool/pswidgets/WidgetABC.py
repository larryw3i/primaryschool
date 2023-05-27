from abc import ABC

from primaryschool import *


class PsWidget(ABC):
    def __init__(self, verbose=False):
        self.set_ps_cp = self.set_ps_copy = set_ps_copy
        self.pscp = pscp
        self.verbose = verbose
        pass

    def save_ps_cp(self):
        self.set_ps_cp(self.pscp)
        pass

    def save_ps_copy(self, *args, **kwargs):
        self.save_ps_cp(*args, **kwargs)
        pass

    pass


pass


class PsSubToplevel(PsWidget):
    def __init__(self, top_widget=None):
        if not top_widget:
            print(_("TopWidget is None."))
        pass


class PsSubWidget(PsWidget):
    def __init__(self, top_widget=None):
        super().__init__()
        if not top_widget:
            print(_("TopWidget is None."))
        self.top_widget = top_widget
        self.sibling_widgets = (
            self.sibling_widget_list
        ) = top_widget.get_subwidgets()
        if not self in self.sibling_widgets:
            self.top_widget.add_subwidget(self)
        pass

    def place(self):
        pass

    pass


pass
