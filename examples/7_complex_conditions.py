print("++++++++++++++++ Complex Condition Examples ++++++++++++++++")
print()

# ********************************************************************
# An if statement can be followed by an "else" statement.
# The code in the else part is run when the condition for
# the if statement is false. The code can be read as
# "If this is true then do that, or else do this other thing instead"

print()
print("** If Else Examples **")

if 1 > 2:
    print("this line won't be run, since 1 is not greater than 2")
else:
    print("since 1 is not greater than 2, this line will run")

# ********************************************************************
# An if statement can also be followed by an "elif" statement,
# which is short for else if. It can be read as "If this is
# true then do that, or else if this other thing is true then
# do this instead"
#
# It can be used with an "else" statement to perform more complex
# behaviors.

# Here, these if, elif, and else statements create some logic
# to test if one value is bigger than another or if they are equal.
#
# Try changing the values of x and y to see what happens.

x = 2
y = 3

if x > y:
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
else:
    print("x equals y")

# Strings can be compared alphapetically
# Try changing these strings and seeing the results
if "alligator" > "zebra":
    print("The words are in alphabetical order")
else:
    print("The words are in reverse alphabetical order")

# ********************************************************************
# More than one condition can be part of an if statement,
# joined together with "and" and "or" keywords.
#
# When two conditions are joined with and, then the result
# is true only when both conditions are true.
#
# When two conditions are joined with or, then the result
# is True if either condition is True.
print()
print("** And/Or Examples **")

if True and True:
    print("This aways be shown, because both parts are true")

if True and False:
    print("This will never be shown")

if True or False:
    print("This will always be shown, because one part is true")

if False or False:
    print("This will never be shown, because no parts are true")

print()
print("** Complex Example **")

# You can have multiple if statements inside a block, and a block of
# an if statement doesn't have to be just one line like the ones
# above. See if you can figure out what this complex condition does
# and explain it in words rather than code. Try starting with following
# which block belongs to which if statement, and then which ones
# are run when the condition for that if statement is true or false.
#
# Try changing the values of a, b, and c. Does the output match what
# you expect when you make that change?
#
# An explanation is in a comment at the end of this file after the
# complex condition.

a = 1
b = 2
c = 3

if a == b or a == c or b == c:
    print("a, b, and c should all be different!")
else:
    if a > b and a > c:
        print("a is the biggest with a value of:")
        print(a)
        
        if b > c:
            print("and it is bigger by:")
            difference = a - b
            print(difference)
        else:
            print("and it is bigger by:")
            difference = a - c
            print(difference)

    if b > a and b > c:
        print("b is the biggest with a value of:")
        print(b)

        if a > c:
            print("and it is bigger by:")
            difference = b - a
            print(difference)
        else:
            print("and it is bigger by:")
            difference = b - c
            print(difference)

    if c > b and c > a:
        print("c is the biggest with a value of:")
        print(c)

        if a > b:
            print("and it is bigger by:")
            difference = c - a
            print(difference)
        else:
            print("and it is bigger by:")
            difference = c - b
            print(difference)



# ********************************************************************
# SPOILERS BELOW! DON'T READ UNLESS YOU WANT THE ANSWER :)
# 
# 
#
#
#
# The code above checks first to see if a, b, or c are the same. If
# they are, it prints that they should be different and none of the
# rest of the code is run.
#
# If they are different, the conditions of the if statements check
# to see which is the biggest and prints it out, then showing how
# much bigger that variable is from the next biggest one.