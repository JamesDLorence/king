from dataclasses import dataclass

@dataclass
class Position:
    """Location of Square on Battlefield"""
    x: int
    y: int