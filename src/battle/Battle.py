from src.battle.Battlefield import Battlefield
from src.util.ActionType import ActionType


class Battle:
    """Runs battle turns and manges character actions"""

    def __init__(self, battle_field: Battlefield, turn_order: []):
        self._battle_field = battle_field
        self._turn_order = turn_order

    def start(self):
        # TODO: Rewrite how turn order works
        i = 0
        while(self.battle_still_going()):
            character = self._turn_order[i]
            action = character.take_action(self._battle_field)

            if (action.type == ActionType.MOVE):
                result = self._battle_field.move_character(character, action.result_pos)
            elif (action.type in ActionType.__members__):
                recipient = self._battle_field.get_occupant_by_position(action.result_pos)
                result = recipient.receive_attack(action)
            else:
                raise Exception

            # Update counter to keep looping through characters until battle over
            if i == (len(self._turn_order) - 1):
                i = 0
            else:
                i++

    def battle_still_going(self):
        pass