# According from https://en.wikipedia.org/wiki/Dutch_national_flag_problem

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Null input
    if input_list is None:
        return -1
    # Empty List input
    if input_list == []:
        return -1
    start = 0  # start point
    pointer = 0  # a pointer to traversal the list
    mid = 1  # end point
    end = len(input_list) - 1

    while pointer <= end:

        if input_list[pointer] < mid:
            # swap
            temp = input_list[start]
            input_list[start] = input_list[pointer]
            input_list[pointer] = temp
            start += 1
            pointer += 1
        elif input_list[pointer] > mid:
            # swap
            temp = input_list[pointer]
            input_list[pointer] = input_list[end]
            input_list[end] = temp
            end -= 1
        else:
            pointer += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

'''
Test case 1:
Test if the length of list is 0, then the result should be -1.
'''
print(sort_012([]))

'''
Test case 2:
Test if the list is None, then the result should be -1.
'''
print(sort_012(None))

'''
Test case 3:
Test if the function is work, then the result should be (964, 852).
'''
print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
