print("++++++++++++++++++++ String Examples +++++++++++++++++++++++")
print()

# ********************************************************************
# Strings are one of the most common types of data used
# in a program. There's lots of things that can be done
# with strings, and knowing how to manipulate them is
# important.
#
# Python has many built in functions for manipulating
# strings, some of which are covered here.

# ********************************************************************
# One of the most common things done with strings is joining them
# together and using them to print dynamic text.
#
# While the "+" operator for numbers adds them together, the "+"
# operator for strings concatenates them, or appends the second
# string to the first one

print("****** Concatenation Examples ******")

first_string = "yellow"
second_string = "banana"

print(first_string + second_string)

# The print above isn't formatted well, the two strings are bunched
# together making it hard to read. Adding a space between then would
# make them easier to read, with you can do by concatenating them
# together. Here, a space is added to make it more readable.
print(first_string + " " + second_string)

# ********************************************************************
# Another way to format strings is by dynaimcally inserting them as
# variables in another string using a special pattern. Instead of
# starting the string like normal with a double quote, starting a
# string with an f before the double quote tells Python that this
# string will be formatted with some variables inserted. This is
# called string interpolation.
# 
# By using by a pair of brackets like {} with a variable inside them,
# the varuable will be instered in place of that pattern in the string.
# This special pattern can be used to more easily create dynamic text.
print()
print("****** Interpolation Examples ******")

# Here, the strings defined above are inserted into short sentence.
print(f"A ripe {second_string} is {first_string}.")

# Without the f, the variables aren't inserted.
print("A ripe {second_string} is {first_string}.")

# A formatted string can be assigned to a variable like any other string.
sentence = f"The sun is {first_string}, but it's not a {second_string}!"
print(sentence)

# Numbers and other variable types also work. Try changing count
# to one see the difference in the output
count = 5
if count > 1:
    conditional_string = f"There are {count} rotten {second_string}s."
else:
    conditional_string = f"There is {count} rotten {second_string}"

print(conditional_string)

# And the value in the curly braces doesn't have to be a variable.
# It could be an expression, too.

a = 7
b = 4

print(f"The sum of a + b is {a + b}")

# ********************************************************************
# There are also functions you can use to do more with strings. These
# functions are used differently from the ones in the 7_functions.py
# file. Those kinds of functions are called with just some values, but
# another type of function is called on a value or variable as well.
#
# Calling this kind of function has a different format, where a
# variable or value comes first, then a dot, and then a function
# as before. A function that is used this way is called a method
# to differentiate it from the other style of functions, and the
# value or variable before the dot is the object that will be
# acted on when the method is called. This style of function is
# useful compared to the other one to be clear that something is
# being done with the value or variable before the dot. It also
# helps with organizing and reading code when writing more advanced
# programs that have complicated behaviors and logic.
#
# A few of them are shown in this fie, but there's tons of methods
# for manipulating strings. This is a full list of all of the ones
# that are built in to Python:
#
# https://docs.python.org/3/library/stdtypes.html#string-methods
# 
# While this kind of documentation can be a lot to read at first,
# it shows all the built in methods for strings. Learning how to
# read this kind of documentation is an important skill for software
# development to find information to solve or understand a problem.

print()
print("****** Method  Examples ******")

# As an example, to convert a string from lowercase to uppercase,
# you can use the upper() method to return an uppercase version
# of that string. Here, the an uppercase version of the string
# "lowercase" will be returned, so the uppercase_string variable
# will have a value of "LOWERCASE".

uppercase_string = "lowercase".upper()
print(f"This is an uppercase string: '{uppercase_string}'.")

# Similarly, the lower() method returns a lowercase version of
# a string. Here, the value assigned to the variable lowercase_string
# will be a lowercase version of uppercase_string. Thus, the value
# of lowercase_string will be "lowercase".

lowercase_string = uppercase_string.lower()
print(f"This is an lowercase string: '{lowercase_string}'.")

# There's many methods that can be used with strings.
# A useful one is strip, which strips away extra whitespace at the
# beginning and end of a string. This helps to standardize user input
# that might have unexpected whitespace.

string_with_whitespace = " words go here  "
stripped_string = string_with_whitespace.strip()

print(f"This string has been stripped of extra whitespace: '{stripped_string}'.")

# These kinds of methods can take values just like the other functions.
# The count method returns the number of times the given value occurs in a string.

sentence = "My cat and my dog don't like my bird, but they do like each other."
my_count = sentence.count("my")
like_count = sentence.count("like")
# The value doesn't have to be a word, it can be anything.
str_count = sentence.count("rd, b")
# And if the value isn't in the string, it returns zero.
fish_count = sentence.count("fish")

print(f"The value 'my' occurs in the sentence {my_count} like_count")
print(f"The value 'like' occurs in the sentence {like_count} times")
print(f"The value 'rd, b' occurs in the sentence {str_count} times")
print(f"The value 'fish' occurs in the sentence {fish_count} times")

# ********************************************************************
# Another common thing done with strings is converting them
# into other values, such as numbers.
#
# To convert a string to another type, you need to know that
# the string can be converted and the type to convert to.
# If the string can't be converted, then it will create an
# error, so knowing that it can be converted is important.

print()
print("****** String Converting Examples ******")

# To convert a string to an integer, use python's built in
# int() function.

num = int("5")
print(type(num))
print(num + 2)

# **try uncommenting the lines below and seeing what happens**
# num = int("five")
# num = int(" 5 ")
# num = int("5.0")

# To convert to a decimal, or floating point number, use
# the float() function.
num = float("-5.3")
print(type(num))
print(num + 10.3)

# **try uncommenting the lines below and seeing what happens**
# num = float(" 5.0 ")
# num = float("5")

# It's a good idea to check if a string is numeric before converting it.
def print_if_numeric(string):
    if string.isnumeric():
        print(f"The value '{string}' is numeric.")
    else:
        print(f"The value {string} is not numeric.")

print_if_numeric("5")
print_if_numeric("five")

# ********************************************************************
# Finally, the strings so far have started and ended with a double
# quote. But what if you want to have a double quote in a string?
# There's two ways to do this.

print()
print("***** String Defining and Escape Sequences *****")

# First, strings can start and end with a single quote instead, but
# then you can't simply use a single quote inside a string. If the
# string starts and ends with double quotes, then it can have a
# single quote since it's not defining the start and end of the string.

print("This string starts with double quotes so using ' is fine.")
print('This string starts with single quotes so using " is fine.')

# The other way to do it is by using what's called an escape sequence.
# An escape sequence is a special pattern that lets Python know how
# to read a character that can't easily be used otherwise. There's a
# lot of escape sequences but a few common ones, and they always
# start with a backslash. They're called escape sequences because
# as the program reads the string from left to right, if it sees
# a backslash it knows to escape from how it normally reads a string
# to do something special.
print("Using a backslash lets you include \" in a string.")

# This means that a backslash like \ needs to be escaped as well.
print("To print a backslash like \\, you need to escape it in the same way.")

# Another common one is a newline, which is like including a return in
# the string to go to a new line. Here, the \n escape sequence is like
# replacing each use of it with pressing the return key.
print("This is the first line of the string.\nAnd this is the second line.\nAnd this is the third.")