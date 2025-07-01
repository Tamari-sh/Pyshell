import os
import glob
import shutil
import sys
from colorama import Fore, Back, Style


def pyshell_ls() -> None:
    """Function to recreate ls in python"""
    current_path = os.getcwd()

    for root, dirs, files in os.walk(current_path):
        for directory in dirs:
            print(Fore.BLUE + directory)
            dirs.remove(directory)
        for file in files:
            print(Fore.GREEN + file)

    print(Style.RESET_ALL)


def pyshell_pwd() -> None:
    """Function to print working directory"""

    print(os.getcwd())


def pyshell_echo(echo_str: str) -> None:
    """Function to print wanted echoed strings"""

    print(echo_str)
    

def main() -> None:
    """The Pyshell API"""

    print(Fore.MAGENTA + "✨ 💗 🎀  Welcome to the Python shell!!!  🎀 💗 ✨")
    print(Style.RESET_ALL)
    while True:
        action = input("💗 ")
        if action == "ls":
            pyshell_ls()
        elif action == "pwd":
            pyshell_pwd()
        elif action == "quit":
            break
        else:
            continue


if __name__ == '__main__':
    main()
