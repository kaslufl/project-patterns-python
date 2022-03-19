from abc import ABC, abstractmethod


class Profession(ABC):
    "Abstract class to represent professions"

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def attack(self) -> str:
        pass
