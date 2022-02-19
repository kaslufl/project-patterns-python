from project_patterns import ComputerBuilder, Director


def test_computer_builder():
    director = Director()
    builder = ComputerBuilder()
    director.builder = builder
    director.build_full_pc()
    assert builder.computer.parts == [
        "Motherboard",
        "CPU",
        "GPU",
        "Storage",
        "RAM",
        "Power",
    ]
