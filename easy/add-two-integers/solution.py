"""
[Description]
Add Two Integers
https://leetcode.com/problems/add-two-integers/

Given two integers num1 and num2, return the sum of the two integers.
 
Example 1:

Input: num1 = 12, num2 = 5
Output: 17
Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

Example 2:

Input: num1 = -10, num2 = 4
Output: -6
Explanation: num1 + num2 = -6, so -6 is returned.

 
Constraints:

  -100 <= num1, num2 <= 100

[Metadata]
- Difficulty: Easy
- Topics: Math
- Slug: add-two-integers
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