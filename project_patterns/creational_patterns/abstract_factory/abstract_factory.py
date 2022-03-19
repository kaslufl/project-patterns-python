from abc import ABC, abstractmethod

from .profession import Profession
from .race import Race

class AbstractFactory(ABC):
    "Class to represent an AbstracFactory"

    @abstractmethod
    def get_race(self) -> Race:
        pass

    @abstractmethod
    def get_profession(self) -> Profession:
        pass
