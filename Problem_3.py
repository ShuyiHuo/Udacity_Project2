def mergesort(input):
    if len(input) <= 1:
        return input

    mid = len(input) // 2
    left = input[:mid]
    right = input[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) == 0:
        return -1, -1

    if len(input_list) == 1:
        return input_list[0], 0

    input_list = mergesort(input_list)
    input_list.reverse()  # Python method
    num1 = ""
    num2 = ""
    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 += str(input_list[i])
        if i % 2 == 1:
            num2 += str(input_list[i])
    return int(num1), int(num2)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

'''
Test case 1:
Test if the length of list is 0, then the result should be -1.
'''
print(rearrange_digits([]))

'''
Test case 2:
Test if the list is None, then the result should be -1.
'''
print(rearrange_digits(None))

'''
Test case 3:
Test if the function is work, then the result should be (964, 852).
'''
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
