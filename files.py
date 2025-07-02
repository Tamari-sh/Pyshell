"""
File containing file related shell functionality.
"""
import os
import os.path
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

    if os.path.exists(os.path.abspath(src)):
        shutil.move(os.path.abspath(src), os.path.abspath(dst))
    else:
        print(f"mv: cannot stat '{src}', no such file or directory")


def pyshell_cp(src: str, dst: str) -> None:
    """Function to copy files or directories"""

    pass


def pyshell_rm(file: str) -> None:
    """Function to remove files or directories"""

    if os.path.isfile(file):
        if input("Are you sure? (y/n)") == "y":
            os.remove(file)
        else:
            print("Operation failed")
    elif os.path.isdir(file):
        print(f"rm: cannot remove '{file}', is a directory")
    else:
        print(f"rm: cannot remove '{file}', no such file or directory")
