from src.util.Action import Action
from src.util.Position import Position
from src.battle.Square import Square
from src.models.Character import Character


class Battlefield:
    """Representation of physical space a battle will take place"""

    def __init__(self, height, width):
        battlefield = []
        for i in range(height):
            battlefield.append([])
            for j in range(width):
                battlefield[i].append(Square())

        self._battlefield = battlefield

    def get_square_by_occupant(self, occupant: Character) -> Square:
        pos = self.get_position_by_occupant(occupant)
        occupant = self.get_square_by_position(pos)
        return occupant

    def get_occupant_by_pos(self, pos: Position):
        return self._battlefield[pos.y][pos.x].get_occupant()

    def get_square_by_pos(self, pos: Position) -> Square:
        return self._battlefield[pos.y][pos.x]

    def get_position_by_occupant(self, occupant: Character) -> Position:
        for x in range(len(self._battlefield)):
            for y in range(len(self._battlefield[y])):
                if self._battlefield[y][x].get_occupant() == occupant:
                    return Position(y=y, x=x)

        raise Exception

    def move_character(self, character: Character, pos: Position):
        current_square = self.get_square_by_occupant(character)
        current_square.remove_occupant()

        new_square = self.get_square_by_position(pos)
        new_square.add_occupant(character)

    def get_action_position(self, character: Character, direction: str, distance: int) -> Position:
        pos = self.get_position_by_occupant(character)

        if direction == "up":
            new_pos = Position(y=pos.y - distance, x=pos.x)
        elif direction == "down":
            new_pos = Position(y=pos.y + distance, x=pos.x)
        elif direction == "left":
            new_pos = Position(y=pos.y, x=pos.x - distance)
        elif direction == "right":
            new_pos = Position(y=pos.y, x=pos.x + distance)
        else:
            raise Exception

        return new_pos

    def check_if_valid_move_position(self, character: Character, action: Action) -> bool:
        pos = self.get_move_position(character, action.direction)

        if pos.x < 0 or pos.x >= len(self._battlefield[0]):
            return False
        elif pos.y < 0 or pos.y >= len(self._battlefield):
            return False
        else:
            return True

    def get_dimensions(self):
        return len(self._battlefield), len(self._battlefield[0])

    def add_new_character(self, character, pos):
        self.get_square_by_pos(pos).add_occupant(character)
