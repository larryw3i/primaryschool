
from abc import ABC, abstractmethod


class GameBase(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def save(self):

        ...

    @abstractmethod
    def load(self):

        ...

    @abstractmethod
    def start(self):
        ...
