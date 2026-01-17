"""
[Description]
Power of Two
https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

 
Constraints:

  -231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?

[Metadata]
- Difficulty: Easy
- Topics: Math, Bit Manipulation, Recursion
- Slug: power-of-two
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