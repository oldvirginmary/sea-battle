from sources import (
    User,
)


def make_players():
    user = User(input('Input username: '))
    print('Hi {}, let\'s go!'.format(user.name))

    PC = User('computer')

    return user, PC


def ship_placement(user, PC):
    while True:
        user.display_field()
        user.arrange_ships(input('Arrange your ships on the field: '))



def main():
    user, PC = make_players()

    ship_placement(user, PC)



if __name__ == '__main__':
    main()
