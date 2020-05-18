def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:  # input is None
        return None
    if number < 0:  # return -1  if number is negative
        return -1

    low = 1
    high = number
    guess = high
    old_guess = low

    while guess != old_guess:
        old_guess = guess
        square = old_guess ** 2

        if square > number:
            high = old_guess
        elif square < number:
            low = old_guess

        guess = (high + low) // 2

    return guess


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

'''
Test case 1: 
Test if input is null number, then the return should be None
'''
print(sqrt(None))

'''
Test case 2: 
Test if input is negative number, then the return should be -1
'''
print(sqrt(-1))

'''
Test case 3: 
Test if input is large number 32103556, then the return should be 5666
'''
print(sqrt(32103556))