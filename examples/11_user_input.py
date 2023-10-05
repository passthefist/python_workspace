print("*+++++++++++++++++++ Simple Loop Examples ++++++++++++++++++++++++++")
print()

# So far, these example programs have just run through their code
# each time without any user input, which isn't that realistic.
# Part of the point of any program is to interact with a user or
# some other information that's not part of the program's code.
#
# There's many ways to do this, but the most simple is to give
# a user a prompt to enter a value on the command line.
#
# In Python, the built in input() function is used to do this.
# It takes a string that will be shown as part of the prompt to
# the user for their input.

user_input = input("Please type something: ")
print(f"You typed {user_input}")

# Sometimes a program needs to wait for some specific input.
# Here, a while loop will ask for input until the user types
# 'yes' for the prompt.
while True:
    continue_running = input("Type yes to continue: ")

    if continue_running.lower() == "yes":
        break

# Similarly, a while loop can be used to make sure the input
# from a user is valid. In general, a program shouldn't trust
# that the input from a user will be as expected. It's good
# practice to try and validate input as best you can.
x = input("Now type a number: ")
while not x.isnumeric():
    print("Please was not a number.")
    x = input("Please type a valid number: ")

# This loop does the same thing as the one above, but with
# a different variable. 
y = input("Please type a number: ")
while not y.isnumeric():
    print("That was not a number.")
    y = input("Please type a valid number: ")

x = int(x)
y = int(y)
sum = x + y

print(f"The sum of the numbers you entered is {sum}") 

# Since the loops above did the same thing, they could
# be a function instead of repeating the same code.

def get_number():
    value = input("Please type a number: ")
    while not value.isnumeric():
        print("That was not a number.")
        value = input("Please type a valid number: ")
    
    return value

print(f"Now type three numbers.")

x = get_number()
y = get_number()
z = get_number()

print(f"The sum of the three numbers is {x + y + z}")