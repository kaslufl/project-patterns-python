from abc import ABCMeta, abstractmethod


class Dispenser(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def next_successor(successor):
        pass

    @staticmethod
    @abstractmethod
    def handle(amount):
        pass
