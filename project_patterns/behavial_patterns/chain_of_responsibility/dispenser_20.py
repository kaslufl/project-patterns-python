from .dispenser import Dispenser


class Dispenser20(Dispenser):

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f'Dispensing {num} R$20 note(s)')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
