from util.ActionValues import ActionType, Direction, Distance


#_valid_user_action = ['a']

def get_user_action() -> str:
    action_input = get_input("What is your action: ", ActionType)

    if action_input != ActionType.none:
        direction_input = get_input("What is your action: ", Direction)
        distance_input = get_input("Distance of action: ", Distance)
    else:
        direction_input = None
        distance_input = None

    return action_input, direction_input, distance_input

def get_input(text, values):
    valid_input = False
    while not valid_input:
        user_input = input(text)

        if user_input in values.__members__:
            valid_input = True
        else:
            print("Invalid action")

    return user_input

