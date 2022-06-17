class Doubler:
    count = 1

    @classmethod
    def next(cls):
        cls.count *= 2
        return cls.count

    __call__ = next
