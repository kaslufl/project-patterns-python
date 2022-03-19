from project_patterns import Affinity, Item


def test_item_affinities():
    fire_affinity = Affinity('Fire', 1, 3)
    normal_affinity = Affinity('Normal', 2, 0)

    sword = Item('Sword of Kor', 15, 15, normal_affinity)
    enchanted_sword = Item('Micolas Rapier', 15, 15, fire_affinity)

    assert sword.get_info() == 'Sword of Kor | att: 30 mag: 0 aff: Normal'
    assert enchanted_sword.get_info() == 'Micolas Rapier | att: 15 mag: 45 aff: Fire'