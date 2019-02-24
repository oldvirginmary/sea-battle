def _handle_input():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    location = input('Input location: ').lower()

    try:
        letter = location[0]
        num = location[1:]
        column = nums[letters.index(letter)]
        row = int(num)
    except ValueError:
        print('Incorrect location! True input: f2, b7, etc.')
        return _handle_input()
    except IndexError:
        print('Incorrect input!')
        return _handle_input()

    if row not in range(11):
        print('Incorrect location! Try 1 — 10')
        return _handle_input()

    return column, row
