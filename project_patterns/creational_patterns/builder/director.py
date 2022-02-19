from .builder import Builder


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_full_pc(self) -> None:
        self._builder.add_motherboard()
        self._builder.add_cpu()
        self._builder.add_gpu()
        self._builder.add_storage()
        self._builder.add_ram()
        self._builder.add_power()
