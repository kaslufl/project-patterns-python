from .package_state import PackageState


class Separation(PackageState):
    name = "separation"
    allowed = ['in_transit']
