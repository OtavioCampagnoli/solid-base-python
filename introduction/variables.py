"""Python Variables
    Variables
    Variables are containers for storing data values.

    Creating Variables
    Python has no command for declaring a variable.

    A variable is created the moment you first assign a value to it.
"""
x = 5
y = "Otavio"
print(x)
print(y)

# info: Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Campagnoli" # x is now of type str
print(x)
y = 10
print(y)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

a = str(21)
b = int(10)
z = float(3.3)

print(a)
print(b)
print(z)

# Get the Type
# You can get the data type of a variable with the type() function.

print(type(a)) # <class 'str'>
print(type(b)) # <class 'int'>
print(type(z)) # <class 'float'> 