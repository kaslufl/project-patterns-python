from abc import ABC, abstractmethod

class Serializer(ABC):
    "Class to define a serializer"

    def __init__(self):
        self._current_object = None

    @abstractmethod
    def start_object(self):
        pass

    @abstractmethod
    def add_property(self):
        pass

    @abstractmethod
    def to_str(self):
        pass
