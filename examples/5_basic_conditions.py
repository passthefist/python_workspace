print("+++++++++++++++++ Basic Condition Examples +++++++++++++++++++")
print()

# ********************************************************************
# There's other operators than just the arithmetic ones,
# Python and many other languages have comparison operators
# that compare two values together.
#
# The result of a comparison is a Boolean value, which can
# only have a value of True or False.

print("** Comparison Results **")
# The "==" operator tests if two values are equal
print(2 == 2)
# The "!=" operator tests if two values are not equal
print(3 != 1)
# The ">" operator tests if the value on the left is greater than the right
print(1 > 2)
# The "<" operator tests if the value on the left is less than the right
print(1 < 2)

# ********************************************************************
# In Python, some words are reserved and cannot be used as variable
# or function names. One of these is the "if" keyword, which is used
# for what are called "if statements". A reserved keyword will be
# highligted differently in your code editor from a variable or
# function name.
#
# An if statement can be used with a condition to control if some
# code will be run or not. The if statement tests if the condition
# is True or False, and runs some code depending on the outcome.
# If statements and conditions are a core part of writing a
# program, allowing the behavior to change depending on user inputs
# or the values in a variable. They can control the flow the program
# is run in. Normally, a program just runs each line in order from
# top to bottom, but using an if statement tells the program to
# move instead to a different part of the program that might not
# be the next line when reading in order.
#
# If the condition being tested by the if statement is True, then
# the code belonging to that condition will run. If the condition
# results in False, the code belonging to that condition will be
# skipped. The code for an if statement can be read as "if this
# condition is true then do that".
#
# The code belonging to a an if statement is called a "block", and
# in Python a block of code is marked by indentation. The way the
# code is formatted matters, where it must be indented at the same
# level to be part of the same block.

# Here, the values True and False are used to demonstrate which
# part of the code will be run.
print()
print("** If Statements **")

if True:
    print("This line will always run because the condition is always True")
    print("This will also print since it's part of the same code block")

if False:
    print("This line will never run because the condition is always False")
    print("This will also never since it's part of the same code block")

# The not keyword can be used to invert a condition to the opposite value.
# Not False is True and not True is False.
if not False:
    print("This line will always run because the condition is always True")
    print("This will also print since it's part of the same code block")

# Here, the "2 == 2" condition checks if the value of 2 equals the value
# of 2, which will always be True. Since it's True, the code for the
# condition will run.
if 2 == 2:
    print("2 does, in fact, equal 2")

# Here, first 3 == 2 is checked, which is False. Since there's a not in
# front of it the full condition is True, because the opposite of False
# is True.
if not (3 == 2):
    print("3 does not, in fact, equal 2")

# Here, the "1 != 1" condition checks if the value of 1 does not equal
# the value of 1, which will always be False. Since it's False, the code
# for the condition will not run.
if 1 != 1:
    print("this line will not run, because 1 != 1 is False.")

# Any value can be compared, not just numbers. Try changing the strings
# in this if statement.
if "some string" == "some string":
    print("the strings are the same")

# Here, two variables are defined and compared. Try changing the values
# of the variables to make the condition true so the line is printed.
a = 1
b = 2

if a > b:
    print("a is greater than b")

# So far, the if statements of this program have only been used to print
# if the condition for the if was true, but if statements are usually used
# to do something more intersting, like changing variables.
#
# Here, if x is less than y it will increase x by 1 and decrease y by 1.
# 
# Try changing the values of x and y to see how it changes the output
# of the program.

x = 1
y = 5

print("The value of x before the if is:")
print(x)

if x < y:
    x += 1
    y -= 1

print("The value of x after the if is:")
print(x)