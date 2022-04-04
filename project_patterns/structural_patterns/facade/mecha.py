from .engine import Engine
from .weapon import Weapon
from .assisted_aim import AssistedAim


class Mecha:
    """Class to represents a giant biped robot"""

    engine: Engine
    weapon: Weapon
    logs: list[str]


    def __init__(self) -> None:
        self.engine = Engine()
        self.weapon = Weapon()
        self.log = []

    def start(self) -> None:
        self.engine.start_engine()

    def stop(self) -> None:
        self.engine.stop_engine()

    def get_target(self) -> None:
        self.weapon.aim(AssistedAim.get_target())

    def attack(self) -> None:
        self.weapon.shoot()

    def enter_battle_mode(self) -> None:
        self.start()
        self.get_target()
        self.attack()

    def await_rescue(self) -> None:
        self.stop()
