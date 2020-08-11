from src.util.Position import Position

def render(self, battlefield):
    h, w = battlefield.get_dimensions()

    self.print_line(w)
    for y in range(h):
        for x in range(w):
            occupant = battlefield.get_occupant_by_position(Position(y, x))
            print_square(occupant)

        # end row with closing pipe
        print('|')
        self.print_line(w)

def print_line(self, w):
    print((w * 5 + 1) * '-')

def print_square(self, occupant):
    if occupant is None:
        output = '|    '
    else:
        output = '| ' + occupant.name + ' '

    print(output, end='')