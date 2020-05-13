from src.ui.ValidUserInput import ValidUserInput


class UserInput:
-
    _valid_user_action = ['a']

    def get_user_action(self) -> str:
        valid_input = False
        while not valid_input:
            user_input = input("What is your action: ")

            if user_input in ActionType.__members__:
                valid_input = True
            else:
                print("Invalid action")

        if user_input == ActionType.magic

        return user_input


