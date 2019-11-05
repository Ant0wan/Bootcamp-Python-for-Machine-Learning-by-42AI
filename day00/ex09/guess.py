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
    print('This is an interactive guessing game!', 'You have to enter a number between 1 and 99 to find out the secret number.', 'Type \'exit\' to end the game.', 'Good luck!', sep='\n', end='\n')


if __name__ == '__main__':
    number = randint(1, 99)
    intro()
    user_input = 0
    while user_input is not number:
        user_input = int(input('What\'s your guess between 1 and 99?\n>> '))
        if user_input > number:
            print('Too high!', end='\n')
        elif user_input < number:
            print('Too low!', end='\n')
    if user_input is number:
        print('Congratulations, you\'ve got it!')
