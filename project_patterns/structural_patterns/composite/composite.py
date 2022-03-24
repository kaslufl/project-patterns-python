from .component import Component


class Composite(Component):
    "Class to represent a Composite component"

    name: str

    def __init__(self, name) -> None:
        self.name = name
        self.children = []

    def operation(self) -> str:
        details = f'{self.name}'
        for child in self.children:
            details = details + '\n\t' + child.operation()
        return details

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)
