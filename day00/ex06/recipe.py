#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   recipe.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 18:36:44 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 18:36:45 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

cookbook = {
        'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': '10'},
        'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': '60'},
        'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': '15'}
    }


def recipe(name):
    print('Recipe for {0}:\nIngredients list:\
 {1}\nTo be eaten for {2}.\nTakes {3} minutes\
 of cooking.'.format(name, cookbook[name]['ingredients'], cookbook[name]['meal'], cookbook[name]['prep_time']), end='\n')


if __name__ == '__main__':
    name = input('Please enter the recipe\'s name to get its details:\n>> ')
    try:
        recipe(name)
    except KeyError:
        print('This option does not exist, please type the\
 corresponding number.\nTo exit, enter 5.', end='\n')
