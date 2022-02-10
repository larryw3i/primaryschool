
import os
import sys
from importlib import import_module

from primaryschool.locale import _

subject_module_prefix = 'primaryschool.subjects.'
subject_path = os.path.abspath(os.path.dirname(__file__))

def get_game_modules():
    modules = []
    for _subject in os.listdir(subject_path):
        _subject_path = os.path.join(subject_path, _subject)
        if not _subject_path.startswith('s_'):
            continue
        for _game in os.listdir(_subject_path):
            if not _game.startswith('g_'):
                continue
            modules.append(f'{subject_module_prefix+_subject}.{_game}')
    return modules

game_modules = get_game_modules()

def get_subjects():
    return [p for p in os.listdir(subject_path) if not p.startswith('__')]


def get_subjects_t():
    return [
        import_module(f'primaryschool.subjects.{m}').name
        for m in get_subjects()
    ]




class Game():
    def __init__(self,module_str):
        self.module_str = module_str
        self.module = import_module(self.module_str)
        self.name = self.get_name()
        self.name_t = self.get_name_t()
        self.difficulties = self.get_difficulties() 
    
    def get_difficulties(self):
        self.difficulties = self.module.difficulties
    
    def get_name_t(self):
        return self.module.name

    def get_name(self):
        return self.module_str.split('.')[-1]
    
    def play(self):
        self.module.play()

class Subject():
    def __init__(self):
        self.subjects = self.get_subjects()
        self.game_modules = self.get_game_modules()
        self.default_game = 

    def get_game_modules(self):
        modules = []
        for _subject in os.listdir(subject_path):
            _subject_path = os.path.join(subject_path, _subject)
            if not os.path.isdir(_subject_path):
                continue
            if _subject_path.startswith('_'):
                continue
            for _game in os.listdir(_subject_path):
                if not _game.startswith('g_'):
                    continue
                modules.append(
                    (_game,f'{subject_module_prefix+_subject}.{_game}'))
        return modules

    def get_subjects(self):
        subjects = []
        for m in self.game_modules:
            _subject = m.split('.')[-2]
            _subject_t = import_module(
                subject_module_prefix + _subject).name
            subjects.append(_subject, _subject_t)
        return subjects

    def get_difficulties_by_game(self, game_name):
        for m in self.game_modules:
            if m.endswith(game_name):
                return import_module(m).difficulties

    def get_games_by_subject(self, subject_name):
        games = []
        for m in self.game_modules:
            _subject = m.split('.')[-2]
            _game = m.split('.')[-1]
            if _subject == subject_name:
                _game_t = import_module(m).name
                games.append((_game, _game_t, m))
        return games


class SubjectGame():
    def __init__(self, win):
        pass

    def update():
        pass
