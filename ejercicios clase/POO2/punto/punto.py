from abc import ABC, abstractmethod
class Punto (ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x():
        return self._x