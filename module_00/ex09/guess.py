#!/usr/bin/env python3
"""
guess
"""

from random import randint
import sys


def intro():
    """Introduction"""
    print('This is an interactive guessing game!',
          'You have to enter a number between 1 and 99\
 to find out the secret number.',
          'Type \'exit\' to end the game.', 'Good luck!', sep='\n', end='\n')


if __name__ == '__main__':
    intro()
    number, USER_INPUT, attempt = randint(1, 99), 0, 0
    while int(USER_INPUT) is not int(number):
        try:
            USER_INPUT = input('What\'s your guess between 1 and 99?\n>> ')
            if USER_INPUT == 'exit':
                print('Goodbye!', end='\n')
                sys.exit()
            elif int(USER_INPUT) > number:
                print('Too high!', end='\n')
            elif int(USER_INPUT) < number:
                print('Too low!', end='\n')
        except ValueError:
            print('That\'s not a number.', end='\n')
            USER_INPUT = 0
        attempt += 1
    print('Congratulations, you\'ve got it!',
          f'You won in {attempt} attempts!', sep='\n', end='\n')
