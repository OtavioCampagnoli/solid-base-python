# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

# Python uses indentation to indicate a block of code.

if 5 > 2:
    print("Five is greater than two!")

# if 5 > 2:
# print("Five is greater than two!")

# IndentationError: expected an indented block after 'if' statement on line 12

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:


if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")