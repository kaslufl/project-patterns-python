from project_patterns import HighAttack, LowAttack, Hero


def test_high_attack():
    hero = Hero

    assert hero.attack(HighAttack) == 'High Attack ⬆'


def test_low_attack():
    hero = Hero

    assert hero.attack(LowAttack) == 'Low Attack ⬇'
