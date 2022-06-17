import sys
from io import StringIO

from project_patterns import Mediator, Component


def test_interaction():
    logs = StringIO()
    sys.stdout = logs

    mediator = Mediator()
    person1 = Component(mediator, "Lucas")
    person2 = Component(mediator, "Marco")
    mediator.add(person1)
    mediator.add(person2)

    person1.notify("bom dia")
    person2.notify("boa tarde")

    sys.stdout = sys.__stdout__

    assert logs.getvalue() == ('Lucas: >>> Sends >>> : bom dia\n'
                               'Marco: <<< Receives <<< : bom dia\n'
                               'Marco: >>> Sends >>> : boa tarde\n'
                               'Lucas: <<< Receives <<< : boa tarde\n')
