import random

def generation(ship, position):

    if position == 'horizontal':
        columns = [random.choice(range(1, 11)) for i in range(ship.size)]
        rows = [random.choice(range(1, 11))] * ship.size

    elif position == 'vertical':
        columns = [random.choice(range(1, 11))] * ship.size
        rows = [random.choice(range(1, 11)) for i in range(ship.size)]

    print(columns, rows)
    return columns, rows
