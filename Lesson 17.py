__author__ = 'Scott'

def add_numbers(*args):
    total = 0
    for y in args:
        total += y
    print(total)

add_numbers(10)
add_numbers(500, 50, 5)
add_numbers(845, 621, 71)