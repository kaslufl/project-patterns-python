from project_patterns import Fight, AmbushFight, Enemy, Character


def test_normal_fight():
    enemy = Enemy("Soldier", 10, 5)
    character = Character("Player", 20, 8)
    fight = Fight(character, enemy)
    fight.start()
    assert enemy.hp == 10


def test_ambush():
    enemy = Enemy("Soldier", 10, 5)
    character = Character("Player", 20, 8)
    fight = AmbushFight(character, enemy)
    fight.start()
    assert enemy.hp == 12
