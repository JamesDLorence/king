from ui import UI
from util.Action import Action
from util.ActionValues import ActionType

from dataclasses import dataclass


@dataclass
class Character:
    """Base interface for all characters"""
    engine_type: str
    name: str
    max_hp: int
    att: int
    df: int
    mag: int
    mag_df: int
    sp: int

    def __post_init__(self):
        self.engine = self.get_engine(self.engine_type)
        self.hp = self.max_hp

    def get_engine(self, engine_type):
        # TODO: Fix this
        return "Engine"

    def decide_action(self, battlefield, mode=None):
        if mode == "terminal":
            act_type, direction, distance = UI.terminal_get_user_action()
        else:
            act_type, direction, distance = self.engine.decide_action(battlefield)

        if act_type == ActionType.attack:
            act_val = self.att
        elif act_type == ActionType.magic:
            act_val = self.mag
        else:
            act_val = None

        pos = battlefield.get_action_position(direction, distance)

        return Action(type=act_type, value=act_val, result_pos=pos)

    def receive_action(self, action):
        # TODO: complete
        pass
