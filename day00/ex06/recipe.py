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


def quit_fn():
    raise SystemExit


def print_a_recipe():
    try:
        name = input('Please enter the recipe\'s name to get its details:\n>> ')
        print('Recipe for {0}:\nIngredients list:\
 {1}\nTo be eaten for {2}.\nTakes {3} minutes\
 of cooking.'.format(name, cookbook[name]['ingredients'], cookbook[name]['meal'], cookbook[name]['prep_time']), end='\n')
    except KeyError:
        print(name + ' is not in the cookbook.', end='\n')


def delete_a_recipe():
    name = input('What recipe do you want to delete ?\n>> ')
    try:
        del cookbook[name]
    except KeyError:
        print(name + ' is not in the cookbook.', end='\n')


def add_a_new_recipe():
    name = input('Recipe name\n>> ')
    ingredients = input('List ingredients\n>> ')
    meal = input('What dish or meal time is it for ?\n>> ')
    prep_time = input('How long does it take to cook it ?\n>> ')
    cookbook[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}


def print_all_recipe_name():
    for i in cookbook.keys():
        print(i)


menu = {
        '1': ('Add a recipe', add_a_new_recipe),
        '2': ('Delete a recipe', delete_a_recipe),
        '3': ('Print a recipe', print_a_recipe),
        '4': ('Print the cookbook', print_all_recipe_name),
        '5': ('Quit', quit_fn)
    }


if __name__ == '__main__':
    while True:
        print('Please select an option by typing the corresponding number:')
        for i in menu:
            print(i, menu[i][0], sep=': ', end='\n')
        choice = input('>> ')
        try:
            menu[choice][1]()
        except KeyError:
            print('This option does not exist, please type the\
 corresponding number.\nTo exit, enter 5.', end='\n')
