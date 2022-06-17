from project_patterns import Sword, Gem


def test_sword():
    sword = Sword('Forgotten Sword', 16, 36)

    assert sword.get_info() == 'Name: Forgotten Sword Att: 16 Val: 36'

def test_gemmed_sword():
    sword = Sword('Sword of Memory', 32, 50)
    gemmed_sword = Gem(sword)

    assert gemmed_sword.get_info() == 'Name: Sword of Memory Att: 64 Val: 70'
