from project_patterns import Npc, Caretaker, Memento


def test_create():
    npc = Npc()
    caretaker = Caretaker(npc)
    npc.state = 'alive'
    caretaker.create()
    npc.state = 'dead'
    caretaker.restore(0)

    assert npc.state == 'alive'


def test_restore():
    npc = Npc()
    caretaker = Caretaker(npc)
    npc.state = 'alive'
    caretaker.create()
    npc.state = 'dead'
    caretaker.create()
    npc.state = 'resurrected'
    caretaker.restore(1)

    assert npc.state == 'dead'
