import random

class AssistedAim:
    """Class to represents an auto aim for the weapons"""

    @classmethod
    def get_target(cls) -> tuple:
        return random.randint(1,100), random.randint(1,100)
