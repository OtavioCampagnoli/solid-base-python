# Global variables can be used by everyone, both inside of functions and outside.

# Example
# Create a variable outside of a function, and use it inside the function

x = "Otavio"

def myFunc():
    print("Name: " + x) # Name: Otavio

myFunc()

# If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

# example

def myFuncTwo():
    x = "Henrique"
    print("Name: " + x) # Name: Henrique
    
myFuncTwo()

print(x)