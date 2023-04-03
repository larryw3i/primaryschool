import argparse
import getopt
import json
import sys
from pathlib import Path

import toml

project_path = Path(__file__).parent / "src"
if not str(project_path) in sys.path:
    print(f"Add '{str(project_path)}' to 'sys.path'.")
    sys.path.append(str(project_path))


import primaryschool
from primaryschool import *

_ = str


parent_path = Path(__file__).parent
pyproject_toml_path = parent_path / "pyproject.toml"
pyproject0_toml_path = parent_path / "pyproject0.toml"
pyproject = None


def get_pyproject(_read=False, cp=False):
    global pyproject
    if (not _read) and pyproject:
        return pyproject
    with open(pyproject0_toml_path if cp else pyproject_toml_path, "r") as f:
        pyproject = toml.loads(f.read())

    return pyproject
    pass


def update_pyproject_toml():
    global pyproject_toml_path
    pyproject = get_pyproject(cp=True)
    pyproject["project"]["name"] = app_name
    pyproject["project"]["version"] = app_version
    pyproject["project"]["dependencies"] = deps
    pyproject["project"]["authors"] = app_authors
    pyproject["project"]["urls"]["Source"] = project_url
    pyproject["project"]["description"] = project_description
    with open(pyproject_toml_path, "w") as f:
        toml.dump(pyproject, f)
    print("Update completed.")
    pass


def print_pyproject_toml():
    print(json.dumps(get_pyproject(), indent=4))
    pass


parser = argparse.ArgumentParser(
    prog=_("primaryschool.py"),
    add_help=True,
    description=_("Some unitls for primaryschool."),
)


parser.add_argument(
    "-t",
    "--test",
    action="store_true",
    help=_("Run the testings."),
)

parser.add_argument(
    "--upptoml",
    action="store_true",
    help=_("Run the testings."),
)


def test():
    print("print_pyproject_toml")
    print_pyproject_toml()


argv = sys.argv[1:]
if len(argv) < 1:
    pass

args = parser.parse_args()
run_test = args.test
upptoml = args.upptoml

if upptoml:
    update_pyproject_toml()
    exit()

if run_test:
    test()
    exit()


pass
