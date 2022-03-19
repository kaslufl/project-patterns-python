from .race import Race
from .profession import Profession
from .abstract_factory import AbstractFactory

class Player:
    "Class to represent a player"

    def __init__(self, factory: AbstractFactory) -> None:
        self.race: Race = factory.get_race()
        self.profession: Profession = factory.get_profession()

    def attack(self) -> str:
        return self.profession.attack()

    def get_race(self) -> str:
        return self.race.get_name()
