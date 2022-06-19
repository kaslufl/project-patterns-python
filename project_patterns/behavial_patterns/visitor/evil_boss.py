from .armor import Armor
from .weapon import Weapon


class EvilBoss:

    def __init__(self):
        self._equipment = [
            Weapon("Sword of Destiny", 100, -1),
            Armor("Black Helmet", 0, 50)
        ]

    def accept(self, visitor):
        for equipment in self._equipment:
            equipment.accept(visitor)
