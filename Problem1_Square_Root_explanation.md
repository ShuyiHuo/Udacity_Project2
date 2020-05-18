Problem:

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n)).

Explanation:

In this problem, I used the bisection method to find the square root.
Given a positive integer, find the square of the mid value and then
compare to the integer to determine the new mid value. The time complexity
is O(log(n)) because of bisection method and space complexity is
O(1).
