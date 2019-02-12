def _is_located_correctly(ship, field):

    def _is_same_values(some_list):
        first = some_list[0]
        for i in some_list:
            if i != first:
                return False
        return True


    if _is_same_values(ship._columns):
        ship._rows = [int(i) for i in sorted(ship._rows)]

        if len(ship._rows) != len(set(ship._rows)):
            return False

        for idx, n in enumerate(ship._rows):
            if n == ship._rows[-1] or ship._rows[idx+1] - n == 1:
                pass
            else:
                return False

    elif _is_same_values(ship._rows):
        ship._columns = [int(i) for i in sorted(ship._columns)]

        if len(ship._columns) != len(set(ship._columns)):
            return False

        for idx, n in enumerate(ship._columns):
            if n == ship._columns[-1] or ship._columns[idx+1] - n == 1:
                pass
            else:
                return False

    else:
        return False

    for square in ship.location:
        if square in field._ships_field:
            return False

    return True


def _input_columns():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    try:
        letter = input('Column: ').lower()
        return nums[letters.index(letter)]
    except ValueError:
        print('\nIncorrect column! Expected: A - J\n')
        return _input_columns()


def _input_rows():
    try:
        num = int(input('Row: '))
    except ValueError:
        print('\nInsert the number 0 - 10\n')
        return _input_rows()

    if num not in range(11):
        print('\nThere is no this row! Expected: 0 - 10\n')
        return _input_rows()

    return num
