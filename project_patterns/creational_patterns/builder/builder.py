from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def computer(self) -> None:
        pass

    @abstractmethod
    def add_motherboard(self) -> None:
        pass

    @abstractmethod
    def add_cpu(self) -> None:
        pass

    @abstractmethod
    def add_gpu(self) -> None:
        pass

    @abstractmethod
    def add_storage(self) -> None:
        pass

    @abstractmethod
    def add_ram(self) -> None:
        pass

    @abstractmethod
    def add_power(self) -> None:
        pass
