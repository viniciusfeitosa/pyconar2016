import gevent


def jedi_msg():
    return 'May the force be with you'


def sith_msg():
    raise Exception('Luke, I\'m your father')


jedi = gevent.spawn(jedi_msg)
sith = gevent.spawn(sith_msg)

print("¿Jedi Started?", jedi.started)
print("¿Sith Started?", sith.started)

try:
    gevent.joinall([jedi, sith])
except Exception as e:
    print('This will never be reached')

print("Jedi value:", jedi.value)  # 'May the force be with you'
print("Sith value:", sith.value)  # None

print("Jedi ready:", jedi.ready())  # True
print("Sith ready:", sith.ready())  # True

print("¿Jedi Successful?", jedi.successful())  # True
print("¿Sith Successful?", sith.successful())  # False

print("Sith exception:", sith.exception)
