import sys
from io import StringIO

from project_patterns import EvilBoss, Inspect


def test_inspect():
    logs = StringIO()
    sys.stdout = logs

    boss = EvilBoss()
    boss.accept(Inspect)

    sys.stdout = sys.__stdout__

    assert logs.getvalue() == ('Name: Sword of Destiny ATT: 100 DEF: -1\n'
                               'Name: Black Helmet ATT: 0 DEF: 50\n')
