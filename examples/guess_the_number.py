# This program combines some of the examples for a guess
# the number game. The player has a certain number of
# guesses, and after each guess it will tell them if the
# number is higher or lower. If they guess correctly,
# they win, but if they take too many guesses they lose.

print("Guess the secret number!")
print("It is between 1 and 100.")

# This is the secret number that the player will guess
secret_number = 71

# This is how many guesses the player will be allowed to
# make before losing.
num_guesses = 7

# This is the current guess the player is on. The game
# hasn't started yet, so it's guess 0.
current_guess = 0

# Whether or not the player has guessed correctly. The
# game hasn't started yet, so since the player hasn't
# made any guesses at all they haven't guessed correctly.
guessed_correctly = False

# This function gets a guess from the player. It loops
# until the player gives a valid number as a guess
def get_guess():
    while True:
        guess = input("Input a number between 1 and 100: ")

        # If the input is a valid number, convert the string to an int
        # and break out of the loop.
        # Otherwise tell the player to input a valid number and ask
        # for input again, rerunning the loop.
        if guess.isnumeric():
            guess = int(guess)

            # Check if the guess is between 1 and 100
            if guess < 0 or guess > 100:
                # Not in range, print and let the loop run again
                print("Please guess a number between 1 and 100.")
            else:
                # The input is valid, return the value
                return guess
        else:
            # Not a number. Print and let the loop run again
            print(f"'{guess}' is not a valid number.")

# ***************** MAIN GAME LOOP *********************
# As long as the current guess is less than the number of
# guesses allowed, run the main game loop.
#
# The main loop increments which guess the player is on,
# shows the player which guess they are on, gets a
# value from the player as their guess, and checks if
# it is correct or not.
while current_guess < num_guesses:
    print()

    # Increment which guess nunmber this is
    current_guess += 1

    # Check if this is the player's last guess
    last_guess = current_guess == num_guesses

    # Let the player know what guess they are on, or if it's their last guess
    print(f"You have {num_guesses}.")
    if last_guess:
        print("This is your last guess!")
    else:
        print(f"This is guess number {current_guess} of {num_guesses}")

    print()

    # Get a guess from the player
    guess = get_guess()

    # Check if the player guessed correctly. If they did, set that
    # they did and break out of the main game loop
    if guess == secret_number:
        guessed_correctly = True
        break

    # If the program is here, then the player did not guess correctly.
    # Check if it's the last guess or not. If it isn't let the player
    # know if the secret number is higher or lower than their guess.
    if not last_guess:
        print("*********************************************")
        if guess > secret_number:
            print("The secret number is lower than your guess, try again.")
        else:
            print("The secret number is higher than your guess, try again.")

# The game is over. Check if the game ended because the player guessed
# the number or not.
if guessed_correctly:
    print("Congratulations! You found the secret number!")
else:
    print("Sorry, you were not able to guess the number :(")
    print(f"The secret number was {secret_number}.")