
import importlib
import os
import sys

from primaryschool.locale import _

subject_path = os.path.abspath(os.path.dirname(__file__))


def list_subjects():
    subjects = []
    for p in os.listdir(subject_path):
        if p.startswith('__'):
            continue
        subject = importlib.import_module(
            f'primaryschool.subjects.{p}')
        subjects.append(subject.name)
    return subjects
