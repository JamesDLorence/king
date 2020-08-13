from util.ActionValues import ActionType, Direction, Distance


#_valid_user_action = ['a']

def get_user_action(char_name) -> str:
    action_input = get_input(char_name + " - What is your action: ", ActionType.__members__)

    if action_input != ActionType.none.name:
        direction_input = get_input(char_name + " - In what Direction: ", Direction.__members__)
        distance_input = int(get_input(char_name + " - At what distance: ", [str(e.value) for e in Distance]))
    else:
        direction_input = None
        distance_input = None

    return action_input, direction_input, distance_input

def get_input(text, valid_values):
    valid_input = False
    while not valid_input:
        user_input = input(text)

        if user_input in valid_values:
            valid_input = True
        else:
            print("Invalid action")

    return user_input

