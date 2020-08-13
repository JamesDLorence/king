from src.battle.Battlefield import Battlefield
from src.util.ActionValues import ActionType
from src.ui import UI

class Battle:
    """Runs battle turns and manages character actions"""

    def __init__(self, battlefield: Battlefield, turn_order: []):
        self._battlefield = battlefield
        self._turn_order = turn_order

    def start(self, mode=None):
        if mode is not None:
            self.render(mode)

        i = 0
        while(self.is_battle_still_going()):
            character = self._turn_order[i]
            action = character.decide_action(self._battlefield, mode=mode)
            result = self.resolve_action(action, character)

            # Update counter to keep looping through characters until battle over
            if i == (len(self._turn_order) - 1):
                i = 0
            else:
                i += 1

            if mode is not None:
                self.render(mode)

    def resolve_action(self, action, character):
        if action.type == ActionType.move.name:
            result = self._battlefield.move_character(character, action.result_pos)
        elif action.type == ActionType.attack.name or action.type == ActionType.magic.name:
            recipient = self._battlefield.get_occupant_by_position(action.result_pos)
            result = recipient.receive_action(action)

            if result is False:
                self._battlefield.get_square_by_occupant(recipient).remove_occupant()
                self._turn_order.remove(recipient)
        # TODO: clean this up
        elif action.type == ActionType.none.name:
            pass
        else:
            raise Exception

        return result

    def is_battle_still_going(self):
        # TODO: Write logic
        return True

    def render(self, mode):
        if mode == 'terminal':
            UI.terminal_display(self._battlefield, [[ch.name, ch.hp] for ch in self._turn_order])






