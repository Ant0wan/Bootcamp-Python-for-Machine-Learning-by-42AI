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

    def __init__(self, name, lvl, time, ing, des, typ):
        self._name = self.only_str(name)
        self._cooking_lvl = self.btwrange(lvl)
        self._cooking_time = self.only_int(time)
        self._ingredients = self.only_list(ing)
        self._description = self.only_str(des)
        self._recipe_type = self.isdish(typ)

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = self._name
        txt += '\nLevel: ' + str(self._cooking_lvl) + '/5'
        txt += '\nTime: ' + str(self._cooking_time) + 'min'
        txt += '\nIngredients: ' + ', '.join(self._ingredients)
        txt += '\n' + self._description
        txt += '\nType: ' + self._recipe_type
        return txt

    @property
    def name(self):
        """'Name' property"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = self.only_str(name)

    @property
    def cooking_lvl(self):
        """'Cooking level' property"""
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, lvl):
        self._cooking_lvl = self.btwrange(lvl)

    @property
    def cooking_time(self):
        """'Cooking time' property"""
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, time):
        self._cooking_time = self.only_int(time)

    @property
    def ingredients(self):
        """'Ingredients' property"""
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ing):
        self._ingredients = self.only_list(ing)

    @property
    def description(self):
        """'Name' property"""
        return self._description

    @description.setter
    def description(self, des):
        self._description = self.only_str(des)

    @property
    def recipe_type(self):
        """'Name' property"""
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, typ):
        self._recipe_type = self.isdish(typ)

    @staticmethod
    def only_str(s):
        if isinstance(s, str):
            return str(s)
        else:
            raise ValueError('Not a valid type')

    @staticmethod
    def only_int(n):
        if isinstance(n, int):
            return int(n)
        else:
            raise ValueError('Not a valid type')

    @staticmethod
    def only_list(lst):
        if isinstance(lst, list):
            return list(lst)
        else:
            raise ValueError('Value must be list')

    @classmethod
    def btwrange(self, n):
        n = self.only_int(n)
        if int(n) in range(1, 6):
            return n
        else:
            raise ValueError('Value must be between 1 to 5')

    @classmethod
    def uptoinf(self, n):
        n = self.only_int(n)
        if int(n) >= 0:
            return n
        else:
            raise ValueError('Value must be between 0 to +inf')

    @classmethod
    def isdish(self, s):
        dishtypes = ['starter', 'lunch', 'dessert']
        s = self.only_str(s)
        if s in dishtypes:
            return s
        else:
            raise ValueError('Not a valid dish')
