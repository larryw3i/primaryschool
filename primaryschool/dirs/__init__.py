import importlib
import os
import uuid
from pathlib import Path

from appdirs import AppDirs

from primaryschool.settings import app_author, app_name, app_version

project_path = str(Path(__file__).parent.parent.parent.absolute())
_dirs = AppDirs(app_name, app_author)

user_data_dir_path = Path(_dirs.user_data_dir)
user_cache_dir_path = Path(_dirs.user_cache_dir)
user_log_dir_path = Path(_dirs.user_log_dir)
user_config_dir_path = Path(_dirs.user_config_dir)

user_screenshot_dir_path = os.path.join(user_data_dir_path, "screenshots")

for d in [
    user_data_dir_path,
    user_cache_dir_path,
    user_log_dir_path,
    user_config_dir_path,
    user_screenshot_dir_path,
]:
    if not d.exists():
        os.makedirs(str(d), exist_ok=True)


def get_copy_path(game_module_name=None, _format="toml"):
    cp_path = (
        (user_data_dir_path / game_module_name)
        if game_module_name
        else user_config_dir_path
    )

    return cp_path


def get_default_screenshot_path(module_str, player_name):
    _uuid = str(uuid.uuid4())
    return os.path.join(
        user_screenshot_dir_path, f"{module_str}.{player_name}.{_uuid}.png"
    )
