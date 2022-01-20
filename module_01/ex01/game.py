"""
ex01: game
"""


class GotCharacter:
    """Recipe class
    Init first_name, is_alive(default to True)
    """

    def __init__(self, first_name, is_alive=True):
        self.__first_name = str(first_name)
        self.__is_alive = bool(is_alive)

    @property
    def first_name(self):
        """'first_name' property"""
        return self.__first_name

    @property
    def is_alive(self):
        """'is_alive' property"""
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        self.__is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family.\
 Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.__family_name = "Stark"
        self.__house_words = "Winter is Coming"

    @property
    def family_name(self):
        """'family_name' property"""
        return self.__family_name

    @property
    def house_words(self):
        """'house_words' property"""
        return self.__house_words

    def print_house_words(self):
        """Display the house words"""
        print(self.__house_words)

    def die(self):
        """Set is_alive to False"""
        self.is_alive = False
