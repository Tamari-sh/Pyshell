from colorama import Fore, Back, Style
from typing import Tuple, List
from history import pyshell_history, pyshell_history_magics, _add_to_history
from man import MAN
from other import pyshell_echo, pyshell_pwd
from dirs import pyshell_cd, pyshell_mkdir
from ls import pyshell_ls
from files import pyshell_cat, pyshell_touch


def _parser_input(input_cmd: str) -> Tuple[List[str], str]:
    """Divide the given cmd input into command and params and flags list"""

    params = input_cmd.split(" ")
    command = params[0]
    params.remove(command)

    return params, command


def pyshell() -> None:
    """The Pyshell main logic"""

    while True:
        # get action input with flags and params from user
        input_cmd = input("💗 ")
        # in case of magic cmd
        input_cmd = pyshell_history_magics(input_cmd)
        params, command = _parser_input(input_cmd)

        # create log
        _add_to_history(input_cmd)

        if command == "ls":
            pyshell_ls(params)
        elif command == "cd":
            pyshell_cd(params[0])
        elif command == "pwd":
            pyshell_pwd()
        elif command == "echo":
            pyshell_echo(params)
        elif command == "man":
            man_page = params[0]
            if man_page in MAN.keys():
                print(MAN[man_page])
        elif command == "history":
            pyshell_history()
        elif command == "cat":
            pyshell_cat(params[0])
        elif command == "touch":
            pyshell_touch(params[0])
        elif command == "mkdir":
            pyshell_mkdir(params[0])
        elif command == "quit":
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
