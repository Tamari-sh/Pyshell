import os
import glob
import shutil
import sys
from colorama import Fore, Back, Style


def pyshell_ls() -> str:
    """Function to recreate ls in python"""
    current_path = os.getcwd()

    for root, dirs, files in os.walk(current_path):
        for directory in dirs:
            print(Fore.BLUE + directory)
            dirs.remove(directory)
        for file in files:
            print(Fore.GREEN + file)

    print(Style.RESET_ALL)


def main() -> None:
    pyshell_ls()


if __name__ == '__main__':
    main()
