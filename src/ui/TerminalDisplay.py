from src.util.Position import Position

def render(battlefield):
    h, w = battlefield.get_dimensions()

    print_line(w)
    for y in range(h):
        for x in range(w):
            occupant = battlefield.get_occupant_by_pos(Position(y=y, x=x))
            print_square(occupant)

        # end row with closing pipe
        print('|')
        print_line(w)

def print_line(w):
    print((w * 5 + 1) * '-')

def print_square(occupant):
    if occupant is None:
        output = '|    '
    else:
        output = '| ' + occupant.name + ' '

    print(output, end='')