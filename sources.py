class User:
    def __init__(self, name):
        self.name = name



class Field:
    def __init__(self, owner):
        self.owner = owner.name
        self.field = self.make_field()


    def arrange_ship(self, ship_location):
        for cell in ship_location:
            self.field[cell] = 'o'


    def display_field(self):
        print('Field of {}:'.format(self.owner))
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

        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
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
        self.location = None
