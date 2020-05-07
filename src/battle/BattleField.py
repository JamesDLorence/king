import numpy as np

from src.battle.Square import Square
from src.battle.Position import Position
from src.character import Character


class BattleField:
    """Representation of physical space a battle will take place"""

    def __init__(self, h=10, w=10):
        self._battle_field = np.empty([h, w], dtype=object).fill(Square())

    def get_square_by_occupant(self, occupant: Character) -> Square:
        # TODO: write functionality
        pass

    def get_square_by_position(self, x: int, y: int) -> Square:
        return self._battle_field[x, y]

    def move_occupant(self, occupant: Character, x: int, y: int):
        current_square = self.get_square_by_occupant(occupant)
        current_square.remove_occupant()

        new_square = self.get_square_by_position(x, y)
        new_square.add_occupant(occupant)
