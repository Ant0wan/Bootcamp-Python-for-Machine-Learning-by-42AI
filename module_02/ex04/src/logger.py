"""
ex02
"""

from random import randint

import os
import time


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

        if execution_time < 0.001:
            fmtime = f"{execution_time * 1000:.3f} ms"
        else:
            fmtime = f"{execution_time:.3f} s"
        log_msg = f"({user})Running: {func_name:18} [ exec-time = {fmtime} ]\n"

        with open('machine.log', "at", encoding='utf-8') as file:
            file.write(log_msg)
        return func_result

    return inner


# pylint: disable=missing-class-docstring,missing-function-docstring
# pylint: disable=no-else-return,no-self-use
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
