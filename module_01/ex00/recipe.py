"""
Recipe Class Definition
"""

DISHTYPES = ('starter', 'lunch', 'dessert')


class Recipe:
    """Recipe class
    Init name, cooking_lvl, cooking_time, ingredients, description and type
    """

    # pylint: disable=too-many-arguments
    def __init__(self, name, lvl, time, ing, des, typ):
        self.__name = self._only_str(name)
        self.__cooking_lvl = self._btwrange(lvl)
        self.__cooking_time = self._uptoinf(time)
        self.__ingredients = self._only_list(ing)
        self.__description = self._only_str(des)
        self.__recipe_type = self._isdish(typ)

    def __str__(self):
        """Return the string to print with the recipe info"""
        return f"{self.__name}\
                \nLevel: {self.__cooking_lvl}/5\
                \nTime: {self.__cooking_time}min\
                \nIngredients: {', '.join(self.__ingredients)}\
                \n{self.__description}\
                \nType: {self.__recipe_type}"

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
        self.__name = self._only_str(name)

    @cooking_lvl.setter
    def cooking_lvl(self, lvl):
        self.__cooking_lvl = self._btwrange(lvl)

    @cooking_time.setter
    def cooking_time(self, time):
        self.__cooking_time = self._only_int(time)

    @ingredients.setter
    def ingredients(self, ing):
        self.__ingredients = self._only_list(ing)

    @description.setter
    def description(self, des):
        self.__description = self._only_str(des)

    @recipe_type.setter
    def recipe_type(self, typ):
        self.__recipe_type = self._isdish(typ)

    @staticmethod
    def _only_str(string):
        """Check whether it is string"""
        if isinstance(string, str):
            return str(string)
        raise ValueError('Not a valid type')

    @staticmethod
    def _only_int(number):
        """Check whether it is integer"""
        if isinstance(number, int):
            return int(number)
        raise ValueError('Not a valid type')

    @staticmethod
    def _only_list(lst):
        """Check whether it is a list"""
        if isinstance(lst, list):
            return list(lst)
        raise ValueError('Value must be list')

    @staticmethod
    def _btwrange(number):
        """Check whether number is in range"""
        number = Recipe._only_int(number)
        if int(number) in range(1, 6):
            return number
        raise ValueError('Value must be between 1 to 5')

    @staticmethod
    def _uptoinf(number):
        """Check whether the number is greater than 0"""
        number = Recipe._only_int(number)
        if int(number) >= 0:
            return number
        raise ValueError('Value must be between 0 to +inf')

    @staticmethod
    def _isdish(string):
        """Check whether it is a dish"""
        string = Recipe._only_str(string)
        if string in DISHTYPES:
            return string
        raise ValueError('Not a valid dish')
