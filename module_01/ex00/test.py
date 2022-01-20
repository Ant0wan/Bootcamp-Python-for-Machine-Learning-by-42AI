#!/usr/bin/env python3
"""
Test script for Recipe and Book Classes
"""

import io
import unittest
import sys

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
        """Test instantiate Recipe class object"""
        self.assertTrue(Recipe(name='Tourte', cooking_lvl=2, cooking_time=70, ingredients=['pate', 'lardons'], description="Etape1.", recipe_type=DISHTYPES[0]))
        self.assertTrue(Recipe('Tourte', 2, 70, ['pate', 'lardons'], "Etape1.", DISHTYPES[0]))
        self.assertTrue(Recipe('Bread', 4, 120, [''], "Pain.", DISHTYPES[0]))
        self.assertTrue(Recipe('Bread', 4, 120, [''], "", DISHTYPES[0]))
        with self.assertRaises(ValueError):
            Recipe('', 2, 70, ['pate', 'lardons'], "Etape1.", DISHTYPES[0])
        with self.assertRaises(ValueError):
            Recipe(2342, 2, 70, ['pate', 'lardons'], "Etape1.", 'reveil-matin')
        with self.assertRaises(TypeError):
            Recipe('', 2, 70, ['pate', 'lardons'], "Etape1.")

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

    def test_classobject_as_string(self):
        """Test Recipe class object as a string"""
        pancakes = Recipe('Pancakes', 4, 120, ['salt', 'salt'], "Pain.", 'starter')
        self.assertEqual(str(pancakes), "Name: Pancakes\nLevel: 4/5\nTime: 120min\nIngredients: salt, salt\nDescription: Pain.\nType: starter")


class TestBookClass(unittest.TestCase):
    """Test Class for Book class unit tests"""

    def test_isdate(self):
        """Test isdate staticmethod"""
        self.assertRaises(ValueError, Book._isdate, "2019-12-010")
        self.assertRaises(ValueError, Book._isdate, "2019-19-10")
        self.assertRaises(ValueError, Book._isdate, "2019-00-00")
        self.assertRaises(ValueError, Book._isdate, "0000-00-00")
        self.assertEqual(Book._isdate("2019-12-10"), "2019-12-10")

    def test_only_dictoftype(self):
        """Test only_dictoftype staticmethod"""
        self.assertRaises(ValueError, Book._only_dictoftype, {'starter': '', 'lunch': '', 'dessert': ''})
        self.assertTrue(Book._only_dictoftype({dishtype:{} for dishtype in DISHTYPES}))
        self.assertTrue(Book._only_dictoftype({dishtype:{} for dishtype in DISHTYPES[::-1]}))
        with self.assertRaises(ValueError):
            Book._only_dictoftype({dishtype:{} for dishtype in DISHTYPES[0]})
        with self.assertRaises(ValueError):
            Book._only_dictoftype({dishtype:'' for dishtype in DISHTYPES})
        with self.assertRaises(ValueError):
            Book._only_dictoftype({dishtype:[] for dishtype in DISHTYPES})
        with self.assertRaises(ValueError):
            Book._only_dictoftype({})
        with self.assertRaises(ValueError):
            Book._only_dictoftype({'':dishtype for dishtype in DISHTYPES})
        with self.assertRaises(TypeError):
            Book._only_dictoftype()

    def test_init(self):
        """Test instantiate Book class object"""
        recipe_dict = {dishtype:{} for dishtype in DISHTYPES}
        self.assertTrue(Book('TheRecipeBook', '2019-12-01', '2018-02-14', recipe_dict))
        self.assertTrue(Book('TheRecipeBook', '2019-12-01', '2022-02-14', recipe_dict))
        self.assertTrue(Book('TheRecipeBook', '2019-12-01', '2019-12-01', recipe_dict))
        rev_recipe_dict = {dishtype:{} for dishtype in DISHTYPES[::-1]}
        self.assertTrue(Book('TheRecipeBook', '2019-12-01', '2018-02-14', rev_recipe_dict))
        self.assertTrue(Book('TheRecipeBook', '2019-12-01'))
        self.assertTrue(Book('TheRecipeBook'))
        self.assertTrue(Book(name='TheRecipeBook', last_update='2019-12-01'))
        self.assertTrue(Book(name='TheRecipeBook', creation_date='2019-12-01'))
        self.assertTrue(Book(name='TheRecipeBook', recipe_list=rev_recipe_dict))
        with self.assertRaises(ValueError):
            Book('TheRecipeBook', '2019-12-01', '2018-02-14', {'':{}})
        with self.assertRaises(ValueError):
            recipe_dict = {dishtype:'' for dishtype in DISHTYPES}
            Book('TheRecipeBook', '2019-12-01', '2018-02-14', recipe_dict)
        with self.assertRaises(ValueError):
            recipe_dict = {dishtype:'' for dishtype in DISHTYPES[::-1]}
            Book('TheRecipeBook', '2019-12-01', '2018-02-14', recipe_dict)
        with self.assertRaises(ValueError):
            recipe_dict = {dishtype:[] for dishtype in DISHTYPES[0]}
            Book('TheRecipeBook', '2019-12-01', '2018-02-14', recipe_dict)
        with self.assertRaises(ValueError):
            recipe_dict = {dishtype:[] for dishtype in DISHTYPES[0]}
            Book('TheRecipeBook', '2019-13-01', '2018-02-14', recipe_dict)
        with self.assertRaises(ValueError):
            recipe_dict = {dishtype:[] for dishtype in DISHTYPES[0]}
            Book('TheRecipeBook', '2019-13-01', '2018-02-00', recipe_dict)

    def test_add_recipe(self):
        mybook = Book('TheUltimateBook')
        soba = Recipe('Soba', 5, 60, ['water', 'sarrasin'], "Nouilles de soba", DISHTYPES[0])
        self.assertTrue(mybook.add_recipe(soba))
        self.assertTrue(mybook.add_recipe(soba))
        soba = Recipe('Soba', 5, 120, ['water', 'sarrasin'], "Nouilles de soba is difficult", DISHTYPES[0])
        self.assertTrue(mybook.add_recipe(soba))

    def test_get_recipe_by_name(self):
        name_tourte = 'Tourte'
        tourte = Recipe(name_tourte, 2, 70, ['pate', 'lardons'], "Etape1.", DISHTYPES[0])
        soba = Recipe('Soba', 5, 60, ['water', 'sarrasin'], "Nouilles de soba", DISHTYPES[0])
        mybook = Book('AwesomeRecipeBook')
        mybook.add_recipe(soba)
        mybook.add_recipe(tourte)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        retval = str(mybook.get_recipe_by_name(tourte.name))
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), str(tourte) + '\n')
        self.assertEqual(retval, str(tourte))


if __name__ == '__main__':
    unittest.main(verbosity=1)
