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


class PsSubToplevel(PsWidget):
    def __init__(self, top_widget=None):
        if not top_widget:
            print(_("TopWidget is None."))
        pass


class PsSubWidget(PsWidget):
    def __init__(self, top_widget=None):
        super().___init__()
        if not top_widget:
            print(_("TopWidget is None."))
        self.sibling_widgets = self.sibling_widget_list = top_widget.subwidgets
        if not self in self.sibling_widgets:
            self.top_widget.add_subwidget(self)
        pass

    pass


pass
