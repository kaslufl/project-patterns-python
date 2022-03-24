from abc import ABC, abstractmethod


class Component(ABC):
    "Abstract class to define composite and leaf common methods"

    @abstractmethod
    def operation(self):
        pass
