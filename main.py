import random
from handlers import _handle_input
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


def start(user, pc):
    player = Player.whose_move(user, pc)

    while True:
        moving_player = next(player)
        if moving_player == user:
            Shot.shoot(user, pc)


def main():
    user = Player(input('\nInput username: '))
    pc = Player('pc')

    create_resources(user, pc)
    ship_placement(user, pc)

    start(user, pc)


if __name__ == '__main__':
    main()
