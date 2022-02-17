from threading import Lock, Thread


class LoggerMeta(type):
    """Consists in a thread-safe singleton implementation"""

    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=LoggerMeta):
    """Singleton implementation"""
    _logger: str = None

    def __init__(self, value) -> None:
        self._logger = value

    def get_logger(self) -> str:
        return self._logger


def test_logger(value: str) -> None:
    logger = Logger(value)
    print(logger.get_logger())


if __name__ == "__main__":
    process1 = Thread(target=test_logger, args=("Logger",))
    process2 = Thread(target=test_logger, args=("NotLogger",))
    process1.start()
    process2.start()
