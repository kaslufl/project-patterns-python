from .component import Component


class Leaf(Component):
    "Class to represent a Leaf component"

    name: str

    def __init__(self, name) -> None:
        self.name = name

    def operation(self) -> str:
        return '\t' + self.name
