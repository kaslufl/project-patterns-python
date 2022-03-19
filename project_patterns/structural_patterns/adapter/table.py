from .furniture import Furniture


class Table(Furniture):
    "Class to represent tables"

    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height
