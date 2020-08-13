from ui import UI
from util.Action import Action
from util.ActionValues import ActionType

from dataclasses import dataclass
import math


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
            act_type, direction, distance = UI.terminal_get_user_action(self.name)
        else:
            act_type, direction, distance = self.engine.decide_action(battlefield)

        if act_type == ActionType.attack.name:
            act_val = self.att
        elif act_type == ActionType.magic.name:
            act_val = self.mag
        else:
            act_val = None

        pos = battlefield.get_action_position(self, direction, distance)

        return Action(type=act_type, value=act_val, result_pos=pos)

    def receive_action(self, action):
        if action.type == ActionType.attack.name:
            self.hp -= math.ceil(action.value - (self.df / 2))
        elif action.type == ActionType.magic.name:
            self.hp -= action.value - self.mag_df

        if self.hp <= 0:
            self.hp = 0

        return self.hp != 0




