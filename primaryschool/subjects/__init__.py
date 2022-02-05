
import importlib
import os
import sys

from primaryschool.locale import _


subject_path = os.path.abspath(os.path.dirname(__file__))


def list_subjects():
    subjects_t = []
    subjects = []
    for p in os.listdir(subject_path):
        if p.startswith('__'):
            continue
        subject = importlib.import_module(
            f'primaryschool.subjects.{p}')
        subjects_t.append(subject.name)
        subjects.append(p)
    return subjects_t, subjects


class SubjectGame():
    def __init__(self, win):
        print(win.difficulty_index, win.subject_index)
        
    def update():
        pass
