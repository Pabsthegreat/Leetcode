"""
[Description]
Rotate Array
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 
Constraints:

  1 <= nums.length <= 105
  -231 <= nums[i] <= 231 - 1
  0 <= k <= 105

 
Follow up:

  Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
  Could you do it in-place with O(1) extra space?

[Metadata]
- Difficulty: Medium
- Topics: Array, Math, Two Pointers
- Slug: rotate-array
"""

// [Solution]
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        start = 0
        count = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_index = (current + k) % n
                nums[next_index], prev = prev , nums[next_index]
                current = next_index
                count += 1
                if current == start:
                    break
            start += 1