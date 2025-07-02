import os
import glob
import shutil
import sys
from colorama import Fore, Back, Style
import lzma
from man import MAN
from typing import Tuple, List


HISTORY_FILE = "history.xz"


def pyshell_ls(cmd: List[str]) -> None:
    """Function to recreate ls in python"""
    current_path = os.getcwd()

    if len(cmd) > 0 and cmd[0] != "":
        # if path of alternative directory passed
        path = cmd[0]
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for directory in dirs:
                    print(Fore.BLUE + directory)
                    dirs.remove(directory)
                for file in files:
                    print(Fore.GREEN + file)
        else:
            print(f"ls cannot access '{path}': No such directory")
    else:
        for root, dirs, files in os.walk(current_path):
            for directory in dirs:
                print(Fore.BLUE + directory)
                dirs.remove(directory)
            for file in files:
                print(Fore.GREEN + file)

    print(Style.RESET_ALL)


def pyshell_cd(path: str) -> None:
    """Function to change working directory"""
    path_split = path.split("/")
    current_path = os.getcwd()

    for folder in path_split:
        if folder == ".":
            continue
        if folder == "..":
            os.chdir(os.path.dirname(current_path))
        else:
            new_path = os.path.abspath(folder)
            if os.path.isdir(new_path):
                os.chdir(new_path)
            else:
                break


def pyshell_pwd() -> None:
    """Function to print working directory"""

    print(os.getcwd())



def pyshell_echo(echo_lst: List[str]) -> None:
    """Function to print wanted echoed strings"""
    # join the string to print
    echo = " ".join(echo_lst)
    print(echo)


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


def _parser_input(input_cmd: str) -> Tuple[List[str], str]:
    """Divide the given cmd input into command and params and flags list"""

    actions = input_cmd.split(" ")
    action = actions[0]
    actions.remove(action)

    return actions, action


def _add_to_history(action: str) -> str:
    """Log actions in compressed history file"""

    # if its a magic - don't log action in history
    if action.startswith("!") and not action.startswith("! "):
        return HISTORY_FILE
    else:
        with lzma.open(HISTORY_FILE, "a") as file:
            file.write(f"{action}\n".encode())
        return HISTORY_FILE


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
