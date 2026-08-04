"""
[Description]
Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 
Constraints:

  1 <= nums.length <= 105
  nums[i] is either 0 or 1.
  0 <= k <= nums.length

[Metadata]
- Difficulty: Medium
- Topics: Array, Binary Search, Sliding Window, Prefix Sum
- Slug: max-consecutive-ones-iii
"""

// [Solution]
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zero_count = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # Window is invalid, so shrink it
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            res = max(res, right - left + 1)

        return res