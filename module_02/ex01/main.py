"""
ex01
"""


def what_are_the_vars(*args, **kwargs):
    """Returns an instance of class ObjectC"""
    instance = ObjectC()
    for index, arg in enumerate(args):
        setattr(instance, f"var_{index}", arg)
    for key, value in kwargs.items():
        try:
            if getattr(instance, key):
                return None
        except AttributeError:
            setattr(instance, key, value)
    return instance


# pylint: disable=missing-class-docstring,useless-object-inheritance
# pylint: disable=too-few-public-methods
class ObjectC(object):
    def __init__(self):
        pass


# pylint: disable=missing-function-docstring,redefined-outer-name
# pylint: disable=consider-using-f-string
def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
