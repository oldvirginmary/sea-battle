class User:
    def __init__(self, name):
        self.name = name



class Field:
    def __init__(self, owner):
        self.owner = owner.name
        self.field = self.make_field()


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


    def arrange_ship(self):
        for idx, column in enumerate(self._columns):
            self.location.append(str(column) + str(self._rows[idx]))
