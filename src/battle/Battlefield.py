import numpy as np

from src.util.Position import Position
from src.battle.Square import Square
from src.character.Character import Character


class Battlefield:
    """Representation of physical space a battle will take place"""

    def __init__(self, h=10, w=10):
        self._battle_field = np.empty([h, w], dtype=object).fill(Square())

    def get_square_by_occupant(self, occupant: Character) -> Square:
        # TODO: write functionality
        pass

    def get_occupant_by_position(self, pos: Position):
        return self._battle_field[pos.x, pos.y].get_occupant()

    def get_square_by_position(self, pos: Position) -> Square:
        return self._battle_field[pos.x, pos.y]

    def move_occupant(self, occupant: Character, pos: Position):
        current_square = self.get_square_by_occupant(occupant)
        current_square.remove_occupant()

        new_square = self.get_square_by_position(pos)
        new_square.add_occupant(occupant)
