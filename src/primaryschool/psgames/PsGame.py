from abc import ABC

import primaryschool
from primaryschool import *


class PsGameABC(ABC):
    def __init__(self, name=None, difficulties=None):
        self.difficulties = difficulties
        self.name = name

    def get_difficulties(self):
        if not self.difficulties:
            self.difficulties = []
        return self.difficulties
        pass

    def set_name(self, name=None):
        if not name:
            return
        self.name = name
        pass

    def get_name(self):
        if not self.name:
            self.name = str(uuid.uuid4())
        return self.name

        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    def hell0(self):
        print(_("Hello!"))
        pass

    pass


def get_game_list():
    game_list = []
    return game_list
    pass


def get_game_name_list():
    game_name_list = []
    return game_name_list
    pass


def get_game_difficulties(name=None):
    if not name:
        return None
    difficulties = []
    pass


if __name__ == "__main__":
    print(_("Testing . . ."))
    pass


pass
