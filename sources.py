class User:
    def __init__(self, name):
        self.name = name



class Field:
    def __init__(self, owner):
        self.owner = owner.name
        self.field = self.make_field()
        self._ships_field = []

        self._ships_by_columns = []
        self._ships_by_rows = []


    def make_ship_field(self, ship):
        for idx, column in enumerate(ship._columns):
            self._ships_field.append(str(column + 1) + str(ship._rows[idx] + 1))
            self._ships_field.append(str(column - 1) + str(ship._rows[idx] - 1))
            self._ships_field.append(str(column + 1) + str(ship._rows[idx] - 1))
            self._ships_field.append(str(column - 1) + str(ship._rows[idx] + 1))
            self._ships_field.append(str(column) + str(ship._rows[idx] + 1))
            self._ships_field.append(str(column) + str(ship._rows[idx] - 1))


    def display_field(self, ships):

        for ship in ships:
            for place in ship.location:
                    self.field[place] = 'o'

        print('\nField of {}:'.format(self.owner))
        print('''
             A   B   C   D   E   F   G   H   I   J
           +---+---+---+---+---+---+---+---+---+---+
        1  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        2  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        3  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        4  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        5  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        6  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        7  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        8  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        9  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        10 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           +---+---+---+---+---+---+---+---+---+---+
        '''.format(*self.field.values())
        )


    @staticmethod
    def make_field():

        columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        cells = []

        for row in rows:
            for column in columns:
                cells.append(str(column + row))

        field = dict(zip(cells, ' '*len(cells)))

        return field



class Ship(Field):
    def __init__(self, size, name, owner):
        self.size = size
        self.name = name
        self.owner = owner
        self.location = []

        self._columns = []
        self._rows = []
        self._ship_field = []


    def make_location(self):
        for idx, column in enumerate(self._columns):
            self.location.append(str(column) + str(self._rows[idx]))
