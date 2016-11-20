import gevent


def jedi_msg():
    return 'May the force be with you'


def sith_msg():
    raise Exception('Luke, I\'m your father')


jedi = gevent.spawn(jedi_msg)
sith = gevent.spawn(sith_msg)

print(jedi.started)
print(sith.started)

try:
    gevent.joinall([jedi, sith])
except Exception as e:
    print('This will never be reached')

print(jedi.value)  # 'May the force be with you'
print(sith.value)  # None

print(jedi.ready())  # True
print(sith.ready())  # True

print(jedi.successful())  # True
print(sith.successful())  # False

print(sith.exception)
