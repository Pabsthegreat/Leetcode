"""
[Description]
Majority Element
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

 
Constraints:

  n == nums.length
  1 <= n <= 5 * 104
  -109 <= nums[i] <= 109
  The input is generated such that a majority element will exist in the array.

 
Follow-up: Could you solve the problem in linear time and in O(1) space?

[Metadata]
- Difficulty: Easy
- Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting
- Slug: majority-element
"""

// [Solution]
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        t = len(nums)//2
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > t:
                    return i
            else:
                d[i] = 1
                if d[i] > t:
                    return i