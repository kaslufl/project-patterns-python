from .profession import Profession


class Mage(Profession):
    "Class to represent a person who shots fireballs"

    def get_name(self) -> str:
        return self.__class__.__name__

    def attack(self) -> str:
        return "Fireball"
