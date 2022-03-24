from abc import ABC, abstractmethod


class Item(ABC):
    "Abstract class to represent a game item"

    def get_info(self):
        pass

    def get_name(self):
        pass

    def get_attack(self):
        pass

    def get_value(self):
        pass
