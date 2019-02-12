import random

from sources import (
    User,
    Field,
    Ship
)

from handlers import (
    _is_located_correctly,
    _input_columns,
    _input_rows
)

from generators import generation


def make_players():
    user = User(input('\nInput username: '))
    print('Let\'s battle, {}!'.format(user.name))

    PC = User('PC')

    return user, PC


def make_fields(user, PC):
    user_field = Field(user)
    PC_field = Field(PC)

    return user_field, PC_field


def make_ships():
    # Ships have their ID numbers

    # u1_1 = Ship(1, 'u1_1', 'user')
    # u2_1 = Ship(1, 'u2_1', 'user')
    # u3_1 = Ship(1, 'u3_1', 'user')
    # u4_1 = Ship(1, 'u4_1', 'user')
    # u5_2 = Ship(2, 'u5_2', 'user')
    # u6_2 = Ship(2, 'u6_2', 'user')
    # u7_2 = Ship(2, 'u7_2', 'user')
    # u8_3 = Ship(3, 'u8_3', 'user')
    # u9_3 = Ship(3, 'u9_3', 'user')
    # u10_4 = Ship(4, 'u10_4', 'user')

    pc1_1 = Ship(1, 'pc1_1', 'PC')
    pc2_1 = Ship(1, 'pc2_1', 'PC')
    pc3_1 = Ship(1, 'pc3_1', 'PC')
    pc4_1 = Ship(1, 'pc4_1', 'PC')
    pc5_2 = Ship(2, 'pc5_2', 'PC')
    pc6_2 = Ship(2, 'pc6_2', 'PC')
    pc7_2 = Ship(2, 'pc7_2', 'PC')
    pc8_3 = Ship(3, 'pc8_3', 'PC')
    pc9_3 = Ship(3, 'pc9_3', 'PC')
    pc10_4 = Ship(4, 'pc10_4', 'PC')

    # return u10_4, u9_3, u8_3, u7_2, u6_2, u5_2, u4_1, u3_1, u2_1, u1_1
    return pc10_4, pc9_3, pc8_3, pc7_2, pc6_2, pc5_2, pc4_1, pc3_1, pc2_1, pc1_1
    # return pc5_2, pc1_1


def ship_placement(ships, user_field, PC_field):

    for ship in ships:
        if ship.owner == 'user':

            def user_placement(ship):
                user_field.display_field(ships)
                print('Place a ship of size {} on the field'.format(ship.size))

                for size in range(ship.size):
                    ship._columns.append(_input_columns()) #1, 2, ..., 10
                    ship._rows.append(_input_rows()) #1, 2, ..., 10
                    ship.make_location()

                if not _is_located_correctly(ship, user_field):
                    print('\nIncorrect location!\n')
                    ship.location = []
                    ship._columns = []
                    ship._rows = []

                    return user_placement(ship)

                user_field.make_ship_field(ship)

            user_placement(ship)


        elif ship.owner == 'PC':

            def PC_placement(ship):
                position = random.choice(['horizontal', 'vertical'])

                ship._columns, ship._rows = generation(ship, position)
                ship.make_location()

                if not _is_located_correctly(ship, PC_field):
                    ship.location = []
                    ship._columns = []
                    ship._rows = []

                    return PC_placement(ship)

                print('\nLOCATION is CORRECT!!!\n')
                PC_field.make_ship_field(ship)

            PC_placement(ship)



    user_field.display_field(ships)
    PC_field.display_field(ships)


def main():
    user, PC = make_players()
    user_field, PC_field = make_fields(user, PC)
    ships = make_ships()
    ship_placement(ships, user_field, PC_field)



if __name__ == '__main__':
    main()
