
import importlib
import os
import sys

from primaryschool.locale import _

subject_path = os.path.abspath(os.path.dirname(__file__))


def get_subjects():
    subjects = []
    for p in os.listdir(subject_path):
        if p.startswith('__'):
            continue
        subject = importlib.import_module(
            f'primaryschool.subjects.{p}')
        subjects.append(p)
    return  subjects


class SubjectGame():
    def __init__(self, win):
        print(win.difficulty, win.subject)

    def update():
        pass
