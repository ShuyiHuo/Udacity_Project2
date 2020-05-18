def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return -1
    if len(ints) == 1:
        return (ints[0], ints[0])

    min = ints[0]
    max = ints[0]
    pointer = 0

    while pointer < len(ints):
        if ints[pointer] < min:
            min = ints[pointer]
        if ints[pointer] > max:
            max = ints[pointer]
        pointer += 1

    return (min, max)




## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

'''
Test case 1:
Test if the length of list is 0, then the result should be -1.
'''
print(get_min_max([]))

'''
Test case 2:
Test if the list is None, then the result should be -1.
'''
print(get_min_max(None))

'''
Test case 3:
Test if the length of list is 1, then the result should be tuple of (1,1).
'''
print(get_min_max([1]))

'''
Test case 4:
Test if the function is work, then the result should be (0, 7).
'''
print(get_min_max([0, 0, 7, 2, 2, 4, 1, 1, 2, 0, 2]))