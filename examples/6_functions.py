print("++++++++++++++++++++ Function Examples +++++++++++++++++++++++")
print()

# ********************************************************************
# Like if statements, functions allow you to create blocks of code that
# are grouped together, but unlike conditions you can run the block
# of code in the function any time.
# 
# Using functions helps to organize code that's used in multiple
# places instead of repeating it.
#
# A function is first defined with the "def" keyword. Then, the name
# of the function, a set of values for it to use in parenthesis,
# ending in a comma. Like an if statement, the code block for the
# function must be indented.
#
# Later, in other parts of the code, the function can be used
# with some given values. This is calling a function, and the
# values or variables given to the function to use are said
# to be passed to the function. If the function has a result,
# then that value is returned using the return keyword. Not all
# functions need to return a value.

print("****** Function Examples *******")

# These are two simple functions that take two values and add
# or subract them. They expect two values to be given when they
# are called, and these values are put in two variables named
# x and y. The order of the values when the function is called
# correspond to the order of variables.
#
# The values that are given to a function are called its
# parameters, and they are said to be passed to the function.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Here, the add function is called with the values 1 and 4, which
# then become the values of x and y in the function. In this example
# x will be 1 and y will be 4, so the result of 1 + 4 will be returned
# and assigned to a variable named "sum".
sum = add(1, 4)
print(sum)

# Now, the subtract function will be used to subtract 2 from the value
# of the sum variable, assigning the result to difference. In this
# example, the value of the sum variable will be x in the function and
# the 2 will be the value of the y variable in the subract function.
difference = subtract(sum, 2)
print(difference)

# This function is more complex and does more than adding two numbers
# together. It prints the numbers that will be added and then the
# result of adding them together using the add function defined above.
# A function can call other functions in it's code block, which is
# very common in a program. It helps different parts of a program be
# organized into doing just one thing into code blocks that can be reused.
# Since it prints the value of the two numbers added together, it doesn't
# return a value, so it doesn't need to use the return keyword.
print()
print("***** Larger Function Example *****")

def add_and_print(x , y):
    print("Adding these numbers:")
    print(x)
    print(y)
    sum = add(x, y)
    print("The result is:")
    print(sum)

add_and_print(1, 4)

# Just like the other functions, variables can be passed instead
# of numbers.
print()
add_and_print(difference, sum)

# Finally, functions can be used together in the same line.
# When multiple functions are used together on the same line
# of code, the first thing that's done is running the functions.
# In general, you can think of a function like a placeholder,
# putting the result of the function in its place on the line
# of code it's on. 
print()
print("***** Combined Function Examples*****")

# Here, the subtract function is run first, and then the
# result is passed as the first value for the add function.
added_and_subtracted = add(subtract(3,2), 1)
print(added_and_subtracted)

# Here, the results of the add and subract functions are
# added together and passed into the print function
# to be shown in the console. First, the add function is
# called. Then, the subtract function is called. Finally,
# the results of each function are added together. This is
# kind of like the order of operations from math, where the
# functions are called first before anything else is done
print(add(2,3) + subtract(5,1))

#*********************************************************
# Try writing your own functions to do something simple.

# There are other ways to use and call functions, which
# are discussed more in the 8_strings.py file.