import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' % (n, task))
        gevent.sleep(0)

    print('%s salindo de la cola!' % (n))


def boss():
    for i in range(1, 25):
        tasks.put_nowait(i)


gevent.spawn(boss).join()

gevent.joinall([
    gevent.spawn(worker, 'Luke'),
    gevent.spawn(worker, 'Ham'),
    gevent.spawn(worker, 'Lea'),
])
