from abc import ABC, abstractmethod


class Race(ABC):
    "Abstract class to represent races"

    @abstractmethod
    def get_name(self) -> str:
        pass
