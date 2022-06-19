from abc import ABCMeta, abstractmethod


class Attack(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def attack():
        pass
