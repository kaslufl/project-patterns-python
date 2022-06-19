class Weapon:

    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def accept(self, visitor):
        visitor.visit(self)
