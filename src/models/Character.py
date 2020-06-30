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

    def decide_action(self, battlefield):
        action = self._engine.decide_action(battlefield)

        return action

    def receive_action(self, action):
        # TODO: complete
        pass
