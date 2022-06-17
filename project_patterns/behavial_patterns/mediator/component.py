class Component:

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def notify(self, message):
        print(self._name + ": >>> Sends >>> : " + message)
        self._mediator.notify(message, self)

    def receive(self, message):
        print(self._name + ": <<< Receives <<< : " + message)
