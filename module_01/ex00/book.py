"""
Book Class Definition
"""

from datetime import date, datetime

from recipe import Recipe, DISHTYPES, only_str, isdish


class Book:
    """ Book class
    Init name, last_update, creation_date, recipe_list
    """

    def __init__(
            self, name,
            last_update=str(date.today()), creation_date=str(date.today()),
            recipe_list={dishtype: {} for dishtype in DISHTYPES}
    ):
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

    @staticmethod
    def _isdate(val):
        if datetime.strptime(val, '%Y-%m-%d'):
            return val
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @staticmethod
    def _only_dictoftype(lst):
        if isinstance(lst, dict):
            for dishtype in DISHTYPES:
                if dishtype not in lst.keys():
                    raise ValueError('Can only have dishtypes keys')
                if not isinstance(lst.get(dishtype), dict):
                    raise ValueError('Items must be of dict type')
            return dict(lst)
        raise ValueError('Value must be dict')

    def add_recipe(self, recipe):
        """Add a recipe to the book, update last_update and return true"""
        if isinstance(recipe, Recipe):
            self.__recipe_list[recipe.recipe_type].update(
                    {recipe.name: recipe}
                    )
            self.__last_update = str(date.today())
            return True
        raise ValueError("Value must be of class type Recipe")

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        only_str(name)
        for dishtype in DISHTYPES:
            if self.__recipe_list[dishtype].get(name):
                print(self.__recipe_list[dishtype][name])
                return self.__recipe_list[dishtype][name]
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        isdish(recipe_type)
        return list(self.__recipe_list[recipe_type].keys())
