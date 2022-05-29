
from abc import ABC

class SubWidgetABC(ABC):
    def __init__(self,ps):
        self.ps = ps
        self.root = self.ps.root