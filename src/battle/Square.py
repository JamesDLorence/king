class Square:
    """Representation of one unit on BattleField"""

    def __init__(self):
        self._occupant = None

    def remove_occupant(self):
        self._occupant = None

    def add_occupant(self, occupant):
        if self._occupant is not None:
            self._occupant = occupant
        else:
            raise Exception

    def get_occupant(self):
        return self._occupant