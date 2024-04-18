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

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# example

# if you want to create a global variable in a function, you can be use the global keyword

def testFunction():
    global y 
    y = "Testing"

testFunction()

print("I'm: " + y)

# if you want to change the value off a global variable created, you can use the keyword global nameVariable you want to change the value

def myAnotherTest():
    global x
    x = "Campagnoli"
    print("My Name is:" + x)
    
myAnotherTest()