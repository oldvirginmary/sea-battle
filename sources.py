import itertools, random
from handlers import _handle_input
from generators import gen_placement


class Player:
    def __init__(self, name):
        self.name = name
        self.field = []
        self.shots = []
        self.ships = []
        self._ships_field = []

    @staticmethod
    def whose_move():
        players = ['user', 'PC']
        for player in itertools.cycle(players):
            yield player


class Field:
    def __init__(self, owner):
        self.owner = owner.name
        self.field = self.make_field()

    def display_field(self, player):
        for ship in player.ships:
            for place in ship.location:
                    self.field[place] = 'o'
        # for shot in shots.location:
        #     self.field[shot] = 'x'
        # for field in self._ships_field:
        #     self.field[field] = 'f'

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
    def __init__(self, name, size, player):
        self.name = name
        self.size = size
        self.owner = player.name
        self.location = []

        self.columns = []
        self.rows = []

    @staticmethod
    def create_ships(player):
        # Genereate 10 ships as class objects
        sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for idx, size in enumerate(sizes):
            ship_name = '{}_{}'.format(player.name, idx)
            exec('{} = Ship(ship_name, {}, player)'.format(ship_name, size))
            exec('player.ships.append({})'.format(ship_name))

    @staticmethod
    def arrange_ships(player):
        # Arrange ships by columns and rows, and then check their location

        for ship in player.ships:

            def arrange_ship(ship):

                if player.name != 'pc':
                    player.field.display_field(player)
                    print('Place a ship of size {} on the field'.format(ship.size))

                    for size in range(ship.size):
                        column, row = _handle_input()
                        ship.columns.append(column)
                        ship.rows.append(row)
                    ship.make_location()

                else:
                    position = random.choice(['horizontal', 'vertical'])
                    ship.columns, ship.rows = gen_placement(ship, position)
                    ship.make_location()

                # for check ship placement according common sense
                if not ship._is_located_correctly(player):
                    ship.location = []
                    ship.columns = []
                    ship.rows = []
                    if player.name != 'pc':
                        print('\nIncorrect location!\n')

                    arrange_ship(ship)

                # make 1 block field around ship
                ship._make_ship_field(player)

            arrange_ship(ship)

        player.field.display_field(player)

    def make_location(self):
        for idx, column in enumerate(self.columns):
            self.location.append(str(column) + str(self.rows[idx]))

    def _make_ship_field(self, player):
        # Make field in 1 block around ship
        for idx, column in enumerate(self.columns):
            """TODO: FIX BUG OF INCORRECT SHIPS FIELD"""
            player._ships_field.append(str(column + 1) + str(self.rows[idx] + 1))
            player._ships_field.append(str(column - 1) + str(self.rows[idx] - 1))
            player._ships_field.append(str(column + 1) + str(self.rows[idx] - 1))
            player._ships_field.append(str(column - 1) + str(self.rows[idx] + 1))
            player._ships_field.append(str(column) + str(self.rows[idx] + 1))
            player._ships_field.append(str(column) + str(self.rows[idx] - 1))
            player._ships_field.append(str(column + 1) + str(self.rows[idx]))
            player._ships_field.append(str(column - 1) + str(self.rows[idx]))

    def _is_located_correctly(self, player):

        def _is_same_values(some_list):
            first = some_list[0]
            for i in some_list:
                if i != first:
                    return False
            return True

        if _is_same_values(self.columns):
            self.rows = [int(i) for i in sorted(self.rows)]

            if len(self.rows) != len(set(self.rows)):
                print('duplicate values')
                return False

            for idx, n in enumerate(self.rows):
                if n == self.rows[-1] or self.rows[idx + 1] - n == 1:
                    pass
                else:
                    print('inconsistent ship blocks')
                    return False

        elif _is_same_values(self.rows):
            self.columns = [int(i) for i in sorted(self.columns)]

            if len(self.columns) != len(set(self.columns)):
                print('duplicate values')
                return False

            for idx, n in enumerate(self.columns):
                if n == self.columns[-1] or self.columns[idx + 1] - n == 1:
                    pass
                else:
                    print('inconsistent ship blocks')
                    return False

        else:
            print('neither row nor column is consistent')
            return False

        for square in self.location:
            if square in player._ships_field:
                print('can not be in field another ship')
                return False

        for another_ship in player.ships:
            if self.location == another_ship.location and self.name != another_ship.name:
                print('can not be in another ship')
                return False

        return True


class Shot(Ship):
    def __init__(self, player):
        self.location = []
        self.owner = player.name

        self.columns = []
        self.rows = []

    @staticmethod
    def create_shots(player):
        # Generate 100 shots as class objects
        for idx in range(1, 101):
            shot_name = '{}_s_{}'.format(player.name, idx)
            exec('{} = Shot(player)'.format(shot_name))
            exec('player.shots.append({})'.format(shot_name))
