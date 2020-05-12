class UI:
    """Prints UI for user"""
    char_symbols ={}

    def __init__(self, battlefield):
        self._b= battlefield

    def render(self):
        w = len(self._b[0])

        self.print_line(w)
        for row in self._b:
            for square in row:
                self.print_square()

            print('|')
            self.print_line(w)

    def print_line(self, w):
        print((w * 5 + 1) * '-')

    def print_square(self, occupant=None):
        if occupant is None:
            output = '|    '
        else:
            output = '| ' + self.get_char_symbol(occupant) + '  '

        print(output, end='')

    def get_char_symbol