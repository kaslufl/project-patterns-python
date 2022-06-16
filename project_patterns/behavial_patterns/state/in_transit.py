from .package_state import PackageState


class InTransit(PackageState):
    name = "in_transit"
    allowed = ['delivered']
