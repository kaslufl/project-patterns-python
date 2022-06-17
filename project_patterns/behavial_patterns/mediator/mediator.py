class Mediator:

    def __init__(self):
        self._components = set()

    def add(self, component):
        self._components.add(component)

    def notify(self, message, originator):
        for component in self._components:
            if component != originator:
                component.receive(message)
