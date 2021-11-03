import abc


class Event(abc.ABC):
    key = None

    def __init__(self, message):
        self.message = message

    @classmethod
    def check_key(cls, key):
        return key == cls.key

    @abc.abstractmethod
    def consume(self):
        pass


class UnKnownEvent(Event):
    def consume(self):
        print('UnKnownEvent!!')


class TestEvent(Event):
    key = 'test'

    def consume(self):
        print(self.message.key, self.message.value)


class Test2Event(Event):
    key = 'test2'

    def consume(self):
        print(self.message.key, self.message.value)
