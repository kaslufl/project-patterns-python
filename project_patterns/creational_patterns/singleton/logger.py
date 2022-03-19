from .logger_meta import LoggerMeta


class Logger(metaclass=LoggerMeta):
    """Singleton implementation."""

    _logger: str = None

    def __init__(self, value) -> None:
        self._logger = value

    def get_logger(self) -> str:
        return self._logger


def test_logger(value: str) -> None:
    logger = Logger(value)
    return logger.get_logger()
