"""
File containing dir related shell functionality.
"""
import os
import os.path


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


def pyshell_mkdir(directory: str) -> None:
    """Function to create directories"""

    os.mkdir(directory)


def pyshell_rmdir(directory: str) -> None:
    """Function to remove directories"""

    if os.path.isfile(directory):
        print(f"rmdir: failed to remove '{directory}', not a directory")
    else:
        try:
            if input("Are you sure? (y/n)") == "y":
                os.rmdir(directory)
            else:
                print("Operation failed")
        except FileNotFoundError:
            print(f"rmdir: failed to remove '{directory}', no such file or directory")
