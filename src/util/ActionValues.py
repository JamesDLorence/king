from enum import Enum


class ActionType(Enum):
    move = "move"
    attack = "attack"
    magic = "magic"
    none = "none"


class Direction(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


class Distance(Enum):
    one = 1
    two = 2
    three = 3
