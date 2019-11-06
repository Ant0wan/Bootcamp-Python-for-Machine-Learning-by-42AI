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


class Recipe(object):
    ''' Recipe class
Init name, cooking_lvl, cooking_time, ingredients'''
    def __init__(self, name=None):
        self._name = name

    def notvalid():
        print('Not a valid type')

    @property
    def name(self):
        """I'm the 'name' property."""
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            notvalid()

'''
        try:
            if str(name) and not name:
                self.name = name
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)
        except ValueError:
            raise Exception('Could not instanciate Recipe attributes')
'''
