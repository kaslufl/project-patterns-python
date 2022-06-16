from .separation import Separation


class Package:
    def __init__(self):
        self.state = Separation()

    def change(self, state):
        return self.state.switch(state)
