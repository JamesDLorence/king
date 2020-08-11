import numpy as np

from src.util.Action import Action
from src.util.Position import Position
from src.battle.Square import Square
from src.models.Character import Character


class Battlefield:
    """Representation of physical space a battle will take place"""

    def __init__(self, h=10, w=10):
        self._battlefield = np.empty([h, w], dtype=object).fill(Square())

    def get_square_by_occupant(self, occupant: Character) -> Square:
        pos = self.get_position_by_occupant(occupant)
        occupant = self.get_square_by_position(pos)
        return occupant

    def get_occupant_by_position(self, pos: Position):
        return self._battlefield[pos.x, pos.y].get_occupant()

    def get_square_by_position(self, pos: Position) -> Square:
        return self._battlefield[pos.x, pos.y]

    def get_position_by_occupant(self, occupant: Character) -> Position:
        for x in range(len(self._battlefield)):
            for y in range(len(self._battlefield[y])):
                if self._battlefield[y][x].get_occupant() == occupant:
                    return Position(y, x)

    def move_character(self, character: Character, pos: Position):
        current_square = self.get_square_by_occupant(character)
        current_square.remove_occupant()

        new_square = self.get_square_by_position(pos)
        new_square.add_occupant(character)

    def return_move_position(self, character: Character, direction: str) -> Position:
        pos = self.get_position_by_occupant(character)

        if direction == "up":
            new_pos = Position(y=pos.y - 1, x=pos.x)
        elif direction == "down":
            new_pos = Position(y=pos.y + 1, x=pos.x)
        elif direction == "left":
            new_pos = Position(y=pos.y, x=pos.x - 1)
        elif direction == "right":
            new_pos = Position(y=pos.y, x=pos.x + 1)
        else:
            raise Exception

        return new_pos

    def check_if_valid_move_position(self, character: Character, action: Action) -> bool:
        pos = self.return_move_position(character, action.direction)

        if pos.x < 0 or pos.x >= len(self._battlefield[0]):
            return False
        elif pos.y < 0 or pos.y >= len(self._battlefield):
            return False
        else:
            return True

    def get_dimensions(self):
        return len(self._battlefield), len(self._battlefield[0])
