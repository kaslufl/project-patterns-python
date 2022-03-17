from .abstract_factory import AbstractFactory
from .orc import Orc
from .mage import Mage

class OrcMageFactory(AbstractFactory):

    def get_race(self) -> Orc:
        return Orc()

    def get_profession(self) -> Mage:
        return Mage()
