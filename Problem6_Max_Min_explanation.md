Problem:

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
Bonus Challenge: Is it possible to find the max and min in a single traversal?

Explanation:

The main idea for this problem is using pointer to traversal the list.
If the pointer value in the list is smaller than the min value, then set new min value as
the pointer value. Similar to max value. Thus after a single traversal, the min and max
value will be find. The time complex is O(n) and the space complex is O(1).