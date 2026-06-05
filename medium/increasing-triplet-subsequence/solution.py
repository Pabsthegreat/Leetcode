"""
[Description]
Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 
Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.

 
Constraints:

  1 <= nums.length <= 5 * 105
  -231 <= nums[i] <= 231 - 1

 
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

[Metadata]
- Difficulty: Medium
- Topics: Array, Greedy
- Slug: increasing-triplet-subsequence
"""

// [Solution]
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = float('inf')
        s = f
        for i in nums:
            if i <= f:
                f = i
            elif  i<= s: #dont update second since it just remembers that there is a smaller value, the value dosent matter to second
                s = i
            else:
                return True
        return False