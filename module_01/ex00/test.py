#!/usr/bin/env python3
"""
Test script for Recipe and Book Classes
"""

import unittest

from recipe import *

from book import Book


class TestRecipeModule(unittest.TestCase):
    """Test Class for functions and constant from recipe module"""

    def test_dishtypes_constant_value(self):
        """Test DISHTYPES validity"""
        self.assertIsInstance(DISHTYPES, tuple, "given DISHTYPES is not instance of tuple")
        self.assertTrue(DISHTYPES)

    def test_notfalsy(self):
        """Test notfalsy function"""
        self.assertRaises(ValueError, notfalsy, "")
        self.assertRaises(ValueError, notfalsy, 0)
        self.assertRaises(ValueError, notfalsy, ())
        self.assertRaises(ValueError, notfalsy, [])
        self.assertRaises(ValueError, notfalsy, (""))
        self.assertEqual(notfalsy(("", 0)), ("", 0))
        self.assertEqual(notfalsy(" "), " ")

    def test_only_str(self):
        """Test only_str function"""
        self.assertRaises(ValueError, only_str, 321)
        self.assertRaises(ValueError, only_str, ())
        self.assertRaises(ValueError, only_str, ("Hello", "Bla"))
        self.assertEqual(only_str(""), "")
        self.assertEqual(only_str(" "), " ")
        self.assertEqual(only_str("Hello world 321"), "Hello world 321")

    def test_only_int(self):
        """Test only_int function"""
        self.assertRaises(ValueError, only_int, "Hello")
        self.assertRaises(ValueError, only_int, "12")
        self.assertRaises(ValueError, only_int, "")
        self.assertRaises(ValueError, only_int, (12, 11))
        self.assertRaises(ValueError, only_int, ("Hello", 11))
        self.assertEqual(only_int(0), 0)
        self.assertEqual(only_int(3213210), 3213210)
        self.assertEqual(only_int(-1), -1)

    def test_only_strlist(self):
        """Test only_strlist function"""
        self.assertRaises(ValueError, only_strlist, "Hello")
        self.assertRaises(ValueError, only_strlist, ("plop", "toto"))
        self.assertRaises(ValueError, only_strlist, 0)
        self.assertRaises(ValueError, only_strlist, ["Toto", 0, ["Hey"]])
        self.assertEqual(only_strlist(["Hello", "World"]), ["Hello", "World"])
        self.assertEqual(only_strlist(["", "World"]), ["", "World"])

    def test_btwrange(self):
        """Test btwrange function"""
        self.assertRaises(ValueError, btwrange, "Hello")
        self.assertRaises(ValueError, btwrange, -1)
        self.assertRaises(ValueError, btwrange, 0)
        self.assertRaises(ValueError, btwrange, 6)
        self.assertRaises(ValueError, btwrange, 4.5)
        self.assertRaises(ValueError, btwrange, ())
        self.assertRaises(ValueError, btwrange, [2])
        self.assertRaises(ValueError, btwrange, (2, 3))
        self.assertEqual(btwrange(1), 1)
        self.assertEqual(btwrange(2), 2)
        self.assertEqual(btwrange(3), 3)
        self.assertEqual(btwrange(4), 4)
        self.assertEqual(btwrange(5), 5)

    def test_uptoinf(self):
        """Test uptoinf function"""
        self.assertRaises(ValueError, uptoinf, [2])
        self.assertRaises(ValueError, uptoinf, "")
        self.assertRaises(ValueError, uptoinf, " ")
        self.assertRaises(ValueError, uptoinf, (0, 1))
        self.assertRaises(ValueError, uptoinf, -1)
        self.assertRaises(ValueError, uptoinf, 0.12)
        self.assertRaises(ValueError, uptoinf, -0.9999)
        self.assertEqual(uptoinf(1), 1)
        self.assertEqual(uptoinf(0), 0)
        self.assertEqual(uptoinf(100000), 100000)

    def test_isdish(self):
        """Test isdish function"""
        self.assertRaises(ValueError, isdish, "")
        self.assertRaises(ValueError, isdish, 123)
        self.assertRaises(ValueError, isdish, ["", "Hello"])
        self.assertEqual(isdish(DISHTYPES[0]), DISHTYPES[0])


class TestRecipeClass(unittest.TestCase):
    """Test Class for Recipe class unit tests"""

    def test_init(self):
        """Test instantiate Recipe class"""
        tourte = Recipe(name='Tourte', cooking_lvl=2, cooking_time=70, ingredients=['pate', 'lardons'], description="Etape1.", recipe_type='lunch')
        bread = Recipe('Bread', 4, 120, ['four', 'salt'], "Pain.", 'starter')

    def test_getters(self):
        """Test Recipe getters"""
        name, cooking_lvl, cooking_time = 'Bread', 4, 120
        ingredients, description, recipe_type = ['four', 'salt'], 'Pain.', DISHTYPES[0]
        bread = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
        self.assertEqual(bread.name, name)
        self.assertEqual(bread.cooking_lvl, cooking_lvl)
        self.assertEqual(bread.cooking_time, cooking_time)
        self.assertEqual(bread.ingredients, ingredients)
        self.assertEqual(bread.description, description)
        self.assertEqual(bread.recipe_type, recipe_type)

    def test_setters(self):
        """Test Recipe setters"""
        bread = Recipe('Bread', 4, 120, ['four', 'salt'], 'C\'est du pain', DISHTYPES[0])
        bread.name = 'Pain'
        self.assertEqual(bread.name, 'Pain')
        bread.cooking_lvl = 3
        self.assertEqual(bread.cooking_lvl, 3)
        bread.cooking_time = 90
        self.assertEqual(bread.cooking_time, 90)
        bread.ingredients = ['four', 'water']
        self.assertEqual(bread.ingredients, ['four', 'water'])
        bread.description = 'C\'est aussi du pain'
        self.assertEqual(bread.description, 'C\'est aussi du pain')
        bread.recipe_type = DISHTYPES[0]
        self.assertEqual(bread.recipe_type, DISHTYPES[0])

    #def test_false_init(self):
    #    self.assertRaises(ValueError, Recipe("", 4, 120, ['four', 'salt'], "Pain.", 'starter'))

#    def test_(self):
#        """Test """
#        self.


if __name__ == '__main__':
    unittest.main()
##    bread = Recipe("", 4, 120, ['four', 'salt'], "Pain.", 'starter')
##    bread = Recipe(0, 4, 120, ['four', 'salt'], "Pain.", 'starter')
##    bread = Recipe('Bread', 4, 120, [4545, 'salt'], "Pain.", 'starter')
#    bread.name = "Rotten bread"
#    bread.cooking_lvl = 5
#    print('', end='\n')
#    print(bread)
#    print('', end='\n')
#    to_print = str(tourte)
#    book = Book('GoodOmens', '2019-12-01', '2018-02-14',
#                {"starter": [], "lunch": [], "dessert": []})
##                {"starter": [tourte, bread], "lunch": [], "dessert": []})
##    book.get_recipe_by_name('Tourte')
#    print(book.name )
#    print(book.get_recipes_by_types('starter'))
#
#    # Test destructor
#    del tourte
#    del bread
#    del book
