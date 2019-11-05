# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   recipe.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 18:25:29 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 18:25:54 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Recipe:
    ''' Recipe class
Init name, cooking_lvl, cooking_time, ingredients'''
    def __int__(self, name='', cooking_lvl=0, cooking_time=0,
                ingredients=[], description='', recipe_type=''):
        try:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)
        except ValueError:
            raise Exception('Could not instanciate Recipe attributes')
