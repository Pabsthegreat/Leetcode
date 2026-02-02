"""
[Description]
Missing Ranges
https://leetcode.com/problems/missing-ranges/

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

 

 
Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]

Example 2:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.

 
Constraints:

  -109 <= lower <= upper <= 109
  0 <= nums.length <= 100
  lower <= nums[i] <= upper
  All the values of nums are unique.

[Metadata]
- Difficulty: Easy
- Topics: Array
- Slug: missing-ranges
"""

// [Solution]
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        if not nums:
            return [[lower,upper]]
        l = []
        prev = 0
        temp = []
        if nums[0] > lower:
            l.append([lower,nums[0]-1])
            prev = nums[0]
        else:
            prev = nums[0]
        for i in range(1,len(nums)):
            diff = nums[i] - prev
            if diff == 1:
                prev = nums[i]
            else:
                l.append([prev+1,nums[i]-1])
                prev = nums[i]
        if prev < upper:
            l.append([prev+1,upper])
            prev = upper
        print(prev,l)
        return l