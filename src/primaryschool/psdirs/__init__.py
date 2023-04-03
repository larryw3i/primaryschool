import importlib
import os
import uuid
from pathlib import Path

from appdirs import AppDirs

from primaryschool.pssettings import app_author, app_name, app_version

project_path = str(Path(__file__).parent.parent.parent.absolute())
_dirs = AppDirs(app_name, app_author)

user_data_dir_path = Path(_dirs.user_data_dir)
user_cache_dir_path = Path(_dirs.user_cache_dir)
user_log_dir_path = Path(_dirs.user_log_dir)
user_config_dir_path = Path(_dirs.user_config_dir)

user_screenshot_dir_path = Path(
    os.path.join(user_data_dir_path, "screenshots")
)

for d in [
    user_data_dir_path,
    user_cache_dir_path,
    user_log_dir_path,
    user_config_dir_path,
    user_screenshot_dir_path,
]:
    if not d.exists():
        os.makedirs(str(d), exist_ok=True)


def get_copy_path(game_module_name=None, mk_ifnot_exists=True):
    cp_path = (
        (user_data_dir_path / game_module_name)
        if game_module_name
        else user_config_dir_path
    )
    cp_path = cp_path / "copy.toml"
    if mk_ifnot_exists:
        if not cp_path.exists():
            with open(str(cp_path), "w") as f:
                toml.dump({}, f)

    return cp_path
    pass


def get_game_module_copy_path(game_module_name=None):
    if not game_module_name:
        return None
    cp_path = get_copy_path(game_module_name=game_module_name)
    return cp_path
    pass


def get_default_screenshot_path(module_str, player_name):
    _uuid = str(uuid.uuid4())
    return os.path.join(
        user_screenshot_dir_path, f"{module_str}.{player_name}.{_uuid}.png"
    )


get_cp_path = get_copy_path
get_game_cp_path = get_game_copy_path = get_game_module_copy_path

get_screenshot_path0 = get_default_screenshot_path


pass
