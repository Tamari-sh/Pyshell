"""
File containing history functions
"""
import lzma


HISTORY_FILE = "history.xz"


def pyshell_history() -> None:
    """Function that outputs the command history"""

    i = 1

    with lzma.open(HISTORY_FILE, "r") as history:
        lines_of_history = history.readlines()
        for line in lines_of_history:
            print(f"{i}   {line.decode()}")
            i += 1


def pyshell_history_magics(command: str) -> str:
    """Return a new command according to magic"""

    with lzma.open(HISTORY_FILE, "r") as history:
        lines_of_history = history.readlines()

    if command.startswith("!") and not command.startswith("! "):
        if command == "!!":
            action = lines_of_history[-1]
        elif command.startswith("!-"):
            index = len(lines_of_history) - int(command[2:])
            action = lines_of_history[index]
        elif command.startswith("!"):
            index = int(command[1:])
            action = lines_of_history[index]

        return action.decode()[:-1]

    else:
        return command


def _add_to_history(action: str) -> str:
    """Log actions in compressed history file"""

    # if its a magic - don't log action in history
    if action.startswith("!") and not action.startswith("! "):
        return HISTORY_FILE
    else:
        with lzma.open(HISTORY_FILE, "a") as file:
            file.write(f"{action}\n".encode())
        return HISTORY_FILE
