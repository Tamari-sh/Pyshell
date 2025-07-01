"""
File containing dir related shell functionality.
"""
import os


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

