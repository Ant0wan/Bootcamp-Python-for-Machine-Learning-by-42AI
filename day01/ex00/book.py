# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   book.py                                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 18:25:29 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 18:25:54 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import datetime
from recipe import dishtypes


class Book(object):
    ''' Book class
 Init name, last_update, creation_date, recipe_list'''

    def __init__(self, name, last_update, creation_date, recipe_list):
        self._name = self.only_str(name)
        self._last_update = self.isdate(last_update)
        self._creation_date = self.isdate(creation_date)
        self._recipe_list = self.only_dictoftype(recipe_list)

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        return self

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = self.only_str(name)
    name = property(_get_name, _set_name)

    def _get_last_update(self):
        return self._last_update

    def _set_last_update(self, last_update):
        self._last_update = self.isdate(last_update)
    last_update = property(_get_last_update, _set_last_update)

    def _get_creation_date(self):
        return self._creation_date

    def _set_creation_date(self, creation_date):
        self._creation_date = self.only_int(creation_date)
    creation_date = property(_get_creation_date, _set_creation_date)

    def _set_recipe_list(self):
        return self._recipe_list

    def _get_recipe_list(self, recipe_list):
        self._recipe_list = self.only_list(recipe_list)
    recipe_list = property(_set_recipe_list, _get_recipe_list)

    @staticmethod
    def only_str(s):
        if isinstance(s, str):
            return str(s)
        else:
            raise ValueError('Not a valid type')

    @staticmethod
    def only_dictoftype(lst):
        if isinstance(lst, dict):
            for t in dishtypes:
                if t not in lst.keys():
                    raise ValueError('Can only have dishtypes keys')
            return dict(lst)
        else:
            raise ValueError('Value must be dict')

    @staticmethod
    def isdate(val):
        try:
            date = datetime.datetime.strptime(val, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return date
