import getopt
from pathlib import *
from primaryschool.settings import *


def get_dev_requirements_for_pypi():

    requirements = [
        (
            "black",
            None,
            "https://github.com/psf/black",
            "MIT license",
            "https://github.com/psf/black/blob/main/LICENSE",
        ),
        (
            "pre-commit",
            None,
            "https://github.com/pre-commit/pre-commit",
            "MIT license",
            "https://github.com/pre-commit/pre-commit/blob/main/LICENSE",
        ),
    ]
    requirements += get_requirements_for_pypi()
    return requirements
    pass


def get_latest_dev_requirements_for_pypi():
    requirements = get_dev_requirements_for_pypi()
    for r in requirements:
        r[1] = None
    requirements += get_latest_requirements_for_pypi()
    return requirements
    pass


def get_opt_shortopts_with_comment():
    shortopts = [("t", _("`t` for testing."))]


if __name__ == "__main__":
    print("Have fun!")
    pass
