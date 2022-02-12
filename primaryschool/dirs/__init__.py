

import importlib
import os

from appdirs import AppDirs

_dirs = AppDirs("SuperApp", "Acme")

user_data_dir_path = _dirs.user_data_dir
user_cache_dir_path = _dirs.user_cache_dir
user_log_dir_path = _dirs.user_log_dir
user_config_dir_path = _dirs.user_config_dir
