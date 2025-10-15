# Write a program that simulates rolling a pair of dice. Each time the program runs, it
# should randomly generate two numbers between 1 and 6 (inclusive), representing
# the result of each die. The program should then display the results and ask if the
# user would like to roll again?

# Ask: the user roll the Dice ?
# If user enters y
#  Generate two random numbers
#  print them
# If user enters n
#  print thank you message
#  Terminate
# Else
#  print invalid choice

import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
