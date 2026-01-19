"""
[Description]
Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

 
Constraints:

  1 <= nums.length <= 105
  nums[i] is either 0 or 1.

[Metadata]
- Difficulty: Easy
- Topics: Array
- Slug: max-consecutive-ones
"""

// [Solution]
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        t = 0
        for i in nums:
            if i == 0:
                m = max(t,m)
                t = 0
            else:
                t += 1
        return max(t,m)