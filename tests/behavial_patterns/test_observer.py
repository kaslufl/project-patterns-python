import sys
from io import StringIO

from project_patterns import TaskBoard, GuildMember


def test_new_quest():
    logs = StringIO()
    sys.stdout = logs

    task_board = TaskBoard()

    tank = GuildMember("Lucas", task_board)
    archer = GuildMember("Guilherme", task_board)

    task_board.notify("Kill 2 boars!")

    sys.stdout = sys.__stdout__
    assert logs.getvalue() == ("Adventurer: Guilherme received a new quest: ('Kill 2 boars!',)\n"
                               "Adventurer: Lucas received a new quest: ('Kill 2 boars!',)\n")


def test_unsubscribe():
    logs = StringIO()
    sys.stdout = logs

    task_board = TaskBoard()

    tank = GuildMember("Lucas", task_board)
    archer = GuildMember("Guilherme", task_board)

    task_board.unsubscribe(archer)
    task_board.notify("Kill 2 boars!")

    sys.stdout = sys.__stdout__
    assert logs.getvalue() == "Adventurer: Lucas received a new quest: ('Kill 2 boars!',)\n"
