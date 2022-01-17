"""
Recipe Class Definition
"""

dishtypes = ('starter', 'lunch', 'dessert')


class Recipe(object):
    ''' Recipe class
 Init name, cooking_lvl, cooking_time, ingredients, description and type'''

    def __init__(self, name, lvl, time, ing, des, typ):
        self.__name = self.only_str(name)
        self.__cooking_lvl = self.btwrange(lvl)
        self.__cooking_time = self.only_int(time)
        self.__ingredients = self.only_list(ing)
        self.__description = self.only_str(des)
        self.__recipe_type = self.isdish(typ)

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = self.__name
        txt += '\nLevel: ' + str(self.__cooking_lvl) + '/5'
        txt += '\nTime: ' + str(self.__cooking_time) + 'min'
        txt += '\nIngredients: ' + ', '.join(self.__ingredients)
        txt += '\n' + self.__description
        txt += '\nType: ' + self.__recipe_type
        return txt

    def __del__(self):
        """Destructor"""
        print(f'{self.name} deleted')

    @property
    def name(self):
        """'Name' property"""
        return self.__name

    @property
    def cooking_lvl(self):
        """'Cooking level' property"""
        return self.__cooking_lvl

    @property
    def cooking_time(self):
        """'Cooking time' property"""
        return self.__cooking_time

    @property
    def ingredients(self):
        """'Ingredients' property"""
        return self.__ingredients

    @property
    def description(self):
        """'Description' property"""
        return self.__description

    @property
    def recipe_type(self):
        """'Recipe type' property"""
        return self.__recipe_type

    @name.setter
    def name(self, name):
        self.__name = self.only_str(name)

    @cooking_lvl.setter
    def cooking_lvl(self, lvl):
        self.__cooking_lvl = self.btwrange(lvl)

    @cooking_time.setter
    def cooking_time(self, time):
        self.__cooking_time = self.only_int(time)

    @ingredients.setter
    def ingredients(self, ing):
        self.__ingredients = self.only_list(ing)

    @description.setter
    def description(self, des):
        self.__description = self.only_str(des)

    @recipe_type.setter
    def recipe_type(self, typ):
        self.__recipe_type = self.isdish(typ)

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
        s = self.only_str(s)
        if s in dishtypes:
            return s
        else:
            raise ValueError('Not a valid dish')
