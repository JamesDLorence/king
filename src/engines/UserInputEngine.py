from src.battle.Battlefield import Battlefield
from src.ui.TerminalUserInput import UserInput

class UserInputEngine:

    def decide_action(self, character: Character, battlefield: Battlefield):


        user_action_input = UserInput.get_user_action()

        battlefield.check_if_valid_move_position()
