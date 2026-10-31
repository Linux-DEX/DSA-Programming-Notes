from collections import defaultdict


class PubSub:
    """
    In-process topics. publish calls each subscriber inline, in subscribe order.

    Handlers see a snapshot of the subscriber list, so a handler can
    unsubscribe itself without skipping the next handler.
    """

    def __init__(self):
        self._subs = defaultdict(list)

    def subscribe(self, topic, handler):
        self._subs[topic].append(handler)

    def unsubscribe(self, topic, handler):
        self._subs[topic].remove(handler)

    def publish(self, topic, message):
        for handler in list(self._subs.get(topic, ())):
            handler(message)
