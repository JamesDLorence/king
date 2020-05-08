from src.battle.Battlefield import Battlefield
from src.util.ActionType import ActionType


class Battle:
    """Runs battle turns and manges character actions"""

    def __init__(self, battle_field: Battlefield, turn_order: []):
        self._battle_field = battle_field
        self._turn_order = turn_order

    def start(self):
        i = 0
        while(self.battle_still_going()):
            character = self._turn_order[i]
            action = character.decide_action()

            if (action.type == ActionType.MOVE):
                result = self._battle_field.move_occupant(character, action.result_pos)
            elif (action.type == ActionType.ATTACK):
                recipient = self._battle_field.get_occupant_by_position(action.result_pos)
                result = recipient.receive_attack(action)
            elif (action.type == ActionType.MAGIC):
                recipient = self._battle_field.get_occupant_by_position(action.result_pos)
                result = recipient.receive_magic(action)
            else:
                raise Exception

    def battle_still_going(self):
        pass