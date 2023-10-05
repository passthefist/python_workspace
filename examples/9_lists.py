print("*+++++++++++++++++++ List Examples ++++++++++++++++++++++++++")
print()

# ********************************************************************
# Variables can be more than just numbers and strings.
# Some variables group together other variables, such
# as having a list of numbers instead of being only
# one number. Lists are one of the most useful variable
# types used in Python, but that is also true for other
# languages. These kinds of complex variable types allow
# a program able to keep track of groups of data. Some
# common for a list might be having a list of available
# dates for a hotel or a list sales made in the last month.

# To create a list, the values for the list are written
# between square brackets. Here, this creates a list
# with the numbers 1 through 4.
print("***** List Types *****")
a_list = [1,2,3,4]

print("The value of a_list is:")
print(a_list)

# Just like other variables, we can get the type of the
# a_list variable with the type() function.
print("The type of a_list is:")
print(type(a_list))

# And just like other variables, lists can be inserted
# into strings the same way.
print(f"The value of a_list is: {a_list}")

# Lists can store any value, even if they are different types. 
words = "this is a string"
mixed_list = [7, -5.3, words, 87, "howdy"]

print(f"The value of mixed_list is: {mixed_list}")

# Lists can even store other lists
list_of_lists = [a_list, [7,8,9], words]
print(f"The value of list_of_lists is: {list_of_lists}")

# ********************************************************************
# Since lists contain items, they also have a length to show how
# many items they contain. This is done with the len() function.

print()
print("**** List Length ****")

list_length = len(a_list)
print(f"The a_list list has {list_length} items.")

# If a list contains lists, it's length doesn't count the number of
# itemsin each list it contains. Each is considered one item like
# any other variable.

list_of_lists_len = len(list_of_lists)
print(f"The list_of_lists list has {list_of_lists_len} items.")

# ********************************************************************
# Since lists store values, often a program needs to get a specifc
# value from the list. Lists keep the values they contain in order.
# A value can be gotten from the list by knowing where it is in that
# order, and using the position it is store in the list. This is
# called accessing a list.
#
# To get a value, the square brackets are used again with the
# position of the desired value in between the brackets. The position
# is the offset from the start of the list, so the first item is at 
# position 0, the second at position 1, the third at position 2, etc.
# This can take a bit to get used to, but it's how most programming
# languages keep track of the items in a list.

print()
print("***** Accessing List Values *****")

# This gets the first item from the a_list variable, which is zero
# positions away from the start
one = a_list[0]
# This gets the 5th item from the mixed_list variable, which is 4
# positions away from the start
howdy = mixed_list[4]
# This gets the second item from the list_of_list variable, which
# is 1 position away from the start.
seven_eight_nine = list_of_lists[1]

print(one)
print(howdy)
print(seven_eight_nine)

# You can also set the value of an item in a list if you know
# the position it is in.

print(f"Before updating values, a_list is {a_list}")

a_list[1] = 3
a_list[2] = 5

# You can also get the value from one list and set it in another.
a_list[3] = mixed_list[0]

# Note that the first item is the same, since it wasn't changed.
print(f"After updating values, a_list is {a_list}")

# ********************************************************************
# Lists can also be concatenated together in the same way as strings.
# Lists have a lot in common with strings, and strings can be thought
# of as lists that contain characters. Many things that can be done
# with lists can also be done with strings or work similarly.

print()
print("**** Concatenating Lists ****")

one_through_three = [1,2,3]
four_through_six = [4,5,6]

one_through_six = one_through_three + four_through_six

# You can get a character from a string the same way as a list
chicago = "Chicago, Illinois"
capital_i = chicago[9]
print(f"The 10th letter of 'Chicago, Illinois' is '{capital_i}'.")

# ********************************************************************
# Just like strings, lists have useful methods to interact with
# them and the values they contain.

print()
print("***** List Methods *****")

# A common one is sorting a list so that the values are in order.
# This is done with the sort() method. This modifies the order of
# the items in the list itself, and so doesn't return anything.

sorting_list = [4,5,3,1,2]

print(f"Before sorting the list is {sorting_list}")
sorting_list.sort()
print(f"After sorting the list is {sorting_list}")

# Another common one is adding a new item to a list. This
# can be done with the append() method, which takes the item
# to be added as it's only value. Just like sort(), it modifies
# the list and doesn't return anything.

sorting_list.append(6)

print(f"After appending the list is {sorting_list}")

# You can remove an item from a list with the remove() method.
# It takes in the item to remove and removes it from the list,
# if the item isn't found then it raises an error, so be sure
# that the value is in the list.

# One of these things is not like the others.
animals = ["shark", "gorilla", "wallaby", "apple", "elephant"]
print(f"Before removing, the animals are {animals}")
animals.remove("apple")
print(f"After removing, the animals are {animals}")

# The in keyword can be used to check if an item is in a list.
# This can be used before removing to make sure an item is
# in a list before removal, but it's also useful any time you
# want to know if a list contains an item. 
list_contains_tiger = "tiger" in animals
list_contains_elephant = "elephant" in animals

print(f"The list of animals contains 'tiger': {list_contains_tiger}")
print(f"The list of animals contains 'elephant': {list_contains_elephant}")

# Another way to remove an item is using the del keyword.
# This removes an item at a given position. It looks similar
# to accessing an item, but then it removes that item from
# the list.

# Sharks are sea animals, and the others are land animals.
# If we remove it, then there's only land animals in the list.
# We know it's at the first position, or position 0.
del animals[0]

print(f"After removing again, the animals are {animals}")
print(f"There are {len(animals)} in the list now.")

# Many functions that work with lists also work with strings,
# and you can even think of strings as lists where all the items
# are letters!
fruit = "apple"
second_letter = fruit[1]

print(f"The 2nd letter of {fruit} is {second_letter}")
print(f"Apple has {len(fruit)} letters")
print(f"The letter f is in {fruit}: {'f' in fruit}")