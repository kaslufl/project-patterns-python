from .memento import Memento


class Npc:

    def __init__(self):
        self._state = ""

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def memento(self):
        return Memento(self._state)

    @memento.setter
    def memento(self, memento):
        self._state = memento.state
