print("*++++++++++++++++++ Importing Examples +++++++++++++++++++++++")
print()

# ********************************************************************
# Developers don't write all the code needed for an application.
# Common things like accessing the internet or working with strings
# exist in modules as pre-written code. A developer can use the code
# in these modules instead of having to write that functionality
# themselves. This is common in most programming languages, but
# Python in particular is well known for having many packages that
# are easy to use. Many of these are built in and come with the
# language, but others need to be included and downloaded from the
# internet. The terms "modules" and "packages" are used interchangeably
# and each might be used more often depending on the language.
# 
# This file shows an example of how to use the `string`
# package, which is a built in package which provides functions
# that can be used to manipulate strings.
#
# All built in modules have documentation to show what they can
# do and how to use them. This is the documentation for the string
# module.
# https://docs.python.org/3/library/string.html
#
# Most other modules have documentation as well, which is provided
# by the person or group that created that module. One of the
# common skills of a software developer is actually learning how to
# vet packages.

# This next line will import the `string` package to use in this
# file. A variable named `string` will be imported which can provide
# functions and other variables that can only be accessed using
# the package. Accessing them is similar to other methods, using
# a dot to denote what is being accessed.
import string

# Now the `string` module can be used as if a variable named
# `string` was defined in this file. One of the values provided
# by this module is `punctuation`. This variable is a string of
# all the punctuation characters, and it is accessed by using a
# dot like `string.punctuation`.
print(f"Punctuation characters are {string.punctuation}")

# This function uses the `string.punctuation` variable to test
# if the given character is punctuation or not.
def is_punctuation(character):
    return character in string.punctuation

print(f"The character 'a' is punctuation: {is_punctuation('a')}")
print(f"The character '!' is punctuation: {is_punctuation('!')}")
print(f"The character '?' is punctuation: {is_punctuation('?')}")
print(f"The character '=' is punctuation: {is_punctuation('=')}")

# The string module also provides useful methods to format strings
# The string.capwords method will format the string so the first
# letter of word is capitalized but the other letters are lowercase.
mixed_case_str = "tHiS String IS all miXED uP!"
capwords_str = string.capwords(mixed_case_str)

print(f"After formatting, the string is '{capwords_str}'")

# Another way to use a module is to import a specific variable or
# function provided by the module. This next line will import only
# the capwords() function, which will make it available as if it
# was defined in this file similar to the is_punctuation function
# from above. The from keyword tells Python which module to look
# at, changing how the import keyword works to just import the
# one thing given.
from string import capwords

# Now, the capwords function is available without having to access
# it using the string module.
another_mixed_case_str = "anoTHER sTrinG IS alSo miXED uP!"
another_capwords_str = capwords(another_mixed_case_str)

print(f"After formatting another string, the value is '{capwords_str}'")

# Another way to import is to rename a module or value with the
# `as` keyword. These examples wouldn't be done normally, since
# the values have already been imported, but are still useful to see.

import string as s
from string import capwords as to_caps

capitalized_sring = to_caps("miXeD CasE STRing")
print(f"These are punctuation chars again: {s.punctuation}")
print(f"And this is capitalized: {capitalized_sring}")

# There are literally thousands of modules to use in Python. More
# built in modules can be found here:
# https://docs.python.org/3/py-modindex.html
#
# Modules written by people and organizations can be found here:
# https://pypi.org/project/pip/
#
# Often, the easiest way to find a module is by searching for it
# with Google or another search engine, but sites like pypi.org
# also have searches to help find a module.
#
# See if you can find a module that can easily get information
# about Instagram users and explore their profiles.