from .attack import Attack


class Hero:

    @staticmethod
    def attack(strategy: Attack):
        return strategy.attack()
