from src.battle.Battlefield import Battlefield
from src.util.ActionType import ActionType
from src.ui import UI

class Battle:
    """Runs battle turns and manages character actions"""

    def __init__(self, battlefield: Battlefield, turn_order: []):
        self._battlefield = battlefield
        self._turn_order = turn_order

    def start(self, mode=None):
        if mode is not None:
            self.render(mode)

        # TODO: Rewrite how turn order works
        i = 0
        while(self.is_battle_still_going()):
            character = self._turn_order[i]
            action = character.decide_action(self._battlefield)

            self.resolve_action(action, character)

            if mode is not None:
                self.render(mode)

            # Update counter to keep looping through characters until battle over
            if i == (len(self._turn_order) - 1):
                i = 0
            else:
                i += 1

    def resolve_action(self, action, character):
        if (action.type == ActionType.MOVE):
            result = self._battlefield.move_character(character, action.result_pos)
        elif (action.type in ActionType.__members__):
            recipient = self._battlefield.get_occupant_by_position(action.result_pos)
            result = recipient.receive_attack(action)
        else:
            raise Exception

    def is_battle_still_going(self):
        # TODO: Write logic
        return True

    def render(self, mode):
        if mode == 'terminal':
            UI.terminal_display(self._battlefield)






