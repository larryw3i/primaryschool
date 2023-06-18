import primaryschool
from primaryschool import *

psgames_dir_path = Path(__file__).parent


def get_game_module_names(self):
    game_module_names = [
        d for d in os.listdir(str(psgames_dir_path)) if d.startswith("game_")
    ]
    return game_module_names
    pass


def get_game_list():
    game_list = None
    return game_list
    pass


def get_game_name_list():
    rame_name_list = None
    return game_name_list
    pass


def get_game_names():
    return get_game_name_list()


def get_game_difficulty_list(game_name=None):
    if not game_name:
        return []
    game_difficulty_list = None
    return game_difficulty_list
    pass


def get_game_difficulties(*args, **kwargs):
    return get_game_difficulty_list(*args, **kwargs)


pass
