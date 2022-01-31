"""
ex02
"""

import time
from random import randint
import os


def log(func):
    """Log function decorator"""

    def inner(*args, **kwargs):
        """Inner function to return for closure"""
        user = os.environ.get('USER')
        func_name = func.__name__.replace('_', ' ').title()
        start_time = time.time()
        func_result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        display_time = lambda x: f"{x*1000:.3f} ms" if x < 0.001 else f"{x:.3f} s"
        log_msg = f"({user})Running: {func_name:18} [ exec-time = {display_time(execution_time)} ]\n"
        with open('machine.log', "a+") as f:
            f.write(log_msg)
        return func_result

    return inner


# pylint: disable=missing-class-docstring
class CoffeeMachine:

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
