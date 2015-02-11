__author__ = 'Scott'


# This shows how a function can have many args and only one or two can be modified and modified in any order

def sent(name='Scott', action="went to", thing='class'):
    print(name, action, thing)
sent()
sent(action='slept in')
sent(thing='home', name='Matt')