from .dispenser import Dispenser


class Dispenser50(Dispenser):

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f'Dispensing {num} R$50 note(s)')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
