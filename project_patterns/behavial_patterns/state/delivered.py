from .package_state import PackageState


class Delivered(PackageState):
    name = "delivered"
    allowed = []
