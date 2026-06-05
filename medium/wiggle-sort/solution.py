"""
[Description]
Wiggle Sort
https://leetcode.com/problems/wiggle-sort/

Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

 
Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.

Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]

 
Constraints:

  1 <= nums.length <= 5 * 104
  0 <= nums[i] <= 104
  It is guaranteed that there will be an answer for the given input nums.

 
Follow up: Could you solve the problem in O(n) time complexity?

[Metadata]
- Difficulty: Medium
- Topics: Array, Greedy, Sorting
- Slug: wiggle-sort
"""

// [Solution]
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1,n):
            if i%2==0:
                if nums[i] > nums[i-1]:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
            else:
                if nums[i] < nums[i-1]:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
            

            
