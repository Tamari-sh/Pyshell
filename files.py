"""
File containing file related shell functionality.
"""
import os
import shutil


def pyshell_cat(file_name: str) -> None:
    """Function to read file content"""

    if os.path.isfile(file_name):
        with open(file_name, "r") as file:
            try:
                cat = file.read()
                print(cat)
            except UnicodeDecodeError:
                print(f"cat: '{file_name}' can't read file")
    elif os.path.isdir(file_name):
        print(f"cat: '{file_name}' is a directory")
    else:
        print(f"cat: '{file_name}' no such file or directory")


def pyshell_touch(file_name: str) -> None:
    """Function to create a new file"""

    with open(file_name, "w") as new_file:
        new_file.write("")


def pyshell_mv(src: str, dst: str) -> None:
    """Function to move or rename files"""

    pass
