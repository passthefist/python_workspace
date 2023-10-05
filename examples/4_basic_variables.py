print("++++++++++++++++ Basic Variable Examples +++++++++++++++++++")
print()

# ********************************************************************
# Variables can hold different kinds of data, and
# these are referred to as variable types. Variables
# of different types are treated differently in a
# program, for example text and numbers can't be
# added together since that doesn't really make sense.

# These first four variables are numeric types.
# Variables can have any name as long as it follows
# the rules. A variable name can have any letter or
# number, or an underscore (_). It can't start with
# a number, and variable names are case sensitive so
# another_number and Another_Number are different.
a_number = 5
another_number = 6
Another_Number = 7.5
twenty5 = 25

# ********************************************************************
# These next two are text types. Python and many other
# languages call text types "strings".
a_string = "7"
another_string = "Some text :)"

# ********************************************************************
# These next two are boolean types. Boolean types can
# only have two values, true or false, and are used
# for logic.
a_boolean = True
another_boolean = False

# ********************************************************************
# In Python, we can get what the type of a variable is
# with the type() function.
# Python refers to these types as "int" for integer,
# "str" for string, and "bool" for boolean.
print("*** Testing Variable Types ***")

print("The type of the a_number variable is:")
print(type(a_number))

print("The type of the a_string variable is:")
print(type(a_string))

print("The type of the a_boolean variable is:")
print(type(a_boolean))

# Python also has a special type called None. The None type can
# only have one value, None, and is used to represent when
# a variable exists but doesn't have a value. It's also used
# to represent that the program doesn't know what value a
# variable should have.

empty = None

print("The type of the empty variable is:")
print(type(empty))

# ********************************************************************
# What happens if we reassign a new value of a different
# type to one of these variables?

a_boolean = "some string instead"

print("The new type of the a_boolean variable is:")
print(type(a_boolean))

# ********************************************************************
# What happens when we mix variable types or add them together?
print()
print("*** Examples for mixing types ***")

# Numbers can of course be added together. Note that these
# are actually different variables because one is capitalized.
print(another_number + Another_Number)

# But what happens if we try to add some strings?
print("first string" + " and a " + "second string")
print(a_string + another_string)

# ********************************************************************
# One of the strings has a value of "5", which looks
# like a number. What happens if we try to add it
# to one of the numeric variables? Try uncommenting
# the line below. When you do, you'll see an error.

# print(a_string + a_number)

# When you run the program with the line above, you
# will see an error that looks like this:
#
# Traceback (most recent call last):
#   File "./simple_variables.py", line 43, in <module>
#     print(a_string + a_number)
# TypeError: can only concatenate str (not "int") to str
#
# So what does this error mean? First, it shows where
# the error occured with the line number in the file
# simple_variables.py, plus the code on the line
# that caused the error. Then, it show what kind of
# error ocurred and a message about the error. Note
# that it's a "TypeError", meaning that the error
# was from trying to do something with the wrong
# type of value. The message says that Python can
# only contatenate values of type str (string), to
# strings. Basically, these types can't be mixed like this.
#
# Being able to read errors is an important skill
# to fix programs when they aren't working.