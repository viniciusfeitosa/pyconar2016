import gevent
from gevent.event import AsyncResult
a = AsyncResult()


def setter():
    a.set('Hello!')


def waiter():
    print(a.get())


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
