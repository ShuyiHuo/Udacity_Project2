Problem:

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Explanation:

According to Wikipedia, the idea for this problem is set three pointers:
one for start, one for end and one for pointer to traversal the whole list.
Then comparing the pointer value and 1, if the pointer value is less than 1,
swap the start value and the pointer value. If the pointer value is greater than 1,
swap the end value and the pointer value. Thus, it only sort the array in a single traversal.
The time complex is O(n) and the space complex is O(1).