"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

import os
import sys

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for arg in sys.argv:
    print("1. Argument: ", arg)


# Print out the OS platform you're using:
# YOUR CODE HERE
print("2. Platform: ", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("3. Version: ", sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("4. Current Process ID: ", os.getpid())

# Print the current working directory (cwd):
print("5. Current Working Directory: ", os.getcwd())

# Print out your machine's login name
print("6. Login Name: ", os.getlogin())
