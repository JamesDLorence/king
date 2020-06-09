@dataclass
class Character:
    """Base interface for all characters"""
    engine_type: str
    name: str
    max_hp: int
    hp: int = max_hp
    att: int
    df: int
    mg: int
    mg_def: int
    sp: int

    def __post_init__(self):
        self.engine = self.get_engine(self.engine_type)

    def get_engine(self):
        pass

    def decide_action(self, battlefield):
        action = self._engine.decide_action(battlefield)

        return action

    def receive_action(self, action):
        # TODO: complete
        pass
