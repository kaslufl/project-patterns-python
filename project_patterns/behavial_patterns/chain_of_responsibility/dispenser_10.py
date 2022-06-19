from .dispenser import Dispenser


class Dispenser10(Dispenser):

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f'Dispensing {num} R$10 note(s)')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
