"""
File containing the MAN dict.
"""

MAN = {"ls": """DESCRIPTION
List directory contents
 
SYNOPSIS
ls [OPTION]... [FILE]...  
 """,
       "cd": """DESCRIPTION
Change working directory
 
SYNOPSIS
cd [PATH]...
 """,
       "pwd": """DESCRIPTION
Print working directory
 
SYNOPSIS
pwd
 """,
       "echo": """DESCRIPTION
Display a line of text
 
SYNOPSIS
echo [STRING]...
 """,
       "history": """DESCRIPTION
Display that Pyshell history library
 
EVENT DESIGNATORS
An  event  designator  is  a reference to a command
line entry in the history list.

!      Start a history  substitution,  except  when
       followed by a blank, newline, or char other than -.
!n     Refer to command line n.
!-n    Refer to the current command minus n.
!!     Refer  to  the  previous command.  A
       synonym for `!-1'.
""",
       "cat": """DESCRIPTION
Print the output of a file
 
SYNOPSIS
cat [OPTION]... [FILE]...
 """,
       "touch": """DESCRIPTION
Create a new file
 
SYNOPSIS
touch [OPTION]... [FILE]...
 """,
       "mkdir": """DESCRIPTION
Create new directory
 
SYNOPSIS
mkdir [OPTION]... [DIRECTORY]...
 """}
