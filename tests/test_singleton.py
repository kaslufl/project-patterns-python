from threading import Thread
from project_patterns import test_logger as get_log

def test_logger_multi_threads():
    process1 = Thread(target=get_log, args=("Logger",))
    process2 = Thread(target=get_log, args=("NotLogger",))

    assert process1.start() == process2.start()