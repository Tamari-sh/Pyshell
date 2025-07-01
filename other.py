"""
File that contains a variant of shell commands functions.
"""
import os


def pyshell_pwd() -> None:
    """Function to print working directory"""

    print(os.getcwd())


def pyshell_echo(echo_lst: str) -> None:
    """Function to print wanted echoed strings"""
    # join the string to print
    echo = " ".join(echo_lst)
    print(echo)
