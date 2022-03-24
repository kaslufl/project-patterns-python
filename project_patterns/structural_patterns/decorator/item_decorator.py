from .item import Item


class ItemDecorator(Item):
    "Class to represent an item decorator"

    item: Item

    def __init__(self, item):
        self.item = item

    def get_info(self):
        return f"Name: {self.get_name()} Att: {self.get_attack()} Val: {self.get_value()}"

    def get_name(self) -> str:
        return self.item.get_name()

    def get_attack(self) -> int:
        return self.item.get_attack()

    def get_value(self) -> int:
        return self.item.get_value()
