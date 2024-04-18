# Python Variables - Assign Multiple Values
# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Banana", "Apple", "Orange"
print(x)
print(y)
print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

a = b = c = "Orange"

print("\n" + a)
print(b)
print(c)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.

names = ["Otavio", "Henrique", "Sophie"]
x, y, z = names
print(x)
print(y)
print(z)