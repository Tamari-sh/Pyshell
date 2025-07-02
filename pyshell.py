from colorama import Fore, Style
from typing import Tuple, List
from history import pyshell_history, pyshell_history_magics, _add_to_history
from man import MAN
from other import pyshell_echo, pyshell_pwd
from dirs import *
from ls import pyshell_ls
from files import pyshell_cat, pyshell_touch


def _parser_input(input_cmd: str) -> Tuple[List[str], str]:
    """Divide the given cmd input into command and params and flags list"""

    params = input_cmd.split(" ")
    command = params[0]
    params.remove(command)

    return params, command


def _wrong_syntax(params: List[str]) -> bool:
    """Function to check if syntax used correctly"""

    return len(params) == 0


def _print_syntax_message(command: str) -> None:
    """Function print message to use syntax correctly"""

    print(f"{command}: missing operands\nTry 'man {command}' for more info")


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
            if _wrong_syntax(params):
                _print_syntax_message(command)
            else:
                pyshell_cd(params[0])
        elif command == "pwd":
            pyshell_pwd()
        elif command == "echo":
            pyshell_echo(params)
        elif command == "man":
            if _wrong_syntax(params):
                print("what manual page do you want?\nTry 'man [COMMAND NAME]'")
            else:
                man_page = params[0]
                if man_page in MAN.keys():
                    print(MAN[man_page])
        elif command == "history":
            pyshell_history()
        elif command == "cat":
            if _wrong_syntax(params):
                _print_syntax_message(command)
            else:
                pyshell_cat(params[0])
        elif command == "touch":
            if _wrong_syntax(params):
                _print_syntax_message(command)
            else:
                pyshell_touch(params[0])
        elif command == "mkdir":
            if _wrong_syntax(params):
                _print_syntax_message(command)
            else:
                pyshell_mkdir(params[0])
        elif command == "rmdir":
            if _wrong_syntax(params):
                _print_syntax_message(command)
            else:
                pyshell_rmdir(params[0])
        elif command == "quit":
            break
        else:
            print(f"{command}: command not found")
            continue


def main() -> None:
    """The Pyshell API"""

    print(Fore.MAGENTA + "✨ 💗 🎀  Welcome to the Python shell!!!  🎀 💗 ✨")
    print(Style.RESET_ALL)
    pyshell()


if __name__ == '__main__':
    main()
