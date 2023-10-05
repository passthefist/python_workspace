print("*+++++++++++++++++++ Simple Loop Examples ++++++++++++++++++++++++++")
print()

# ********************************************************************
# If statements are not the only way to control the order that
# a program is run in. Loops are another important way to control
# the flow of a program. A loop does what it sounds like, looping
# the program to run the same code over and over. Just like if
# statements and functions, the code in a loop is a block.
#
# Python has two types of loops, `for` loops and `while` loops.
# Each has different uses but do similar things - repeat a block
# of code until some condition is met.

print("********* While Loops **********")
# Like an if statement, a while loop has a condition. It will
# repeat a block of code as long as that condition is True.
# Each time the block of code ends, instead of continuing to
# the next line below it as normal, the program jumps back to
# the top of the While loop, but only if the condition of the
# while loop is still true. Otherwise it does continue to the
# next line as normal.
# A good way to think of it is "while this is true, do this".

count = 0

# This loop will increment count as long as its value is less
# than 10, so it will count from 0 to 9.
while count < 10:
    print(f"The count is {count}")
    count += 1

print("The while loop has exited.")
print(f"The final value of count is {count}")

# Another way to use a while loop is to use the `break` statement
# to break out of it even if the condition of the loop is stil true.
#
# This loop is similar, but will break early. Note that the print
# function in the loop isn't run when the loop breaks. This is
# because a break will jump the code to the end of the loop.

print("*This loop has a break*")
count = 0
while count < 10:
    if count == 5:
        break
    print(f"The count is {count}")
    count += 1

print("The while loop has exited.")
print(f"The final value of count is {count}")

# Just like if statements, while loops can contain while loops.
# This loop is a more complex, it's using two variables. The
# x variable is used in the outer loop while the y variable is
# used in the inner loop. This loop will print the value of
# x the same number of times as its value, so when x is one
# it will print one time, when x is two it will print two
# times, etc.
#
# How do the two loops work together to do this?

print("*This loop has a loop inside it*")
x = 0

while x < 5:
    x += 1
    print(f"The value of x will print {x} times:")

    y = 0
    while y < x:
        y += 1
        print(x)

print("The while loop has exited.")

# So, to sum up, a while loop will jump the program flow to the
# top of the loop when the block of code in the loop ends, but
# only if the condition of the loop is met. However, the break
# statement will force the program flow to jump to the end of
# the loop's code block.

# Be careful with while loops, and make sure that the condition
# will eventually be false, otherwise they will loop forever
# without stopping. This is called an infinite loop.
#
# Try uncommenting the code in this comment and see what happens
#
# count = 1
# while count > 0:
#    count += 1
#    print(f"The count is {count}")

print()
print("********* For Loops **********")

# **********************************************************
# A for loop is similar to a while loop, where it loops over
# block of code until some condition is met. However, it is
# different in that it uses a list as part of that condition.
#
# It goes through each item in the list, and then runs the
# code block for the loop with the item in a variable for
# the loop to use. For example, this loop is the same as
# the first while loop that counts to 9. Going through a
# list in this way is called iterating.
#
# A good way to think of it is "for these items, do this
# with each one"

list_of_numbers = [0,1,2,3,4,5,6,7,8,9]

# The in keyword is used with a for loop to 
for count in list_of_numbers:
    print(f"The count is {count}")

print("The for loop has exited.")
print(f"The final value of count is {count}")

# Since this is very common, Python has a built in
# function to create a list of numbers called range().
# This will create a list from 0 up to but not
# including the number given.
# In this case, it will be the numbers 0 to 9.

print("*This for loop uses a range*")
for count in range(10):
    print(f"The count is {count}")

print("The for loop has exited.")
print(f"The final value of count is {count}")

# For loops can also use a break in the same way
# as a while loop.

print("*This for loop uses a break*")
for count in range(10):
    if count == 5:
        break
    print(f"The count is {count}")

print("The for loop has exited.")
print(f"The final value of count is {count}")

# For loops can also contain for loops. This one
# does the same thing as the other while loop,
# to print the value of x a number of times
# equal to the value of x. It will start with x=1
# and end with x=5, same as the while loop.

for x in range(1,6):
    print(f"The value of x will print {x} times:")

    for y in range(x):
        print(x)

# Each loop has different uses, but for loops are often
# simpler for more cases. In general, if you need to
# do something with each item in a list, a for loop
# will be better.
#
# If you need to do something until some condition is
# met, then a while loop will be better.