from .serializer import Serializer


class Profile:
    "Class to represents someone profile"

    def __init__(self, id: str, name: str, last_name: str) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name

    def serialize(self, serializer: Serializer):
        serializer.start_object('profile', self.id)
        serializer.add_property('name', self.name)
        serializer.add_property('last_name', self.last_name)
