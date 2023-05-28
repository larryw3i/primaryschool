import primaryschool
from primaryschool import *

psgames_dir_path = Path(__file__).parent

def get_game_module_names(self):
    game_module_names = d for d in  os.listdir(str(psgames_dir_path)) \
        if d.startswith("game_")
    return game_module_names
    pass

def get_game_list():
    game_list = None
    return game_list
    pass


def get_game_names():
    game_names = None
    return game_names
    pass


def get_game_difficulties(game_name=None):
    if not game_name:
        return []
    game_difficulties = None
    return game_difficulties
    pass


pass
