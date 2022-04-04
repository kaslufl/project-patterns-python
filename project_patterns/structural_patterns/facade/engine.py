class Engine:
    """Class to represent an engine of a giant bot"""

    on: bool

    def __init__(self) -> None:
        self.on = False

    def start_engine(self) -> str:
        if self.on:
            print('Already started')
            return
        self.on = True
        print('Engine started')

    def stop_engine(self) -> str:
        if not self.on:
            print('Already stopped')
            return
        self.on = False
        print('Engine stopped')
