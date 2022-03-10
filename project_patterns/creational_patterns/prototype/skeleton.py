import copy
from .prototype import Prototype


class Skeleton(Prototype):
    "A basic skeleton"

    def __init__(self, attack: int, defense: int, hit_points: int) -> None:
        super().__init__()
        self.attack = attack
        self.defense = defense
        self.hit_points = hit_points
        self.gold = 30

    def clone(self):
        return copy.deepcopy(self)
