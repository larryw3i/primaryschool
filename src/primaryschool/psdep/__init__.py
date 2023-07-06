import importlib
import os
from pathlib import *

# from primaryschool.psl10n import _

project_path = os.path.abspath(os.path.dirname(__file__))
pypitxt_path = Path(__file__).parent / "pypi.txt"


install_prefix = "python -m pip install "


def get_requirements_for_apt():
    """For python 3.11, the Python environment is externally managed by default
    , so python packages should be installed via `apt`.
    The Format of requirements:
    ```python3
    [
        (
            "package_name",
            "package_version(N/A)",
            "package_url",
            "license",
            "license_url"),
    ]
    ```
    """
    requirements = [
        (
            "python3-pygame",
            None,
            "https://www.pygame.org/" "GNU LGPL version 2.1",
            "https://github.com/pygame/pygame/blob/main/docs/LGPL.txt",
        ),
        (
            "python3-appdirs",
            None,
            "https://github.com/ActiveState/appdirs",
            "MIT",
            "https://github.com/ActiveState/appdirs/blob/master/LICENSE.txt",
        ),
        (
            "python3-toml",
            None,
            "https://github.com/uiri/toml",
            "MIT license",
            "https://github.com/uiri/toml/blob/master/LICENSE",
        ),
    ]
    return requirements
    pass


def get_requirements_for_pypi():
    """
    Return the requirements for installing 'primaryschool' via 'pypi'.
    """
    requirements = None
    with open(str(pypitxt_path), "r") as f:
        requirements = f.read()
        pass
    requirements = requirements.strip().replace("\\\n", "")
    requirements = [rs for rs in requirements.split("\n\n")]
    requirements = [r.split("\n") for r in requirements]
    for r in requirements:
        if r[1] == "None":
            r[1] = None
    return requirements
    pass


def get_requirements_for_dnf():
    requirements = [("")]
    return requirements
    pass


def get_requirements_for_yourself():
    requirements = None
    print(
        _(
            "Feel free to contribute the code at "
            + "`https://github.com/larryw3i/primaryschool`."
        )
    )
    return requirements
    pass


def get_requirements_product():
    install_requires = []
    for r in requirements[0]:
        install_requires.append(r[0] + r[1])
    return install_requires


def install_requirements_product():
    requirements_product = get_requirements_product()
    os.system(install_prefix + requirements_product)
    pass


def get_latest_requirements_for_pypi():
    requirements = get_requirements_for_pypi()
    requirements = [(r[0], None) for r in requirements]
    return requirements
    pass


def get_latest_requirements_name_for_pypi():
    requirements = get_requirements_for_pypi()
    requirements = [r[0] for r in requirements]
    return requirements
    pass


def get_requirements_name_with_version_for_pypi():
    requirements = get_requirements_for_pypi()
    requirements = [
        (r[0] + f"'{r[1]}'") if r[1] else r[0] for r in requirements
    ]
    return requirements
    pass


def print_latest_requirements_name_for_pypi():
    requirements = get_latest_requirements_name_for_pypi()
    print(" ".join(requirements))
    pass


req_names_pypi = get_latest_requirements_for_pypi()
deps = (
    setup_reqs
) = req_names_with_version_pypi = get_requirements_name_with_version_for_pypi()

deps_full = deps_with_full_info = get_requirements_for_pypi()

pass


