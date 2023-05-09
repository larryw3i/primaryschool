import gettext
import locale
import os
import subprocess
import sys
from pathlib import Path

import primaryschool

sys_lang_code = locale.getdefaultlocale()[0]
locale_path = locale_dir_path = os.path.abspath(os.path.dirname(__file__))
project_path = str(Path(__file__).parent.parent.parent.absolute())
po0_path = os.path.join(
    locale_dir_path, "en_US", "LC_MESSAGES", "primaryschool.po"
)

mo0_path = os.path.join(
    locale_dir_path, "en_US", "LC_MESSAGES", "primaryschool.mo"
)

if not os.path.exists(mo0_path):
    print(
        f"It seems you run 'primaryschool' via development mode. "
        + f"'{mo0_path}' doesn't exist. Try to compile it."
    )
    subprocess.Popen(
        f"cd {project_path};"
        + f". {project_path}/primaryschoo1.sh msg_fmt;"
        + f'echo "Compile successfully!"',
        shell=True,
    )

locale_langcodes = [
    d
    for d in os.listdir(locale_path)
    if os.path.isdir(os.path.join(locale_path, d))
]

if sys_lang_code not in locale_langcodes:
    sys_lang_code = "en_US"

lang = gettext.translation(
    "primaryschool", localedir=locale_path, languages=[sys_lang_code]
)

lang.install()

_ = lang.gettext

t = T = _
