from .fight import Fight


class AmbushFight(Fight):

    def start(self):
        self.enemy.hp = self.enemy.hp * 1.2

        print(f"{self.player.name} HP: {self.player.hp} MP: {self.player.mp}")
        print("X")
        print(f"{self.enemy.name} HP: {self.enemy.hp} MP: {self.enemy.mp}")
