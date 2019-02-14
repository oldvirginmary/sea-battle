import itertools


class Player:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def whose_move():
        players = ['user', 'PC']
        for player in itertools.cycle(players):
            yield player



class Field:
    def __init__(self, owner):
        self.owner = owner.name
        self.field = self.make_field()

        self._ships_field = []


    def _make_ship_field(self, ship):
        for idx, column in enumerate(ship._columns):
            self._ships_field.append(str(column + 1) + str(ship._rows[idx] + 1))
            self._ships_field.append(str(column - 1) + str(ship._rows[idx] - 1))
            self._ships_field.append(str(column + 1) + str(ship._rows[idx] - 1))
            self._ships_field.append(str(column - 1) + str(ship._rows[idx] + 1))
            self._ships_field.append(str(column) + str(ship._rows[idx] + 1))
            self._ships_field.append(str(column) + str(ship._rows[idx] - 1))
            self._ships_field.append(str(column + 1) + str(ship._rows[idx]))
            self._ships_field.append(str(column - 1) + str(ship._rows[idx]))


    def display_field(self, ships, shots):

        for ship in ships:
            for place in ship.location:
                    self.field[place] = 'o'

        for shot in shots.location:
            self.field[shot] = 'x'

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
        print('_columns: {}, _rows: {}, location: {}'.format(self._columns, self._rows, self.location))
        for idx, column in enumerate(self._columns):
            self.location.append(str(column) + str(self._rows[idx]))



class Shots(Ship):
    def __init__(self, owner):
        self.location = []
        self.owner = owner.name

        self._columns = []
        self._rows = []
