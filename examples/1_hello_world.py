# This is a very simple Python program that just displays
# some text in the console. A program is run from top to
# bottom and left to right like reading a text document.
# Each line is run in order, one at a time and tells the
# program to do something. 
#
# These first lines that start with the hash symbol are
# comments. A comment is skipped when the program runs.
# This lets developers put notes in a program for other
# devs to read to give context to their code without
# affecting the behavior of the program. Different
# languages have different styles for comments and this
# is how Python does it.

# Below this comment is the first line of the program.
# It creates a variable named `text_to_output``
# A variable stores values in a program to be used later.
# In this case the value stored is the number 100.

number_to_output = 100

# This line uses a function to print some text to the console.
# A function is used to perform a specific task and can be
# given values to use in that task. The print() function's
# task is to output the given value to the console, and in
# this case it will print the text "hello world!".
# Python includes many functions by default, and print
# is on of them. When you run this program, take note of
# the order that things are printed in. They match the order
# of the prints in this program.
print("This is a simple Python program.")

# The print function can be called with no values to just
# output an empty line
print()

# In this case, the print function will output what is
# stored in the text_to_output variable. Try changing the
# value stored in the variable above and running this
# program again.
print("This program will now print a number.")
print(number_to_output)
