"""
[Description]
Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

 
Constraints:

  0 <= nums.length <= 105
  -109 <= nums[i] <= 109
  nums is a non-decreasing array.
  -109 <= target <= 109

[Metadata]
- Difficulty: Medium
- Topics: Array, Binary Search
- Slug: find-first-and-last-position-of-element-in-sorted-array
"""

// [Solution]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        l = len(nums)
        for i in range(l):
            if nums[i] == target:
                if start == -1:
                    start = i
            elif start != -1 and end == -1:
                end = i-1
                return [start,end]
        if start != -1 and end == -1:
            end = l-1
        return [start,end]