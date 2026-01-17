"""
[Description]
Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 
Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:

Input: arr = [1,1]
Output: 1

 
Constraints:

  1 <= arr.length <= 104
  0 <= arr[i] <= 105

[Metadata]
- Difficulty: Easy
- Topics: Array
- Slug: element-appearing-more-than-25-in-sorted-array
"""

// [Solution]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in ind:
                return [ind[complement], i] 
            
            ind[nums[i]] = i
        
        return None