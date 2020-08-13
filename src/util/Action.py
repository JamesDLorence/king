from dataclasses import dataclass

from src.util.Position import Position


@dataclass
class Action:
    # TODO: check about adding enum values to types
    type: str
    value: int
    result_pos: Position
#    facing_direction: str
#    magic_attribute: str
