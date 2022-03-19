from .affinity import Affinity


class Item:
    "Class to represent a game item"
    name: str
    attack: int
    magic: int
    affinity: Affinity

    def __init__(self, name, attack, magic, affinity) -> None:
        self.name = name
        self.attack = attack
        self.magic = magic
        self.affinity = affinity

    def physical_attack(self) -> int:
        return self.attack * self.affinity.physical_modifier

    def magical_attack(self) -> int:
        return self.magic * self.affinity.magical_modifier

    def get_info(self) -> str:
        return f'{self.name} | att: {self.physical_attack()} mag: {self.magical_attack()} aff: {self.affinity.name}'
