import sys
from pathlib import Path

import primaryschool
from primaryschool import *

ps_cp_path = get_copy_path()


def get_ps_copy():
    pscp = None
    with open(ps_cp_path, "r") as f:
        pscp = toml.loads(f.read())
    return pscp
    pass


def set_ps_copy(pscp=None):
    if not pscp:
        print(_("A copy is required."))
        return
    with open(ps_cp_path, "w") as f:
        toml.dump(pscp, f)
    pass


def get_game_copy(game_name=None):
    if not game_name:
        print(_("A game name is required."))
        return None
    psgcp = None
    game_cp_path = get_game_cp_path(game_name=game_name)
    if not game_cp_path.exists:
        with open(game_cp_path, "w") as f:
            toml.dump({}, f)
        return {}
    with open(game_cp_path, "r") as f:
        psgcp = toml.loads(f.read())
    return psgcp
    pass


pass
