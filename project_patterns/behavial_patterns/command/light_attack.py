from .command import Command


class LightAttack(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.light()
