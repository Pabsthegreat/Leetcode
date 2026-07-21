"""
[Description]
Single Number II
https://leetcode.com/problems/single-number-ii/

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 
Example 1:
Input: nums = [2,2,3,2]
Output: 3
Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

 
Constraints:

  1 <= nums.length <= 3 * 104
  -231 <= nums[i] <= 231 - 1
  Each element in nums appears exactly three times except for one element which appears once.

[Metadata]
- Difficulty: Medium
- Topics: Array, Bit Manipulation
- Slug: single-number-ii
"""

// [Solution]
class Solution(object):
    def singleNumber(self, nums):
        res = 0

        for i in range(32):
            count = 0 #for each bit we count how many times there are 1s and if the reqd number has set bit it gets captured as it will not be a count of multiple of 3

            for num in nums:
                if (num >> i) & 1: #check bit set
                    count += 1

            if count % 3:
                res = res | (1 << i) #update the bit of res

        if res >= 2**31: #if the sign bit is set
            res -= 2**32 #negate the number

        return res