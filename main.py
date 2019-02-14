import random

from sources import (
    Player,
    Field,
    Ship,
    Shots
)

from handlers import (
    _is_located_correctly,
    _handle_input
)

from generators import generation


def make_players():
    user = Player(input('\nInput username: '))
    print('Let\'s battle, {}!'.format(user.name))

    PC = Player('PC')

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

    PC_ships = pc10_4, pc9_3, pc8_3, pc7_2, pc6_2, pc5_2, pc4_1, pc3_1, pc2_1, pc1_1

    user_ships = u10_4, u9_3, u8_3, u7_2, u6_2, u5_2, u4_1, u3_1, u2_1, u1_1

    return user_ships, PC_ships


def ship_placement(user_ships, PC_ships, user_field, PC_field, user_shots, PC_shots):

    # for ship in user_ships:
    #     def user_placement(ship):
    #         user_field.display_field(user_ships, user_shots)
    #         print('Place a ship of size {} on the field'.format(ship.size))
    #
    #         for size in range(ship.size):
    #             column, row = _handle_input()
    #             ship._columns.append(column)
    #             ship._rows.append(row)
    #         ship.make_location()
    #
    #         #for check ship placement according common sense
    #         if not _is_located_correctly(ship, user_ships, user_field):
    #             print('\nIncorrect location!\n')
    #             ship.location = []
    #             ship._columns = []
    #             ship._rows = []
    #
    #             return user_placement(ship)
    #
    #         #for check ship placement according game rule
    #         user_field._make_ship_field(ship)
    #         print(ship.location)
    #
    #     user_placement(ship)

    for ship in PC_ships:
        def PC_placement(ship):
            position = random.choice(['horizontal', 'vertical'])

            ship._columns, ship._rows = generation(ship, position)
            ship.make_location()

            #for check ship placement according common sense
            if not _is_located_correctly(ship, PC_ships, PC_field):
                ship.location = []
                ship._columns = []
                ship._rows = []

                return PC_placement(ship)

            #for check ship placement according game rule
            PC_field._make_ship_field(ship)

        PC_placement(ship)

    # user_field.display_field(user_ships, user_shots)
    PC_field.display_field(PC_ships, PC_shots)


def make_shots(user, PC):
    user_shots = Shots(user)
    PC_shots = Shots(PC)

    return user_shots, PC_shots


def shoot(shots, field, ships):
    while True:
        print('\nYour turn!\n')
        column, row = _handle_input()
        shots._columns.append(column)
        shots._rows.append(row)
        shots.make_location()
        
        # if not _is_shoot_correct():
        #     del shots._columns[-1]
        #     del shots._rows[-1]
        #     return shoot(shots, field, ships)

        field.display_field(ships, shots)
        print(shots.location)


def main():
    user, PC = make_players()
    user_field, PC_field = make_fields(user, PC)
    user_ships, PC_ships = make_ships()
    user_shots, PC_shots = make_shots(user, PC)
    ship_placement(user_ships, PC_ships, user_field, PC_field, user_shots, PC_shots)
    player = Player.whose_move()

    moving_player = next(player)

    if moving_player == 'user':
        shoot(user_shots, PC_field, PC_ships)
    elif moving_player == 'PC':
        shoot(PC_shots, user_field, user_ships)


if __name__ == '__main__':
    main()
