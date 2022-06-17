from project_patterns import Table, MeasurementsAdapter


def test_measurements_adapter():
    table = Table(100, 50)
    table_measurements_inch = MeasurementsAdapter(table).measurements_to_inches()
    assert table_measurements_inch == {'height': '39.37 in', 'width': '19.69 in'}
