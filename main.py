import random
from sources import (
    Player,
    Field,
    Ship,
    Shot
)


def create_resources(user, pc):
    user.field = Field(user)
    pc.field = Field(pc)

    Ship.create_ships(user)
    Ship.create_ships(pc)

    Shot.create_shots(user)
    Shot.create_shots(pc)


def ship_placement(user, pc):
    Ship.arrange_ships(user)
    Ship.arrange_ships(pc)


def shoot(storage):
    while True:
        print('\nYour turn!\n')
        storage.shots
        column, row = _handle_input()
        shot.columns.append(column)
        shot.rows.append(row)
        shot.make_location()

        field.display_field(ships, shots)
        print(shots.location)


def main():
    user = Player(input('\nInput username: '))
    pc = Player('pc')

    create_resources(user, pc)
    ship_placement(user, pc)

    # player = Player.whose_move()
    #
    # moving_player = next(player)
    #
    # if moving_player == 'user':
    #     shoot(user_shots, pc_field, pc_ships)
    #     field.display_field(storage)
    # elif moving_player == 'pc':
    #     shoot(pc_shots, user_field, user_ships)


if __name__ == '__main__':
    main()
