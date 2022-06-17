from project_patterns import Doubler


def test_iter():
    iterator = iter(Doubler(), 32)
    assert list(iterator) == [2, 4, 8, 16]
