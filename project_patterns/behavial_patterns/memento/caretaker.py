class Caretaker:

    def __init__(self, npc):
        self._npc = npc
        self._mementos = []

    def create(self):
        memento = self._npc.memento
        self._mementos.append(memento)

    def restore(self, index):
        memento = self._mementos[index]
        self._npc.memento = memento
