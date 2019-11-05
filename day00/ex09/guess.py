#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   guess.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 12:21:58 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 12:21:58 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from random import randint


def intro():
    print('This is an interactive guessing game!',
          'You have to enter a number between 1 and 99\
 to find out the secret number.',
          'Type \'exit\' to end the game.', 'Good luck!', sep='\n', end='\n')


if __name__ == '__main__':
    intro()
    number, user_input, attempt = randint(1, 99), 0, 0
    print(number)
    while int(user_input) is not int(number):
        try:
            user_input = input('What\'s your guess between 1 and 99?\n>> ')
            if user_input == 'exit':
                print('Goodbye!', end='\n')
                exit()
            elif int(user_input) > number:
                print('Too high!', end='\n')
            elif int(user_input) < number:
                print('Too low!', end='\n')
        except ValueError:
            print('That\'s not a number.', end='\n')
            user_input = 0
        attempt += 1
    print('Congratulations, you\'ve got it!',
          'You won in {0} attempts!'.format(attempt), sep='\n', end='\n')
