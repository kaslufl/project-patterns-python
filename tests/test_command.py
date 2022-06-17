from project_patterns import LightAttack, FireAttack, Receiver, Invoker


def test_light_attack():
    receiver = Receiver()
    light_attack = LightAttack(receiver)
    invoker = Invoker()
    invoker.register("light", light_attack)
    assert invoker.execute("light") == '⚡'


def test_fire_attack():
    receiver = Receiver()
    fire_attack = FireAttack(receiver)
    invoker = Invoker()
    invoker.register("fire", fire_attack)
    assert invoker.execute("fire") == '🔥'


def test_non_valid_attack():
    invoker = Invoker()

    assert invoker.execute("water") == 'Command [water] not recognised'
