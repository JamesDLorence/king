from src.ui import TerminalDisplay
from ui import TerminalUserInput


def terminal_display(battlefield, stats_list):
        TerminalDisplay.render(battlefield, stats_list)

def terminal_get_user_action(char_name):
        return TerminalUserInput.get_user_action(char_name)
