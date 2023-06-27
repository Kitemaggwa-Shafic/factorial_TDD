# Defining the factorial calculation Logic to use in test_last_factorial.py file

# function for my_number
def my_first_func():
    """This function will do nothing just to pass and test it"""
    # pass


# ===========================================================
# modifying the function above to pass
# using the recursive method method
def my_number(number):
    """Using an if and else to try test with number and calc its factorial
    by subtracting one till its 0"""
    if number == 0:
        return 1
    return number * my_number(number - 1)