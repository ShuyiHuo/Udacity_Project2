Problem:

You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Explanation:

The main idea for this problem is binary search method.
Firstly I find the pivot point and then I split the array two parts
by the pivot point. Finally, I apply the binary search method in both parts to find the
target. The time complexity is O(log(n)) since binary search method and the space
complexity is O(1).
