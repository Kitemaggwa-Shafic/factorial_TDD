"""
FACTORIAL ASSIGNMENT
1. Shafic Kitemaggwa
2. Nicholas Edgar Kiwanuka
"""
import math

# Using the MTC first principles of calculating factorial of a number with Maths


# We defined function test_one_1() as below
def test_one_1():
    """Function calculating 1!"""
    number = 1
    # factorial = math.factorial(1)
    factorial = math.factorial(number)
    assert factorial == 1


def test_one_2():
    """Function calculating 2!"""
    number = 2
    factorial = math.factorial(number)
    assert factorial == 2


def test_one_3():
    """Function calculating 3!"""
    number = 3
    factorial = math.factorial(number)
    assert factorial == 6


def test_one_4():
    """Function calculating 4!"""
    number = 4
    factorial = math.factorial(number)
    assert factorial == 24


# 1. Running all tests with pytest, they pass because the assert factorial values match
# with the factorial of the declared numbers
# 2. All file code is reformetted with black
# 3. All file code rate at 10.00/10 by pylint
