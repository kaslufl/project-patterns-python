from project_patterns import Package, InTransit, Delivered, Separation


def test_separation_to_delivered():
    package = Package()

    assert package.change(Delivered) == 'Current: separation not possible to switch to delivered'


def test_separation_to_in_transit():
    package = Package()

    assert package.change(InTransit) == 'Current: separation switching to in_transit'
