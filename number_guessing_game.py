
# Write a program to have the computer randomly select a number between 1 and
# 100, and then prompt the player to guess the number. The program should give
# hints if the guess is too high or too low.

# Generate a random number
# loop
# ask the user to make a guess
# if not a valid number
#   print error
# if number < error
#   print too low
# if number > error
#   print too high
# else
#   print well done

import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')
