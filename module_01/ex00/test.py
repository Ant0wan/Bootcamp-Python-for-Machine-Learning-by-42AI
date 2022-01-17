#!/usr/bin/env python3
"""
Test script for Recipe and Book Classes
"""

from recipe import Recipe
from book import Book


if __name__ == '__main__':
    tourte = Recipe('Tourte', 2, 70, ['pate', 'lardons'], "Etape1.", 'lunch')
    bread = Recipe('Bread', 4, 120, ['four', 'salt'], "Pain.", 'starter')
    to_print = str(tourte)
    book = Book('GoodOmens', '2019-12-01', '2018-02-14',
                {"starter": [], "lunch": [], "dessert": []})
#                {"starter": [tourte, bread], "lunch": [], "dessert": []})
#    book.get_recipe_by_name('Tourte')
    print(book._get_name())
    print(book.get_recipes_by_types('starter'))

    # Test destructor
    del tourte
    del bread
    del book
