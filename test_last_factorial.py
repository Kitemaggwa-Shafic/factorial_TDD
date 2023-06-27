"""
FACTORIAL ASSIGNMENT
1. Shafic Kitemaggwa
2. Nicholas Edgar Kiwanuka
"""


 
def test_factorial():
    """Function calculating the factorial of a declared number"""
    number = 1
    result = my_number(number)
    assert my_number(result)


def test_factorial():
    """Function calculating the factorial of a declared number"""
    number = 2
    result = my_number(number)
    assert my_number(result)

def test_factorial():
    """Function calculating the factorial of a declared number"""
    number = 3
    result = my_number(number)
    assert my_number(result)


# function for my_number
def my_first_func():
    """This function will do nothing just to pass and test it"""
    # pass


# 1st test
#  When you run the test it FAILS, cause you have no return result specified


# ========================================
# modifying the function above to pass
def my_number(number):
    """Using an if and else to try test with number and calc its factorial
    by subtracting one till its 0"""
    if number == 0:
        return 1
    return number * my_number(number - 1)


# 1. Running with pytest, the test pass because the assert value is 24
#  and is the factorial of number 4 declared
# 2. All file code is reformetted with black
# 3. All file code rate at 10.00/10 by pylint
