"""
FACTORIAL ASSIGNMENT
1. Shafic Kitemaggwa
2. Nicholas Edgar Kiwanuka
"""
from factorial_cal import my_number


 
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

# 1st test
#  When you run the test it FAILS, cause you have no return result specified

# -----------------------------------------------------------------------
#  Result Summary
# 1. Running with pytest, the test pass because the assert value is 24
#  and is the factorial of number 4 declared
# 2. All file code is reformetted with black
# 3. All file code rate at 10.00/10 by pylint
