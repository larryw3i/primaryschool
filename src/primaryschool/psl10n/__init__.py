import gettext
import locale
import os
import subprocess
import sys
from pathlib import Path
from babel.messages import frontend as babel

import primaryschool

app_name = "primaryschool"

sys_lang_code = locale.getdefaultlocale()[0]

locale_path = locale_dir_path = Path(os.path.abspath(os.path.dirname(__file__)))
project_path = Path(__file__).parent.parent.parent.absolute()
lc_messages_path = locale_dir_path / "en_US" / "LC_MESSAGES"

po0_path = lc_messages_path / "primaryschool.po"

mo0_path = lc_messages_path / "primaryschool.mo"

if not os.path.exists(mo0_path):
    print(
        f"It seems you run 'primaryschool' via development mode. "
        + f"'{mo0_path}' doesn't exist. Try to compile it..."
    )
    for root, dirs, files in os.walk(locale_path.as_posix()):
        for f in files:
            if f.endswith(".po") and root.endswith("LC_MESSAGES"):
                po_file_path = Path(root, f)
                mo_file_path = po_file_path.with_suffix(".mo")
                local_name = (
                    root.split("/")[-2] if "/" in root else root.split("\\")
                )
                # os.system(f"msgfmt -vv -o {mo_file_path} {po_file_path}")
                os.system(
                    f"pybabel compile"
                    + f" -D {app_name}"
                    + f" -d {locale_path.as_posix()}"
                    + f" -i {po_file_path}"
                    + f" -o {mo_file_path}"
                    + f" -l {local_name}"
                    + f" --statistics"
                )
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
