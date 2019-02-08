import random

from sources import (
    User,
    Field,
    Ship
)

from handlers import (
    _is_located_correctly,
)


def make_players():
    user = User(input('Input username: '))
    print('Let\'s battle, {}!'.format(user.name))

    PC = User('PC')

    return user, PC


def make_fields(user, PC):
    user_field = Field(user)
    PC_field = Field(PC)

    return user_field, PC_field


def make_ships():
    # Ships have their ID numbers
    u1_1 = Ship(1, 'u1_1', 'user')
    u2_1 = Ship(1, 'u2_1', 'user')
    u3_1 = Ship(1, 'u3_1', 'user')
    u4_1 = Ship(1, 'u4_1', 'user')
    u5_2 = Ship(2, 'u5_2', 'user')
    u6_2 = Ship(2, 'u6_2', 'user')
    u7_2 = Ship(2, 'u7_2', 'user')
    u8_3 = Ship(3, 'u8_3', 'user')
    u9_3 = Ship(3, 'u9_3', 'user')
    u10_4 = Ship(4, 'u10_4', 'user')

    # pc1_1 = Ship(1, 'pc1_1', 'PC')
    # pc2_1 = Ship(1, 'pc2_1', 'PC')
    # pc3_1 = Ship(1, 'pc3_1', 'PC')
    # pc4_1 = Ship(1, 'pc4_1', 'PC')
    # pc5_2 = Ship(2, 'pc5_2', 'PC')
    # pc6_2 = Ship(2, 'pc6_2', 'PC')
    # pc7_2 = Ship(2, 'pc7_2', 'PC')
    # pc8_3 = Ship(3, 'pc8_3', 'PC')
    # pc9_3 = Ship(3, 'pc9_3', 'PC')
    # pc10_4 = Ship(4, 'pc10_4', 'PC')

    return u10_4, u9_3, u8_3, u7_2, u6_2, u5_2, u4_1, u3_1, u2_1, u1_1


def ship_placement(ships, user_field, PC_field):

    for ship in ships:
        ship_location = []


        if ship.owner == 'user':

            def place(ship, ship_location):

                user_field.display_field()

                for cells in range(ship.size):
                    cell = input('Place a ship of size {} on the field: '.format(ship.size))
                    ship_location.append(cell)

                if not _is_located_correctly(ship_location):
                    print('\nIncorrect location!\n')

                    return place(ship, ship_location)

            place(ship, ship_location)

            user_field.arrange_ship(ship_location)
            ship.location = ship_location


        elif ship.owner == 'PC':
            ship_location = random.choice(list(PC_field.field.keys()))

            PC_field.arrange_ship(ship_location)

            ship.location = ship_location

    user_field.display_field()
    PC_field.display_field()


def main():
    user, PC = make_players()
    user_field, PC_field = make_fields(user, PC)
    ships = make_ships()
    ship_placement(ships, user_field, PC_field)



if __name__ == '__main__':
    main()
