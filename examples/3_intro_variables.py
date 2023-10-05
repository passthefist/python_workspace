print()
print("+++++++++++++++++ Intro Variable Examples +++++++++++++++++++")

# ********************************************************************
# Python has different types of values that can be
# stored in a variable. One of the most common
# are numeric types, but they're not the only
# one. Different types of variables can't be mixed,
# and it's useful to have types for variables to
# handle them differently. Words and numbers, for
# example, are different. It doesn't make sense to
# subtract a word from a number.

# These next two lines create variables called
# x and y, assigning them the values of 4 and 2
x = 4
y = 2

# ********************************************************************
# Since these variables store numbers, they can
# be used anywhere a number could be
print("addition")
print(4 + 2)
print(x + y)
print(y + x)

print("subtraction")
print(4 - 2)
print(x - y)

print("multiplication")
print(4 * 2)
print(x * y)

print("division")
print(4 / 2)
print(x / y)

# ********************************************************************
# Variables can be given new values, this is
# called reassignment.
print("reassigning x")
x = 6

# x is now six
print(x)
print(y)
print(x + y)

# ********************************************************************
# A variable can be reassigned the outcome of
# some operation. Here, y will now store the
# result of x - 2 instead of its original value.
#
# After, x is reassigned 4. This doesn't change
# the value of y, even though it's assigned x - 2.
# This is because the assignment was done before
# the value of x changed.
print("reassigning y")
y = x - 2
x = 4

print(x)
print(y)

# Now, x will increase by two
x = x + 2
print(x)

# ********************************************************************
# This is so common, there's a shorthand for it
# using the += operator. It means to increase
# the value in the variable by the amount on
# the right hand side.
x += 2
print(x)

# The same applies for subraction
x -= 2
# multiplication
x *= 2
# and division
x /= 2

# try printing the value of x on the next line.
# What do you think it will be?