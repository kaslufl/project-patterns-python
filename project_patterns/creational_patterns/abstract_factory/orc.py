from .race import Race


class Orc(Race):
    "Class to represent a big green guy"

    def get_name(self) -> str:
        return self.__class__.__name__
