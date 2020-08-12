from src.ui import TerminalDisplay
from ui import TerminalUserInput


def terminal_display(battlefield):
        TerminalDisplay.render(battlefield)

def terminal_get_user_action():
        return TerminalUserInput.get_user_action()
