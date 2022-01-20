#!/usr/bin/env python3
"""
ex01: game
"""

class GotCharacter:
    """Recipe class
    Init first_name, is_alive(default to True)
    """

    def __init__(self, first_name, is_alive=True):
        self.__first_name = first_name
        self.__is_alive = is_alive

    @property
    def first_name(self):
    """'GotCharacter first_name' property"""
        return self.__first_name

    @property
    def is_alive(self):
    """'GotCharacter is_alive' property"""
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        self.__is_alive = is_alive


class Stark(GotCharacter):
    """Recipe class
    Init family_name, house_words
    """

    def __init__(self)
        self.__family_name = "Stark"
        self.__house_words = "Winter is Coming"

    @property
    def family_name(self):
    """'Stark family_name' property"""
        return self.__family_name

    @property
    def house_words(self):
    """'Stark house_words' property"""
        return self.__house_words
