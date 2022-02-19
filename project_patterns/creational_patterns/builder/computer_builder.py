from .builder import Builder
from .computer import Computer


class ComputerBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._computer = Computer()

    @property
    def computer(self) -> Computer:
        computer = self._computer
        self.reset()
        return computer

    def add_motherboard(self) -> None:
        self._computer.add("Motherboard")

    def add_cpu(self) -> None:
        self._computer.add("CPU")

    def add_gpu(self) -> None:
        self._computer.add("GPU")

    def add_storage(self) -> None:
        self._computer.add("Storage")

    def add_ram(self) -> None:
        self._computer.add("RAM")

    def add_power(self) -> None:
        self._computer.add("Power")
