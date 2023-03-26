import importlib
import os
from pathlib import *

project_path = os.path.abspath(os.path.dirname(__file__))


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
    ]
    return requirements
    pass


def get_requirements_for_pypi():
    requirements = [
        (
            "pygame",
            None,
            "https://github.com/pygame/pygame",
            "LGPL v2",
            "https://github.com/pygame/pygame/blob/main/docs/LGPL.txt",
        ),
        (
            "appdirs",
            None,
            "https://github.com/ActiveState/appdirs",
            "MIT",
            "https://github.com/ActiveState/appdirs/blob/master/LICENSE.txt",
        ),
    ]
    return requirements
    pass


def get_requirements_for_dnf():
    requirements = [("")]
    return requirements
    pass


def get_requirements_for_yourself():
    requirements = None
    print(
        "Feel free to contribute the code at "
        + "`https://github.com/larryw3i/primaryschool`."
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
    for r in requirements:
        r[1] = None
    return requirements
    pass
