from project_patterns import OrcMageFactory, Player


def test_orc_mage_factory():
    factory = OrcMageFactory()
    player = Player(factory)

    assert 'Orc' == player.get_race()
    assert 'Fireball' == player.attack()
