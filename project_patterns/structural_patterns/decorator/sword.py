from .item import Item


class Sword(Item):
    "Class to represent an item category"

    name: str
    attack: int
    value: int

    def __init__(self, name, attack, value) -> None:
        self.name = name
        self.attack = attack
        self.value = value

    def get_info(self) -> str:
        return f"Name: {self.get_name()} Att: {self.get_attack()} Val: {self.get_value()}"

    def get_name(self) -> str:
        return self.name

    def get_attack(self) -> int:
        return self.attack

    def get_value(self) -> int:
        return self.value
