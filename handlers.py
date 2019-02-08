def _is_located_correctly(ship_location):

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


    return False


    # if _is_same_values(rows):
    #     columns = sorted(columns)
