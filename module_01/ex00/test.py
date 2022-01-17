#!/usr/bin/env python3
"""
Test script for Recipe and Book Classes
"""

from recipe import Recipe, DISHTYPES
from book import Book


if __name__ == '__main__':
    print(DISHTYPES)
    DISHTYPES = ()
    tourte = Recipe('Tourte', 2, 70, ['pate', 'lardons'], "Etape1.", 'lunch')
    bread = Recipe('Bread', 4, 120, ['four', 'salt'], "Pain.", 'starter')
#    bread = Recipe('Bread', 4, 120, [4545, 'salt'], "Pain.", 'starter')
    bread.name = "Rotten bread"
    bread.cooking_lvl = 5
    print(Recipe._only_int(1))
    print('', end='\n')
    print(bread)
    print('', end='\n')
    to_print = str(tourte)
    book = Book('GoodOmens', '2019-12-01', '2018-02-14',
                {"starter": [], "lunch": [], "dessert": []})
#                {"starter": [tourte, bread], "lunch": [], "dessert": []})
#    book.get_recipe_by_name('Tourte')
    print(book._get_name())
    print(book.get_recipes_by_types('starter'))

    print(DISHTYPES)
    # Test destructor
    del tourte
    del bread
    del book
