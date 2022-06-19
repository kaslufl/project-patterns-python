import sys
from io import StringIO

from project_patterns import AtmChainDispenser


def test_dispenser():
    logs = StringIO()
    sys.stdout = logs

    atm = AtmChainDispenser()
    atm.chain1.handle(280)

    sys.stdout = sys.__stdout__
    assert logs.getvalue() == ('Dispensing 5 R$50 note(s)\n'
                               'Dispensing 1 R$20 note(s)\n'
                               'Dispensing 1 R$10 note(s)\n')
