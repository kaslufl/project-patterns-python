class Weapon:
    """Class to represent robot weapons"""

    ammo: int
    pos: tuple[int, int]

    def __init__(self) -> None:
        self.ammo = 20
        self.pos = 0, 0

    def reload(self) -> None:
        if self.ammo > 0:
            print('There is still ammo left')
            return
        self.ammo = 20
        print('Weapon reloaded')


    def shoot(self) -> None:
        if self.ammo < 1:
            print('No ammo available')
            return
        self.ammo -= 1
        print('Weapon fired')

    def aim(self, pos: tuple) -> None:
        self.pos = pos
        print('Target acquired')
