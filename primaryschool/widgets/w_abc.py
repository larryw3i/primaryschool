from abc import ABC


class WidgetABC(ABC):
    def __init__(self, ps):
        self.ps = ps
        self.root = self.ps.root
