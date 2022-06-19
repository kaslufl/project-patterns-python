class GuildMember:
    def __init__(self, name, observable):
        self._name = name
        observable.subscribe(self)

    def notify(self, *args):
        print(f'Adventurer: {self._name} received a new quest: {args}')
