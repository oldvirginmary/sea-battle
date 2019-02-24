import random


def gen_placement(ship, position):

    if position == 'horizontal':
        columns = [random.choice(range(1, 11)) for i in range(ship.size)]
        rows = [random.choice(range(1, 11))] * ship.size

    else:  # position == 'vertical'
        columns = [random.choice(range(1, 11))] * ship.size
        rows = [random.choice(range(1, 11)) for i in range(ship.size)]

    return columns, rows
