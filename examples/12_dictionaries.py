print("*++++++++++++++++++ Dictionary Examples +++++++++++++++++++++++")
print()

# ********************************************************************
# Lists keep track of items as, well, a list where each item has its
# own position in the list. Another type of complex variable is a
# dictionary, which also stores items. A dictionary stores items in
# slots, where each slot has a name or label. Unlike a list, which
# keeps its items in ordered postitions, the slots of a dictionary
# have no order. It's best to think of a dictionary like a filing
# cabinet, with labeled drawers that store items. The items stored
# in these drawers can be looked up by the name of the drawer. The
# name of the drawer or slot is called a "key", and the item
# corresponding to that key its "value".
#
# Or, another way to think of it is as a table, where each item
# as a name in the table. Either way, the important part is remembering
# that a dictionary stores pairs of keys and values that correspond
# to each other.

# Creating a dictionary looks like this, with the curly brackets
# starting and ending the dictionary and then the items in between
# them. Each of the pairs separated by a colon is a slot, where
# the left part of the colon is the slot's key and the right part
# the slot's value. It's always like
#
# <key>: <value>

# Here, the dictionary creates a quick way to look up the capitol
# for a state by the state's name.
state_capitols = {
    "Illinois": "Springfield",
    "New York": "Albany",
    "California": "Sacramento",
    "Iowa": "Des Moines"
}

# The len function can be used to get the length of the dictionary.
state_length = len(state_capitols)
print(f"The number of states in the dictionary is {state_length}")

# To look up a capitol by state, it looks similar to finding an
# item in a list by its position. 

illinois_capitol = state_capitols['Illinois']
print(f"The capitol of Illinois is {illinois_capitol}")
california_capitol = state_capitols['California']
print(f"The capitol of California is {california_capitol}")

# A new item can easily be added like this
state_capitols["Maine"] = "Augusta"

# The value in between the curly braces can be an expression,
# sometimes it's simpler to use the expression instead of
# assigning to a variable first.
print(f"The capitol of Maine is {state_capitols['Maine']}")

# However, this isn't the safest way to get a value from a
# dictionary when looking it up by its key.
# If a key is not in a dictionary when accessing it this way,
# it will cause a 'KeyError'. Try commenting out this line of
# code and running the program.
#
# ohio_capitol = state_capitols["Ohio"]

# The safest way to get a value from a dictionary is using the
# get() method. It takes a key as the function's parameter.
# If the key doesn't exist, it returns the special value None.

ohio_capitol = state_capitols.get("Ohio")
print(f"The dictionary has {ohio_capitol} for the capital of Ohio.")
print(f"The dictionary has {state_capitols.get('California')} for the capital of California.")

# Like lists, a dictionary can contain a mix of variable types, even
# other dictionaries. Similarly, keys can be anything, they don't
# have to be strings.
mixed_dict = {
    "list": [0,1,2,3],
    "string": "words",
    "number": 5,
    "dictionary": state_capitols,
    17: "numeric key"
}

print(f"The mixed dictionary looks like this: {mixed_dict}")
print(f"It has {len(mixed_dict)} items.")

# Even though the dictionary only has 5 items, the key 17 can be
# used to get one of the items since dictionaries don't care about
# the position of the items.

# ********************************************************************
# Like lists, dictionaries can be used with the `in` keyword to check
# if they contain a key. It only checks the key, or the left side of
# the dictionary, not the value, or the right hand side. 

print()
print("***** Containment Examples *****")

# Ohio is not in the dictionary, so this will not be printed
if "Ohio" in state_capitols:
    print("Ohio is in the state_capitols dictionary")

# Maine is in the dictionary, so this will be printed
if "Maine" in state_capitols:
    print("Maine is in the state_capitols dictionary")

# Even though Augusta is in the dictionary, it's a value not
# a key. The in keyword only looks at keys, not values, so
# this condition is false.
if "Augusta" in state_capitols:
    print("Augusta is in the state_capitols dictionary")

# ********************************************************************
# Dictionaries can be used in a for loop similar to a list.
print()
print("***** Loop Examples *****")

# The keys() method can be used to get the keys in a dictionary.
print(f"The states in the dictionary are {state_capitols.keys()}")

# The values() method can be used to get the values in a dictionary.
print(f"The cities in the dictionary are {state_capitols.values()}")

# And these can be used in a for loop
for state in state_capitols.keys():
    print(f"The city of {state} is in the dictionary.")

for capitol in state_capitols.values():
    print(f"The city of {capitol} is in the dictionary.")

# More commonly, though, a for loop is used to loop over both
# the key and value of a dictionary at the same time. So far
# the for loops in these examples have only used one variable
# at a time, but there can be more than one variable in a loop
# in Python.
#
# To use a for loop like this, the variables defined by the loop 
# are separated by a comma.
#
# The items() method can be used with a loop to get both the
# keys and the values.

for state, city in state_capitols.items():
    print(f"The capitol of {state} is {city}")

# ********************************************************************
# And items can be removed from a dictionary like lists as well
print()
print("***** Loop Examples *****")

del state_capitols["Iowa"]

# Note that both the key and value are removed
print(f"The states in the dictionary after removal are {state_capitols.keys()}")
print(f"The cities in the dictionary after removal are {state_capitols.values()}")

# Dictionaries are a powerful variable type to use, can be make
# programming anything where you might want to keep a table of
# values easier.