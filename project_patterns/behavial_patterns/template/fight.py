from .character import Character
from .enemy import Enemy


class Fight:
    def __init__(self, player: Character, enemy: Enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f"{self.player.name} HP: {self.player.hp} MP: {self.player.mp}")
        print("X")
        print(f"{self.enemy.name} HP: {self.enemy.hp} MP: {self.enemy.mp}")
