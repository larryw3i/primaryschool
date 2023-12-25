import gettext
import locale
import os
import subprocess
import sys
from pathlib import Path

import primaryschool

sys_lang_code = locale.getdefaultlocale()[0]

locale_path = locale_dir_path = Path(os.path.abspath(os.path.dirname(__file__)))
project_path = Path(__file__).parent.parent.parent.absolute()
lc_messages_path = Path(locale_dir_path) / "en_US" / "LC_MESSAGES"

po0_path = lc_messages_path / "primaryschool.po"

mo0_path = lc_messages_path / "primaryschool.mo"

if not os.path.exists(mo0_path):
    print(
        f"It seems you run 'primaryschool' via development mode. "
        + f"'{mo0_path}' doesn't exist. Try to compile it..."
    )
    for root, dirs, files in os.walk(lc_messages_path.as_posix()):
        for f in files:
            if f.endswith(".po"):
                po_file_path = Path(root, f)
                mo_file_path = po_file_path.with_suffix(".mo")
                os.system(f"msgfmt -vv -o {mo_file_path} {po_file_path}")
        pass

    # subprocess.Popen(
    #    f"cd {project_path};"
    #    + f". {project_path}/primaryschoo1.sh msg_fmt;"
    #    + f'echo "Compile successfully!"',
    #    shell=True,
    # )

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
