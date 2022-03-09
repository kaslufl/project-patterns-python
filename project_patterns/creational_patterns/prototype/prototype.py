from abc import ABC, abstractmethod


class Prototype(ABC):
    "Class to represent a Prototype"

    def __init__(self):
        self.attack = None
        self.defense = None
        self.hit_points = None

    @abstractmethod
    def clone(self):
        pass
