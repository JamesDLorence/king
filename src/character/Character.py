class Character:
    """Base interface for all characters"""

    def __init__(self, engine):
        self._engine = engine

    def decide_action(self, battlefield):
        action = self._engine.decide_action(battlefield)

        return action

    def receive_action(self, action):
        # TODO: complete
        pass
