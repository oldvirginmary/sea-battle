def _is_located_correctly(ship_location, user_field):

    def _is_same_values(some_list):
        first = some_list[0]

        for i in some_list:
            if i != first:
                return False

        return True


    columns = []
    rows = []

    for cell in ship_location:
        columns.append(cell[0])
        rows.append(cell[1])


    if _is_same_values(columns):
        rows = [int(i) for i in sorted(rows)]

        for idx, n in enumerate(rows):
            if n == rows[-1] or rows[idx+1] - n == 1:
                pass
            else:
                return False

        return True


    elif _is_same_values(rows):
        ship_location = sorted(ship_location)
        user_field = list(user_field.field.keys())

        for idx, cell in enumerate(ship_location):
            if cell == ship_location[-1] or user_field.index(ship_location[idx+1]) - user_field.index(cell) == 1:
                pass
            else:
                return False

        return True


    else:
        return False




    # if _is_same_values(rows):
    #     columns = sorted(columns)
    #
    #     for n in columns:
    #         if n user_field or n[idx+1] - idx:
    #             pass
    #         else:
    #             return False
    #
    #     return True
