from colorama import Fore, Back, Style
from typing import Tuple, List
from history import pyshell_history, pyshell_history_magics, _add_to_history
from man import MAN
from other import pyshell_echo, pyshell_pwd
from dirs import pyshell_cd
from ls import pyshell_ls


def _parser_input(input_cmd: str) -> Tuple[List[str], str]:
    """Divide the given cmd input into command and params and flags list"""

    actions = input_cmd.split(" ")
    action = actions[0]
    actions.remove(action)

    return actions, action


def pyshell() -> None:
    """The Pyshell main logic"""

    while True:
        # get action input with flags and params from user
        input_cmd = input("💗 ")
        # in case of magic cmd
        input_cmd = pyshell_history_magics(input_cmd)
        actions, action = _parser_input(input_cmd)

        # create log
        _add_to_history(input_cmd)

        if action == "ls":
            pyshell_ls(actions)
        elif action == "cd":
            pyshell_cd(actions[0])
        elif action == "pwd":
            pyshell_pwd()
        elif action == "echo":
            pyshell_echo(actions)
        elif action == "man":
            man_action = actions[0]
            if man_action in MAN.keys():
                print(MAN[man_action])
        elif action == "history":
            pyshell_history()
        elif action == "quit":
            break
        else:
            continue


def main() -> None:
    """The Pyshell API"""

    print(Fore.MAGENTA + "✨ 💗 🎀  Welcome to the Python shell!!!  🎀 💗 ✨")
    print(Style.RESET_ALL)
    pyshell()


if __name__ == '__main__':
    main()
