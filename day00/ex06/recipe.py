#!/usr/local/bin/python3.7
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 18:36:44 by abarthel          #+#    #+#              #
#    Updated: 2019/11/04 18:36:45 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ingredients = {
        'sandwich':['ham', 'bread', 'cheese', 'tomatoes'],
        'cake':['flour', 'sugar', 'eggs'],
        'salad':['avocado', 'arugula', 'tomatoes', 'spinach']
    }

dish = {
        'sandwich':'lunch',
        'cake':'dessert',
        'salad':'lunch'
    }

time = {
        'sandwich':10,
        'cake':60,
        'salad':15
    }

def recipe(name):
    print('Recipe for {0}:\nIngredients list: {1}\nTo be eaten for {2}.\nTakes {3} minutes of cooking.'.format(name, ingredients[name], dish[name], time[name]))

if __name__ == '__main__':
    name = input('Please enter the recipe\'s name to get its details:\n>> ')    
    try:
        recipe(name)
    except:
        exit()
