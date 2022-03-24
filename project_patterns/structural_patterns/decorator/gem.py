from .item_decorator import ItemDecorator


class Gem(ItemDecorator):
    "Class to represent a gem that can be placed on an item"

    def get_attack(self) -> int:
        return self.item.get_attack() * 2

    def get_value(self) -> int:
        return self.item.get_value() + 20
