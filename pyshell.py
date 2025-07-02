import os
import glob
import shutil
import sys
from colorama import Fore, Back, Style
from typing import List


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


def main() -> None:
    """The Pyshell API"""

    print(Fore.MAGENTA + "✨ 💗 🎀  Welcome to the Python shell!!!  🎀 💗 ✨")
    print(Style.RESET_ALL)
    while True:
        # get action input with flags and params from user
        input_cmd = input("💗 ")
        actions = input_cmd.split(" ")
        action = actions[0]
        actions.remove(action)

        if action == "ls":
            pyshell_ls(actions)
        elif action == "cd":
            pyshell_cd(actions[0])
        elif action == "pwd":
            pyshell_pwd()
        elif action == "echo":
            pyshell_echo(actions)
        elif action == "quit":
            break
        else:
            continue


if __name__ == '__main__':
    main()
