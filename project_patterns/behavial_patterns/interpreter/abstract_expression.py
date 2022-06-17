from abc import ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def interpret():
        pass
