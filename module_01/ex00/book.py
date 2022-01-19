"""
Book Class Definition
"""

import datetime

from recipe import DISHTYPES, only_str, only_int, only_strlist


class Book:
    """ Book class
    Init name, last_update, creation_date, recipe_list
    """

    # pylint: disable=too-many-arguments
    def __init__(self, name, last_update, creation_date, recipe_list):
        self.__name = only_str(name)
        self.__last_update = self._isdate(last_update)
        self.__creation_date = self._isdate(creation_date)
        self.__recipe_list = self._only_dictoftype(recipe_list)

    @property
    def name(self):
        """'Name' property"""
        return self.__name

    @property
    def recipe_list(self):
        """'Recipe_list' property"""
        return self.__recipe_list

    @property
    def last_update(self):
        """'Last_update' property"""
        return self.__last_update

    @property
    def creation_date(self):
        """'Creation_date' property"""
        return self.__creation_date

    @name.setter
    def name(self, name):
        self.__name = only_str(name)

    @last_update.setter
    def last_update(self, last_update):
        self.__last_update = self._isdate(last_update)

    @creation_date.setter
    def creation_date(self, creation_date):
        self.__creation_date = only_int(creation_date)

    @recipe_list.setter
    def recipe_list(self, recipe_list):
        self.__recipe_list = only_strlist(recipe_list)

    @staticmethod
    def _isdate(val):
        if datetime.datetime.strptime(val, '%Y-%m-%d'):
            return val
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# broken method
    @staticmethod
    def _only_dictoftype(lst):
        if isinstance(lst, dict):
            for dishtype in DISHTYPES:
                if dishtype not in lst.keys():
                    raise ValueError('Can only have dishtypes keys')
                if not isinstance(lst.get(dishtype), list):
                    raise ValueError('Items must be of list type')
            return dict(lst)
        raise ValueError('Value must be dict')

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        only_str(name)
        for dishtype in DISHTYPES:
            if self.__recipe_list.get(dishtype):
                if name is self.__recipe_list.get(dishtype)[0].name:
                    print(self.__recipe_list.get(dishtype)[0])
                    return self.__recipe_list.get(dishtype)
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        only_str(recipe_type)
        if recipe_type in DISHTYPES:
            allnames = []
            for i in self.__recipe_list.get(recipe_type):
                allnames.append(i.name)
            if allnames:
                return allnames
        return None

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            print(recipe)
            pass
        raise ValueError('Value must be of type Recipe')
