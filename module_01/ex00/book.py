"""
Book Class Definition
"""

import datetime

from recipe import DISHTYPES, only_str, only_int, only_list


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
        return self.__recipe_list

    @property
    def last_update(self):
        return self.__last_update

    @property
    def creation_date(self):
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
        self.__recipe_list = only_list(recipe_list)

    @staticmethod
    def _only_dictoftype(lst):
        if isinstance(lst, dict):
            for t in DISHTYPES:
                if t not in lst.keys():
                    raise ValueError('Can only have dishtypes keys')
                if not isinstance(lst.get(t), list):
                    raise ValueError('Items must be of list type')
            return dict(lst)
        else:
            raise ValueError('Value must be dict')

    @staticmethod
    def _isdate(val):
        try:
            date = datetime.datetime.strptime(val, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return date

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        only_str(name)
        for t in DISHTYPES:
            if self.__recipe_list.get(t):
                if name is self.__recipe_list.get(t)[0].name:
                    print(self.__recipe_list.get(t)[0])
                    return self.__recipe_list.get(t)
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        only_str(recipe_type)
        if recipe_type in DISHTYPES:
            allnames = list()
            for i in self.__recipe_list.get(recipe_type):
                allnames.append(i.name)
            if allnames:
                return allnames
        return None

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
