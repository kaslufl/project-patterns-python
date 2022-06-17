from project_patterns import Mecha
from io import StringIO
import sys


def test_combate_mode():
    logs = StringIO()
    sys.stdout = logs

    mecha = Mecha()
    mecha.enter_battle_mode()

    sys.stdout = sys.__stdout__

    assert ( logs.getvalue() == 'Engine started\nTarget acquired\nWeapon fired\n')