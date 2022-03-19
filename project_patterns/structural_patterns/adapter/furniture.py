from abc import ABC, abstractmethod


class Furniture(ABC):
    "Abstract clads to represent furniture"

    def get_model(): pass

    def get_height(): pass

    def get_width(): pass
