class Invoker:

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            return self._commands[command_name].execute()
        else:
            return f"Command [{command_name}] not recognised"
