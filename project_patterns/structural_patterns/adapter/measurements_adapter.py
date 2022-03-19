from .furniture import Furniture


class MeasurementsAdapter:
    "Class to adapt the measurements of a furniture"

    def __init__(self, furniture: Furniture) -> None:
        self.furniture = furniture

    def measurements_to_inches(self) -> dict:
        height = self.furniture.get_height() / 2.54
        width = self.furniture.get_width() / 2.54
        return {"height": f'{height:.2f} in', "width": f'{width:.2f} in'}
