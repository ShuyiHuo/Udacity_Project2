def find_pivot(input_list):
    start = 0
    end = len(input_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if input_list[start] <= input_list[end]:
            return start
        elif input_list[start] <= input_list[mid]:
            start = mid + 1
        else:
            end = mid
    return start


def binary_search(input_list, target):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if input_list[mid] < target:
            low = mid + 1
        elif input_list[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Null input
    if input_list is None or number is None:
        return -1
    # Empty List
    if input_list == [] or number is None:
        return -1

    pivot = find_pivot(input_list)
    partA = binary_search(input_list[0:pivot], number)
    if partA != -1:
        return partA
    partB = binary_search(input_list[pivot:len(input_list)], number)

    if partB != -1:
        return partB + pivot

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

'''
Test case 1:
Test if the list or the target is none, then the result should be -1.
'''
print(rotated_array_search([], 7))
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], None))

'''
Test case 2:
Test if the target is in the list, then the result should be -1.
'''
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 5))

'''
Test case 3:
Test if the function is work, then the result should be 3.
'''
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))