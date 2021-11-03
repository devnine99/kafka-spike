from app.consumer import MessageConsumer
from app.events import Event, UnKnownEvent


class App:
    def __init__(self):
        self.message_consumer = MessageConsumer()

    def run(self):
        self.main_loop()

    def main_loop(self):
        for message in self.message_consumer.receive():
            event_class = self.get_event_class(message)
            event_class.consume()

    @staticmethod
    def get_event_class(message):
        for event_class in Event.__subclasses__():
            if event_class.check_key(message.key):
                return event_class(message)
        return UnKnownEvent(message)
