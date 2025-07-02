"""
File containing the ls command function (and hopefully flags later)
"""
import os
from colorama import Fore, Style
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
